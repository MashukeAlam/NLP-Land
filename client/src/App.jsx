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
    </>
  )
}

export default App
