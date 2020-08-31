import React from 'react'
import './css/login.css'
import LoginButton from './login-button'
import { BrowserRouter as Router, Route, Link, Switch} from 'react-router-dom'
import User from './user.js'

function Login() {
    return (
        <Router>
            <form>
                <h1>Log Masuk</h1>
                <p>Organisasi
                    <input className='organisasi'/>
                </p>
                <p>Kata Laluan
                    <input className='kata-laluan'/></p>
                <p>
                    <Link to='/user'>
                        <LoginButton />
                    </Link>
                </p>
                <Switch>
                    <Route path='/user' component={User} />
                </Switch>
            </form>
        </Router>
    );
}

export default Login