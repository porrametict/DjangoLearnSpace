import React, { Component } from 'react';
import {BrowserRouter as Router} from 'react-router-dom'
import { connect } from 'react-redux'
import CustomLayout from './containers/Layout';
import 'antd/dist/antd.css'; 
import * as actions from './store/actions/auth'

import BaseRouter from './routes'


class  App extends Component {


  componentDidMount () {    
    this.props.onTryAutoSignup();
  }
  render () {
    return (
      <div>
        <Router>
          <CustomLayout {...this.props}>
            <BaseRouter/>
          </CustomLayout>
        </Router>
        
      </div>
    );
  } 
  
}

const  mapStateTpProps = state => {
  return {
    isAuthenticated : state.token !== null 
  } 
}

const mapDispatchtoProps = dispatch => {
  return {
    onTryAutoSignup : () => dispatch(actions.authCheckState())
  }
}


export default  connect(mapStateTpProps,mapDispatchtoProps)(App) ;
