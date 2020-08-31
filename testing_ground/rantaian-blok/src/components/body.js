import React from 'react'
import { BrowserRouter as Router, Link, Route, Switch} from 'react-router-dom'
import Login from './login'
import User from './user'
import Start from './start'

function Body () {
    return (
        <Router>
            <Link to='/'></Link>
            <Link to='/login'></Link>
            <Link to='/user'></Link>
            <Switch>
                <Route path='/user' component={User} />
                <Route path='/login' component={Login}></Route>
                <Route path='/' component={Start} />
            </Switch>
        </Router>
    );
}

export default Body