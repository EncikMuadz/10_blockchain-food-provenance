import React from 'react'
import './css/login.css'
import LoginButton from './login-button'
import { useInput } from './hooks/useInput'

function Login(props) {
    const { value:organisasi, bind:bindOrganisasi, reset:resetOrganisasi } = useInput('')
    const { value:katalaluan, bind:bindKataLaluan, reset:resetKataLaluan } = useInput('')
    
    const handleSubmit = (evt) => {
        evt.preventDefault()
        alert(`Dalam proses log masuk ${organisasi} ${katalaluan}`)
        resetOrganisasi()
        resetKataLaluan()
    }
    return (
        <form onSubmit={handleSubmit}>
            <h1>Log Masuk</h1>
            <p>Organisasi
                <input className='organisasi' type='text' {...bindOrganisasi}/>
            </p>
            <p>Kata Laluan
                <input className='kata-laluan' type='text' {...bindKataLaluan}/></p>
            <p>
                <LoginButton />
            </p>
        </form>
    );
}

export default Login