import { useState } from 'react';

function CheckboxExample() {
    const [check, setCheck] = useState([]);
    const [city, setCity] = useState("");
    const [gender, setGender] = useState("Male");

    const handleChange = (e) => {
        if (e.target.checked) {
            setCheck([...check, e.target.value]);
        } 
        else {
            setCheck(check.filter((item) => item !== e.target.value));
        }
    }

    const handleGenderChange = (e) => {
        setGender(e.target.value);
    }

    return (

        <div>
            <h1>List example</h1>
            <br/>
        <div>
            <select onChange={(e)=>setCity(e.target.value)}>
                <option value="" disabled>Select City</option>
                <option value="Ahemdabad">Ahemdabad</option>
                <option value="Surat">Surat</option>
                <option value="Vadodara">Vadodara</option>
            </select>   
            <br/>
            <br/>
            <h2>You have selected: {city}</h2>
        </div> 
            <br/>
            <h1>Checkbox Example</h1>
            <br/>
            <div>
                <input type="checkbox" value="Java" id="java" onChange={handleChange}/>
                <label htmlFor='java'>Java</label>
                <input type="checkbox" value="Python" id="python" onChange={handleChange} />
                <label htmlFor='python'>Python</label>
                <input type="checkbox" value="React" id="react" onChange={handleChange} />
                <label htmlFor='react'>React</label>
            </div>
            <div>
                <br/>
                <h2>Selected Technologies:</h2>
                <h2>{check}</h2>
            </div>
            <br/>
            <h1>Gender</h1>
            <br/>
            <div>
                <input type="radio" name="gender" value="Male" id="male" onChange={handleGenderChange} checked={gender === "Male"}/>
                <label htmlFor='male'>Male</label>
                <input type="radio" name="gender" value="Female" id="female" onChange={handleGenderChange}/>
                <label htmlFor='female'>Female</label>
            </div>
            <br/>
            <h2>You have selected: {gender}</h2>
        </div>

    );
}

export default CheckboxExample;