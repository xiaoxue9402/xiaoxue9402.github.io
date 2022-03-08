import React, { useState } from "react";
import { ReactReader } from "react-reader";
import axios from "axios";
import './App.css';

const App = () => {
  const [location, setLocation] = useState(null)
  const locationChanged = (epubcifi) => {
    setLocation(epubcifi)
  }
  return (
    <div>
      <ReactReader
        location={location}
        locationChanged={locationChanged}
        url={axios.get('https://github.com/xiaoxue9402/xiaoxue9402.github.io/blob/main/Neverwhere%20by%20Neil%20Gaiman.epub')}
      />
    </div>
  )
}

export default App
