import React from 'react'
import User from './user.js'
import './css/butang-masuk.css'
import { useHistory } from 'react-router-dom'

function LoginButton() {
    const history = useHistory()
    const routeToUser = () => history.push({User})
    return (
        <div>
            <button className='butang-masuk' onClick={routeToUser}>Masuklah.. apa lagi..</button>
        </div>
    );
}

export default LoginButton