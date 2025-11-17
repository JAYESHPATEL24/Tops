import React, {Component} from "react";

class Class_props extends Component {
    constructor(props) {
        super(props);
        this.data = props;
    }
    render() {
        return (
            <>  
            <div><h1>{this.data.color}</h1></div>
            <div><h1>{this.data.height}</h1></div>
            </>
        )
    }
}

export default Class_props;

export function Main_propexam_class(){
    return(
        <>
        <Class_props color="Red" height="150cm"/>
        </>
    )
}


