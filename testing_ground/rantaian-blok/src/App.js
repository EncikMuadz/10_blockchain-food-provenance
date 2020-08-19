import React from 'react';
import RantaianBlokLogo from './blockchain_logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1 className="App-header-one">Rantaian</h1>
        <img src={RantaianBlokLogo} className="App-logo" alt="rantaianbloklogo" />
        <h1 className="App-header-two"> Blok</h1>
      </header>
      <body>
        <a className="App-body" href="https://reactjs.org" target="_blank" rel="noopener noreferrer"> Tekan untuk mula</a>
      </body>
    </div>
  );
}

export default App;
