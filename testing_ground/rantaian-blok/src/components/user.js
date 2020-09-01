import React from 'react'
import './css/user.css'
import UserButton from './user-button'
import { useInput } from './hooks/useInput'

function User(props) {
    const { value: pengirim, bind:bindPengirim, reset:resetPengirim } = useInput('')
    const { value: penerima, bind:bindPenerima, reset:resetPenerima } = useInput('')
    const { value: data, bind:bindData, reset:resetData } = useInput('')
    const handleSubmit = (evt) => {
        evt.preventDefault()
        alert(`Menghantar ${data} daripada ${pengirim} kepada ${penerima}`)
        resetPengirim()
        resetPenerima()
        resetData()
    }
    return(
        <form className='user-form' onSubmit={handleSubmit}>
            <h1 className='h1-form'>Hantar data terkini</h1>
            <p>Pengirim
                <input className='pengirim-form' type='text' {...bindPengirim}/>
            </p>
            <p>Penerima
                <input className='penerima-form' type='text' {...bindPenerima}/>
            </p>
            <p>Data
                <input className='data-input' type='text' {...bindData}/>
            </p>
            <p>
                <UserButton />
            </p>
        </form>
    );
}

export default User