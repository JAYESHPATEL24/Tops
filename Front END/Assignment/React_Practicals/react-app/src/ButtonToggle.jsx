import { useState } from "react";

function ButtonToggle() {

    const [text, setText] = useState("Not Clicked");

    return (
        <div>
            <button onClick={()=>{setText(text === "Not Clicked" ? "Clicked" : "Not Clicked")}}>
                click ME 
            </button>
            <h2>{text}</h2>
        </div>
    );
}   

export default ButtonToggle;