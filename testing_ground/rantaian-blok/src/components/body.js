import React from 'react'
import { BrowserRouter as Router, Link, Route, Switch} from 'react-router-dom'
import Login from './login'
import User from './user'

function Body () {
    return (
        <Router>
            <Link to='/'></Link>
            <Link to='/user'></Link>
            <Switch>
                <Route path='/' component={Login} />
                <Route path='/user' component={User} />
            </Switch>
        </Router>
    );
}

export default Body