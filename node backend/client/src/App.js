import './App.css';
// import Dashboard from './Dashboard';
// import data from './data';
import TableOCR from './Table';

function App() {
  return (
    <div className="App">
      <h1 style={{ textAlign: "center" }} >Results</h1>
      <div style={{ padding: "20px" }}>
        <TableOCR />
      </div>
      {/* <Dashboard /> */}
    </div>
  );
}

export default App;
