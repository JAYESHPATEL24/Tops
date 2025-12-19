import { Component } from "react";

class Greet extends Component {
    constructor(){
        super();
        this.WelcomeMessage = "Welcome to React!" ;
    }

    render() {
        return (
            <div>
                <h1>{this.WelcomeMessage}</h1>
            </div>
        );
    }
}

export default Greet;
