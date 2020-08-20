import React from 'react';
import './App.css';
import Header from './components/header'
import Footer from './components/footer'

function App() {
  return (
    <div className="App">
      <Header />
      <body>
        <a className="App-body" href="https://twistcode.com" target="_blank" rel="noopener noreferrer"> Tekan untuk mula</a>
      </body>
      <Footer />
    </div>
  );
}

export default App;
