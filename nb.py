# pip install opencv-python 
# pip install opencv-python==4.5.5.64
# !pip install easyocr

from datetime import datetime
import os
import csv
import cv2
import easyocr
import random

# setting folder for frames images
upload_folder= r'\upload'
current_working_directory =os.getcwd()
path_of_file = "".join([current_working_directory, upload_folder])

# with open('records.csv', 'w', newline='') as csvfile: 
#     csvwriter = csv.writer(csvfile) 
#     csvwriter.writerows([["Jobs","Count"]])

# if upload folder does not exists
isExist = os.path.exists(path_of_file)
if not isExist:    
  os.makedirs(path_of_file)
  print("The new directory is created!")


images_frames = []

# get images from camera
camera_time = 2
webCam = cv2.VideoCapture(0)
currentframe = 0
start_time = datetime.now()
while (True):
    success, frame = webCam.read()
    temp = 'Frame' + str(currentframe) + '.jpg'
    images_frames.append(temp)
    fpath = os.path.join(path_of_file,temp)
    cv2.imwrite(fpath,frame)
    currentframe += 1
    time_delta = datetime.now() - start_time
    if time_delta.total_seconds() >= camera_time:
        break

webCam.release()


# get output text from image frame
def runScriptPy(index,images_frames):
  # print(path_of_file)
  folder = path_of_file
  filename = images_frames[index]
  img1 = cv2.imread(os.path.join(folder,filename))
  img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  equ = cv2.equalizeHist(img1)
  reader = easyocr.Reader(['en'], gpu=False)
  result = reader.readtext(equ)
  # print("result --> ",result)

  output = ""
  for detection in result:
    text = detection[1]
    output = output + text + " "

  def transformStr(str):
      str = ''.join(e for e in str if e.isalnum())
      str = str.upper()
      return str

  output = transformStr(output)
  print("output --> ",output)    
  return output

def image_frames_handler():
  # images_frames = os.listdir(path_of_file)
  # print(images_frames)
  images_to_be_sampled = 5
  frames_indices = random.sample(range(1, len(images_frames)), images_to_be_sampled)
  frames_indices.sort()

  results = {}
  for i in frames_indices:
    output = runScriptPy(i,images_frames)
    if(output!=""):
      if(results.get(output) == None):
        results[output] = 1
      else:
        results[output] += 1

  final_string = ''
  mx = -1
  for i in results:
    if(results[i]>mx):
      mx = results[i]
      final_string = i
  print("Majority string found --> ",final_string)


#   # Saving results in csv -->
  filename = "records.csv"
  # read csv
  csvArray = []
  with open(filename, mode ='r')as file:   
    csvFile = csv.reader(file)
    for line in csvFile:
      if(len(line) !=0 ):
        csvArray.append(line)

  print("Last records --> ",csvArray)
  # search and update in csvArray for the final_string
  if(final_string != ""):
    flag = 0
    for i in csvArray:
      if(final_string == i[0]):
        flag = 1
        i[1] = str(int(i[1]) + 1)
        break
    if(flag==0):
      csvArray.append([final_string,1])

  print("Modified records --> ",csvArray)
  # write new csv
  with open(filename, 'w', newline='') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(csvArray)




image_frames_handler()

import pymongo # importing the python-mongoDB connector library

connection_url = "mongodb+srv://pilpiddu:s1FiE3EP6NYJXKP4@cluster0.khyvpbl.mongodb.net/?retryWrites=true&w=majority" # This is the general link for connecting to the local device.

client = pymongo.MongoClient(connection_url) 

database=client["OCR"] #Connecting to existing Sales database or creating a new Sales database
collection=database["records"] #connecting to the product collection in the Sales database
collection.drop()
import csv
with open("records.csv","r") as file:
    reader = csv.DictReader(file)
    data = list(reader)
    collection.insert_many(data)

