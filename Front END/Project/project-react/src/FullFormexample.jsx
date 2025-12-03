import { useState } from "react";
import "./form.css";


function FullFormexample() {
    const [formData, setFormData] = useState({
        name: "",
        email: "",
        password: "",
        city: "",
        gender: "Male",
        technologies: []
    });     

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        if (type === "checkbox") {
            let newTechnologies = [...formData.technologies];
            if (checked) {
                newTechnologies= [...newTechnologies, value];
            } else {
                newTechnologies = newTechnologies.filter((item) => item !== value);
            }               
            setFormData({ ...formData, technologies: newTechnologies });
        } else {
            setFormData({ ...formData, [name]: value });
        }   
    }

    const [message, setMessage] = useState("");

    const handleSubmit = (e) => {
        // setMessage("Form Submitted Successfully!"); .
        alert("Form Submitted Successfully!");
    };


    const validateEmail = (e) => {
        const email = e.target.value;
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        check =  re.test(String(email).toLowerCase());
        if (check){ 
            return True;
        }
        else {
            getelementbyClassName("error").innerText = "Invalid Email Address";
            return False;
        }
    }

    return (
        <div className="form-container">
            <form onSubmit={handleSubmit}>
                <label>Name:</label>
                <input type="text" name="name" value={formData.name} onChange={handleChange} /> 
                <label>Email:</label>

                <input type="email" name="email" value={formData.email} onChange={handleChange} onKeyDown={validateEmail} />
                <p className="error"></p>

                <label>Password:</label>
                <input type="password" name="password" value={formData.password} onChange={handleChange} />
                <label>City:</label>
                <select name="city" value={formData.city} onChange={handleChange}>
                    <option value="" disabled>Select City</option>
                    <option value="Ahemdabad">Ahemdabad</option>
                    <option value="Surat">Surat</option>
                    <option value="Vadodara">Vadodara</option>
                </select>

                <br/>
                
                <div>
                    <h3>Technologies:</h3>
                    <input type="checkbox" name="technologies" value="Java" onChange={handleChange} />
                    <label>Java</label>
                    <input type="checkbox" name="technologies" value="Python" onChange={handleChange} />
                    <label>Python</label>
                    <input type="checkbox" name="technologies" value="React" onChange={handleChange} />
                    <label>React</label>
                </div>
                <br/>
                <div>
                    <h3>Gender:</h3>
                    <input type="radio" name="gender" value="Male" onChange={handleChange} checked={formData.gender === "Male"} />
                    <label>Male</label>
                    <input type="radio" name="gender" value="Female" onChange={handleChange} checked={formData.gender ===  "Female"} />
                    <label>Female</label>
                </div>
                <button type="submit">Submit</button>

                {/* <br/>
                <h2>Your Input:</h2>
                <p>Name: {formData.name}</p>
                <p>Email: {formData.email}</p>
                <p>Password: {formData.password}</p>
                <p>City: {formData.city}</p>
                <p>Technologies: {formData.technologies.join(", ")}</p>
                <p>Gender: {formData.gender}</p> */}
            </form>
            <p className="success-message">{message}</p>
        </div>
    );
}

export default FullFormexample;