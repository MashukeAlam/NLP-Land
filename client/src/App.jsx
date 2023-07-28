import { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  useEffect(async () => {
    const res = await axios.get('http://localhost:3333/running')
    console.log(res.data);
  }, [])
  return (
    <>
      <p>hello</p>
      <form action="http://localhost:3333/summary" method="post">
        <input type="text" name="raw_text" id="" />
      </form>
    </>
  )
}

export default App
