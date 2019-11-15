import React from 'react';
import axios from 'axios'
import {connect} from 'react-redux'
import {Card,Button} from 'antd'
import CustomForm from  '../components/Form'

class ArticleDetail extends React.Component {


    state = {
        article : {}
    }


    componentWillReceiveProps (newProps) {
        console.log(newProps)
        if(newProps.token){
            axios.defaults.headers = {
                "Content-Type" : "application/json",
                Authorization : newProps.token
            }
            const articleID = this.props.match.params.articleID
            axios.get(`http://127.0.0.1:8000/api/${articleID}/`)
            .then (res => {
                this.setState({
                    article : res.data
                });

            })
        }
       
    }

  
    handleDelete =  (event) => {
        if(this.props.token !== null) {
            axios.defaults.headers = {
                "Content-Type" : "application/json",
                Authorization : this.props.token
            }
            const articleID = this.props.match.params.articleID
            axios.delete(`http://127.0.0.1:8000/api/${articleID}/`)
            this.props.history.push('/');
            this.forceUpdate();
        }else {
            //show some message
        }

    }
    render () {
        return (
            <div>
            <Card title={this.state.article.title}>
                <p>{this.state.article.content}</p>
            </Card>
            <CustomForm btnText="Update" requestType="put" articleID={this.props.match.params.articleID}/>
            <form onSubmit={this.handleDelete}>
                <Button type="danger" htmlType="submit">Delete</Button>
            </form>
            </div>
        )
    }
} 
const  mapStateTpProps = state => {
    return {
      token : state.token 
    } 
}

export default connect(mapStateTpProps)(ArticleDetail);