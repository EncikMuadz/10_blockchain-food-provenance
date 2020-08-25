import React from 'react'
import './css/login.css'
import User from './user'
import { useHistory } from 'react-router-dom'

function Login() {
    const history = useHistory()
    const routeToUser = () => history.push({User})
    return (
        <form>
            <h1>Log Masuk</h1>
            <p>Organisasi
                <input className='organisasi'/>
            </p>
            <p>Kata Laluan
                <input className='kata-laluan'/></p>
            <p>
                <button className='butang-masuk' onClick={routeToUser}>Masuklah.. apa lagi..</button>
            </p>
        </form>
    );
}

export default Login