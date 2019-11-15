import React from 'react';
import axios from 'axios'
import Articles from '../components/Article'
import {connect} from 'react-redux'
import CustomForm from  '../components/Form'

class ArticleList extends React.Component {

    state = {
        articles : []
    }

    componentWillReceiveProps (newProps) {
        console.log(newProps.token,"newProps")
        if(newProps.token){
            axios.defaults.headers = {
                "Content-Type" : "application/json",
                Authorization : newProps.token
            }
                axios.get('http://127.0.0.1:8000/api/')
                .then (res => {
                    this.setState({
                        articles : res.data
                    });
    
                })
        }
    }
    render () {
        return (

            <div>
                <Articles data={this.state.articles}/>
                <br/>
                <h2>Create Article</h2>
                <CustomForm btnText="Create" requestType="post" articleID={null}/>
            </div>
        )
    }
} 


const  mapStateTpProps = state => {
    return {
      token : state.token 
    } 
}

export default connect(mapStateTpProps)(ArticleList);