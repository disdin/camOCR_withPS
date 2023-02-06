import os
import cv2





from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.

def runScriptPy(path_of_image):
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
