import { useState } from "react";

function Calculater() {
    const [name, setName] = useState("");
    const [greet, setGreet] = useState("");
    const [num1, setNum1] = useState(0);
    const [num2, setNum2] = useState(0);
    const [result, setResult] = useState(0);

    const handleAddition = () => {
        setResult(Number(num1) + Number(num2));
    }
    const handleSubtraction = () => {
        setResult((num1) - (num2));
    }
    const handleMultiplication = () => {
        setResult((num1) * (num2));
    }   
    const handleDivision = () => {
        if (num2 !== 0) {
            setResult((num1) / (num2));
        } else {
            setResult("Error: Division by zero");
        }
    }

    const handlenameChange = () => {
        setGreet("Hello, " + name + "!");
    }

    return (
        <div>
            <h2>Enter Your name : </h2>
            <input type="text" value ={name} onChange={(e) => setName(e.target.value)} />
            <input type="button" onClick={handlenameChange} value="submit"/>
            <h3>{greet}</h3>

            <br />
            <br />
            <br />

            <h2>Simple Calculater</h2>
            <br />
            <input type="number" value={num1} onChange={(e) => setNum1(e.target.value)} />

            <input type="number" value={num2} onChange={(e) => setNum2(e.target.value)} />
            <br />
            <br />
            <button onClick={handleAddition}>+</button>
            <button onClick={handleSubtraction}>-</button>
            <button onClick={handleMultiplication}>*</button>
            <button onClick={handleDivision}>/</button>
            <br />
            <br />
            <h3>Result: {result}</h3>
        </div>
    );
}

export default Calculater;