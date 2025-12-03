import React, { useReducer } from "react";

const initial = 0;

export function reducer(state, action) {
    switch (action) {
        case "INCREMENT":
            return state + 1;
            break;
        case "DECREMENT":
            return state - 1;
            break;
        case "RESET":
            return initial;
            break;  
        default:
            return state;
    }   
}

function UseRed() {
    const [count, dispatch] = useReducer(reducer, initial);
    return (
        <div>
            <h1>Hello reducer logic</h1>
            <h1>Count : {count}</h1>
            <button onClick={() => dispatch("INCREMENT")}>Increment</button>
            <button onClick={() => dispatch("DECREMENT")}>Decrement</button>
            <button onClick={() => dispatch("RESET")}>Reset</button>
        </div>
    );
}

export default UseRed;
