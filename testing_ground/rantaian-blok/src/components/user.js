import React from 'react'
import './css/user.css'
import UserButton from './user-button'

function User() {
    return(
        <form className='user-form'>
            <h1 className='h1-form'>Hantar data terkini</h1>
            <p>Pengirim
                <input className='pengirim-form'/>
            </p>
            <p>Penerima
                <input className='penerima-form'/>
            </p>
            <p>Data
                <input className='data-input'/>
            </p>
            <p>
                <UserButton />
            </p>
        </form>
    );
}

export default User