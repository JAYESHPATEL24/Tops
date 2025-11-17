import { useState } from "react";

function Toggle() {
  const [toggle, settoggle] = useState(false);
    return (
        <>
            {
                toggle ? <h2>The Toggle is ON</h2> : null
            }
            <button onClick={() => settoggle(!toggle)}>{toggle ? "Hide" : "Show"}</button>
        </>

    )
}

export default Toggle;

export function Increment() {
    const [count, setcount] = useState(0);
    return (
        <>
        <h2>Count: {count}</h2>
        {
            count==1 ? <h1>count is 1</h1> : 
            count==2 ? <h1>count is 2</h1> : 
            count==3 ? <h1>count is 3</h1> :
            <h1>count is more than 3</h1>
        }
            
            <button onClick={() => setcount(count + 1)}>Increment</button>
        </>
    )
}

import Props from "./Propesexample";

export function Reactcomponent() {
    return (
        <>
        <Props color="Blue" height="100cm"/>
        </>
    )
}
