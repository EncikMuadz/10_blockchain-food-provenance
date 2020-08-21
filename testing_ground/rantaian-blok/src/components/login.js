import React from 'react'
import './css/login.css'

function Login() {
    return (
        <form>
            <h1>Log Masuk</h1>
            <p>Organisasi</p>
            <input className='organisasi'/>
            <p>Kata Laluan</p>
            <input className='kata-laluan'/>
            <p>
                <button className='butang-masuk'>Masuklah.. apa lagi..</button>
            </p>
        </form>
    );
}

export default Login