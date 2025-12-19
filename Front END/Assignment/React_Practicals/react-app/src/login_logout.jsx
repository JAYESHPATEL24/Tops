import { useState } from "react";

function UserloginStatus() {

    const [userstate, setUserstate] = useState(false);


    return (
        <div>
            <h2>User is {userstate ? "Logged In" : "Logged Out"}</h2>
            <button onClick={() => setUserstate(true)}>Login</button>
            <button onClick={() => setUserstate(false)}>Logout</button>
        </div>
    );
}

export default UserloginStatus;