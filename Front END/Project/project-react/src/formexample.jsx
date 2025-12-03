import React, { useState } from "react";
import "./form.css";

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    check = re.test(String(email).toLowerCase());
    if (check) {
        return True;
    }
    else {
        getelementbyClassName("error").innerText = "Invalid Email Address";
        return False;
    }

}

function Form() {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [mobile, setMobile] = useState("");
    const [password, setPassword] = useState("");

    return (
        <div className="form-container">
            <form>
                <label>Name:</label>
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />

                <label>Email:</label>
                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)}/>
                <p className="error"></p>
            

                <label>Mobile:</label>
                <input type="number" value={mobile} onChange={(e) => setMobile(e.target.value)} />

                <label>Password:</label>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />

                <button type="submit">Submit</button>

                <br/>
                <h2>Your Input:</h2>
                <p>Name: {name}</p>
                <p>Email: {email}</p>
                <p>Mobile: {mobile}</p>
                <p>Password: {password}</p>
            </form>
        </div>
    );
}

export default Form;
