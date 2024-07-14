import axios from "axios";
import { useEffect, useState } from "react";

export const App = () => {

  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get(`http://localhost:8000/api`)
      .then((res) => {
        setData(res.data)
      })
      .catch((err) => console.log(err))
  }, [])

  return (
    <div className="App">
      {data && data.map((datum, index) => {
        return (
          <ul className="card">
            <li>{datum.title}</li>
            <li>{datum.description}</li>
            <li>{datum.status}</li>
          </ul>
        )
      })}
    </div>
  );
}

