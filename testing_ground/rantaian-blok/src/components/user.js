import React from 'react'
import './css/user.css'

function User() {
    return(
        <form className='user-form'>
            <h1>Gunalah</h1>
            <p>Data</p>
            <input className='data-input'/>
            <p>Penerima</p>
            <input className='penerima-form'/>
        </form>
    );
}

export default User