import React, {useState, useEffect} from 'react'
import data_ from './data'
import './dashboard.css'
import axios from 'axios';

const Dashboard = () => {
    const [data, setData] = useState([]);
    useEffect( () => {
      const fetchData = async ()=>{
        const res = await axios.post('http://localhost:5000/getRecords',{});
        console.log(res.data);
        setData(res.data);
      }   
      fetchData();
      
    }, []);
    return (
        <>
            {/* <div className="dashboard-left">
                <h1>Dates</h1>
                
            </div> */}
            <div className='dashboard'>
                <table>
                    <th colSpan={3} className="main-heading">DashBoard</th>
                    <tbody >
                    <tr>
                        <th>id</th>
                        <th>Job</th>
                        <th>Count</th>
                    </tr>
                    {data.map((item) => {
                        return (
                            <tr key={item._id}>
                                <td>{item._id}</td>
                                <td>{item.Jobs}</td>
                                <td>{item.Count}</td>
                            </tr>
                        )
                    })}
                    </tbody>
                </table>
            </div>

        </>
    )
}

export default Dashboard