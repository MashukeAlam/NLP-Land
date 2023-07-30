import { useEffect, useRef, useState } from 'react'
import axios from 'axios'
const Sentiment = () => {
    const [summary, setSummary] = useState('');
    const [pos, setPos] = useState(null)
    const [neg, setNeg] = useState(null)
    const [neu, setNeu] = useState(null)
  const text = useRef('');
  const handleClick = async () => {
    // console.log(text.current.value);
    const {data} = await axios.post('http://localhost:3333/sentiment', {text: text.current.value});
    setPos(data['pos']);
    setNeg(data['neg']);
    setNeu(data['neu']);
  }
    return (
        <>
        <p htmlFor="inp">Input</p>
        <textarea ref={text} type="text" name="raw_text" id="inp" />
        <button onClick={handleClick}>Detect Sentiment</button>

        {pos !== null ? <p>Positive: {pos * 100}%</p>:<></>}
        {neg !== null ? <p>Negative: {neg * 100}%</p>:<></>}
        {neu !== null ? <p>Neutral: {neu * 100}%</p>:<></>}
        </>
        
    )
    
}

export default Sentiment;