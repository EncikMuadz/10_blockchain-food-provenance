import React from 'react'
import './css/login.css'
import User from './user'

function Login() {
    return (
        <form>
            <h1>Log Masuk</h1>
            <p>Organisasi
                <input className='organisasi'/>
            </p>
            <p>Kata Laluan
                <input className='kata-laluan'/></p>
            <p>
                <button className='butang-masuk'>Masuklah.. apa lagi..</button>
            </p>
        </form>
    );
}

export default Login