import React from 'react'
import './css/login.css'
import User from './user'
import { BrowserRouter as Router, Route } from 'react-router-dom'

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
                <Router>
                    <button className='butang-masuk' onClick={() => {return (<Route path='/user' render={() => <User />}></Route>)}}>Masuklah.. apa lagi..</button>
                </Router>
            </p>
        </form>
    );
}

export default Login