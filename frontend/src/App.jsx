import Welcome from '../src/components/welcome.jsx';
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <h1>Моё React-приложение</h1>
      <Welcome name="друг" />
    </div>
  );
}

export default App
