import { useEffect, useRef, useState } from 'react'
import axios from 'axios'
const Summary = () => {
    const [summary, setSummary] = useState('');
  const text = useRef('');
  const handleClick = async () => {
    // console.log(text.current.value);
    const {data} = await axios.post('http://localhost:3333/summary', {text: text.current.value});
    setSummary(data);
  }
    return (
        <>
        <p htmlFor="inp">Input</p>
        <textarea ref={text} type="text" name="raw_text" id="inp" />
        <button onClick={handleClick}>Summarize</button>

        {summary !== '' ? <p>{summary}</p> : <></>}
        </>
        
    )
    
}

export default Summary;