import logo from "./logo.svg";
import "./App.css";
import { useState } from "react";
import axios from "axios";
import DataTable from "./DataTable";

function App() {
  const [question, setQuestion] = useState("");
  const [data, setData] = useState([]);

  const updateQuestion = (e) => setQuestion(e.target.value);
  const getData = () => {
    axios.post("/find_data", { data: question }).then((res) => {
      setData(res.data);
    });
  };

  return (
    <div className="App">
      <div className="container-question">
        <input onChange={updateQuestion} />
        <button onClick={getData}>Search</button>
      </div>
      <div className="container">
        <DataTable data={data} />
      </div>
    </div>
  );
}

export default App;
