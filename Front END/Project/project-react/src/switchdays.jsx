import React, { useReducer, useState } from "react";

const initialDay = "Initial Position";
const intial = 0;

export function reducer(state, action) {
    switch (action) {
        case 0:
            return "Initial Position";
        case 1:
            return "Monday";
        case 2:
            return "Tuesday";
        case 3:
            return "Wednesday";
        case 4:
            return "Thursday";
        case 5:
            return "Friday";
        case 6:
            return "Saturday";
        case 7:
            return "Sunday";
        default:
            return "Please Enter Number from 1 to 7.";
    }
}

function UseDays() {
    const [count, setCount] = useState(intial);
    const [day, dispatch] = useReducer(reducer, initialDay);

    return (
        <div>
            <h1>Day Number: {count}</h1>
            <h1>Day: {day}</h1>

            <button onClick={() => {const newCount = count + 1; setCount(newCount); dispatch(newCount);}}>Increment</button>
            <button onClick={() => {const newCount = count - 1; setCount(newCount); dispatch(newCount);}}>Decrement</button>
            <button onClick={() => {setCount(0); dispatch(0); }}>Reset</button>
        </div>
    );
}

export default UseDays;
