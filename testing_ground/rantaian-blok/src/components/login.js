import React from 'react'
import { Switch, Route, Link } from 'react-router'
import './css/login.css'
import User from 'user'

function Login() {
    return (
        <form>
            <h1>Log Masuk</h1>
            <p>Organisasi</p>
            <input className='organisasi'/>
            <p>Kata Laluan</p>
            <input className='kata-laluan'/>
            <p>
                <button className='butang-masuk' onClick>Masuklah.. apa lagi..</button>
            </p>
        </form>
    );
}

export default Login