import React from "react";
import C from "./C.jsx";

function B({name, setname}) {

    return (
        <div>
            <h1>Hello this is Component B</h1>

            <h1>hello this name : - {name} </h1>
            <button onClick={ () => setname("Tony Stark") }> Change Name</button>

            <C name={name} setname={setname}/>
        </div>
    );
}

export default B;