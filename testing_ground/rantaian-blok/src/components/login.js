import React from 'react'
import { BrowserRouter as Router, Link, Switch, Route } from 'react-router-dom'
import './css/login.css'
import User from './user'

function Login() {
    return (
        <form>
            <h1>Log Masuk</h1>
            <p>Organisasi</p>
            <input className='organisasi'/>
            <p>Kata Laluan</p>
            <input className='kata-laluan'/>
            <Router>
                <Switch>
                    <Route exact path='/' component={Login} />
                    <Route path='/user' component={User} />
                    <p>
                        <Link to='/user' component={User}>
                            <button className='butang-masuk'>Masuklah.. apa lagi..</button>
                        </Link>
                    </p>
                </Switch>
            </Router>
        </form>
    );
}

export default Login