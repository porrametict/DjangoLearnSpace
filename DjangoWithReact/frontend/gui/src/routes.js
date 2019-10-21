import React from 'react';
import {Route} from 'react-router-dom'

import ArticleList from './containers/ArticleListView'
import ArticleDetail from './containers/ArticleDetailView'
import Login from './containers/Login'
import Signup from './containers/Signup'
const BaseRouter = () => (
    <div>
        <Route exact path='/' component={ArticleList}></Route>
        <Route exact path='/article/:articleID' component={ArticleDetail}></Route>
        <Route exact path='/login/' component={Login}></Route>
        <Route exact path='/signup/' component={Signup}></Route>
    </div>
)
export default BaseRouter;