import React from 'react';
import './css/header.css'
import RantaianBlokLogo from './img/blockchain_logo.svg'

function Header() {
    return (
    <div className="Header">
        <header className="header">
          <h1 className="h1-one">Rantaian</h1>
          <img src={RantaianBlokLogo} className="logo" alt="rantaianbloklogo" />
          <h1 className="h1-two">Blok</h1>
        </header>
    </div>
    );
}

export default Header