import React from 'react';
import './App.css';
import Header from './components/header'
import Footer from './components/footer'
import Login from './components/login'

function App() {
  return (
    <div className="App">
      <Header />
      <body>
        <Login />
      </body>
      <Footer />
    </div>
  );
}

export default App;
