import React  from "react";
import D from "./D.jsx";

function C({name, setname}) {
    return (
        <div>
            <h1>Hello this is Component C</h1>
            <D name={name} setname={setname}/>
        </div>
    );
}

export default C;