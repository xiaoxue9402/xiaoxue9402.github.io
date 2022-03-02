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
        url={axios.get('/')}
      />
    </div>
  )
}

export default App
