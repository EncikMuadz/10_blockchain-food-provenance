import React from 'react'
import './css/login.css'
import LoginButton from './login-button'

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
                <LoginButton />
            </p>
        </form>
    );
}

export default Login