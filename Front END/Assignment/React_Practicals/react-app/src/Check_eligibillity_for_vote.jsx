import { useState } from "react";

function Checkeligibillityforvote() {
    const [age, setAge] = useState(0);
    const [msg, setMsg] = useState("");

    return (
        <div>
            <h2>Check Eligibillity for Vote</h2>
            <input type="number" placeholder="Enter Your Age" value={age} onChange={(e) => setAge(e.target.value)} />
            <button onClick={() => { age >= 18 ? setMsg("You are Eligible for Vote") : setMsg("You are Not Eligible for Vote") }}>Check Eligibility</button>
            <h3>{msg}</h3>
        </div>
    );
}

export default Checkeligibillityforvote;