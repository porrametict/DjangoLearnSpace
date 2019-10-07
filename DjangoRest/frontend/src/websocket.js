class WebSocketService {

    static instance = null ;
    callbacks = {}


    static getInstance () {
        if(!WebSocketService.instance) {
            WebSocketService.instance = new WebSocketService();
        }

        return WebSocketService.instance;
    }

    constructor () {
        this.socketRef = null ;
    }

    connect () {
        const path = 'ws://127.0.0.1:8000/ws/chat/cat/';
        this.socketRef = new WebSocket(path);
        this.socketRef.onopen = () => {
            console.log('websocket open');
        }
        this.socketNewMessage(JSON.stringify({
            command : 'fetch_messages'
        }))
        this.socketRef.onmessage = e => {
            this.socketNewMessage(e.data)
        }

        this.socketRef.onerror= e => {
            console.log(e.meeage)
        }

        this.socketRef.onclose = () => {
            console.log('websocket is closed');
            this.connect();
        }
    }


    socketNewMessage (data) {
        const parseData = JSON.parse(data);
        const command = parseData.command;
        if (Object.keys(this.callbacks).length === 0 ) {
            return;
        }
        if(command === 'messages') {
            this.callbacks[command](parseData.messages);
        }

        if(command === 'new_message') {
            this.callbacks[command](parseData.message);
        }
    }

    fetchMessages(username){
        this.sendMessage({
            command : 'fetch_messages',
            username :username
        });

    }

    newChatMessages(message){
        this.sendMessage({
            command : 'new_message',
            from : message.from,
            message :message.content
        });

    }

    addCallbacks (messagesCallback,newChatMessageCallback) {
        this.callbacks['messages'] = messagesCallback;
        this.callbacks['new_message'] = newChatMessageCallback;
    }

    sendMessage(data) {
        try {
            this.socketRef.send(JSON.stringify({ ...data }))

        }catch (err){
            console.log(err.message)
        }
    }

    state(){
        return this.socketRef.readyState;
    }

    waitForSocketConnention (callback) {
        const socket=this.socketRef;
        const  recursion = this.waitForSocketConnention;
        setTimeout (
            function () {
                    if(socket.readyState === 1 ){
                        console.log('connection is secure')
                        if(callback != null) {
                            callback();
                        }
                        return ; 
                    }else {
                        console.log('waiting for connention ...')
                        recursion(callback);
                    }
            },1
        );
    }
}

const WebSocketInstance  = WebSocketService.getInstance();

export default WebSocketInstance;