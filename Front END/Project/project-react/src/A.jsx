import React, { useState }  from "react";
import B from "./B.jsx";

function A() {
    const [name, setname] = useState("Jayesh Patel");

    return (
        <div>
            <h1>Hello this is Component A</h1>
            <B name={name} setname={setname}/>
        </div>
    );
}

export default A;