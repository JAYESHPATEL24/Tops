import { useState } from "react";

function SimpleForm() {
    const [userdata, setUserdata] = useState({
        name: "",
        email: "",
        password: ""
    });

    return (
        <div>
            <h2>Enter Your Data : </h2>
            <form>
                <input type="text" placeholder="Enter Name" value={userdata.name} onChange={(e) => setUserdata({...userdata, name: e.target.value})} />
                <br /><br />
                <input type="email" placeholder="Enter Email" value={userdata.email} onChange={(e) => setUserdata({...userdata, email: e.target.value})} /> 
                <br /><br />
                <input type="password" placeholder="Enter Password" value={userdata.password} onChange={(e) => setUserdata({...userdata, password: e.target.value})} />
                <br /><br />
                <button type="submit">Submit</button>
            </form>
            <h3>Your Name is : {userdata.name}</h3>
            <h3>Your Email is : {userdata.email}</h3>
            <h3>Your Password is : {userdata.password}</h3>
        </div>
    );
}   

export default SimpleForm;