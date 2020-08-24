import React, { useState } from 'react'
import './css/login.css'
import User from './user'

function Login() {
    // const [page, setPage] = useState(() => {return (<Login />)})

    return (
        <form>
            <h1>Log Masuk</h1>
            <p>Organisasi
                <input className='organisasi'/>
            </p>
            <p>Kata Laluan
                <input className='kata-laluan'/></p>
            <p>
                <button className='butang-masuk' onClick={() => {return (<User />)}}>Masuklah.. apa lagi..</button>
            </p>
        </form>
    );
}

export default Login