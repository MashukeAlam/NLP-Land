import { useEffect, useRef, useState } from 'react'
import axios from 'axios'
import './App.css'
import NavBar from './NavBar'
import Summary from './Summary'
import Home from './Home'
import Sentiment from './Sentiment'
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  const [server, setServer] = useState(false)
  

  useEffect(() => {
    const fetch = async () => {
      const res = await axios.get('http://localhost:3333/running')
      console.log(res);
      setServer(res.data['server_running'])
    }

    fetch()
    
  }, []);

  
  return (
    <>

        <BrowserRouter>
          <NavBar />
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='summary' element={<Summary />} />
            <Route path='sentiment' element={<Sentiment />} />
          </Routes>
        </BrowserRouter>
      
        
      
    </>
  )
}

export default App
