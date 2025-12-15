import { Component } from "react";

class Life_cycle extends Component {
    constructor() {
        super(); 
        this.state = { name :  "Jayesh" };  
        console.log("Constructor called");
    }

    componentDidMount() {
        console.log("phase 1");
    }

    componentDidUpdate() {
        console.log("phase 2 - updated");
    }

    componentWillUnmount() {
        console.log("phase 3 - unmounted");
    }

    render() {
        console.log("Render called");
        return (
            <> 
            <div><h1>{this.state.name}</h1></div>
            <button onClick={() => this.setState({ name: "Kumar" })}>Update Name</button>
            </>
        )
    }
}

export default Life_cycle;
