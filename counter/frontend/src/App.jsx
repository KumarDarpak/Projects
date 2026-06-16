import { use, useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  const loadCount = async () => {
    const res = await axios.get("http://localhost:5000/count");

    setCount(res.data.count);
  };

  useEffect(() => {
    loadCount();
  }, []);

  const increment = async () => {
    const res = await axios.post("http://localhost:5000/increment");

    setCount(res.data.count);
  };

  const decrement = async () => {
    const res = await axios.post("http://localhost:5000/decrement");

    setCount(res.data.count);
  };

  const reset = async () => {
    const res = await axios.post("http://localhost:5000/reset");

    setCount(res.data.count);
  };
}
