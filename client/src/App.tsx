import axios from 'axios'
import { useEffect } from 'react';

const api = axios.create({
  baseURL: 'http://localhost:8000',
});

function App() {
  useEffect(() => {
    api.get('/').then((res) => {
      console.log(res.data)
    });
  });
  
  return (
    <>
    <h1>Test</h1>
    </>
  )
}

export default App
