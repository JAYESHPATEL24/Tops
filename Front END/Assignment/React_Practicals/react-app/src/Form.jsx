import {useState} from 'react';

function Form() {
    const [userdata, setUserdata] = useState({
        username: '',
        email: '',
        password: ''
    });

    const [data, setData] = useState('');

    function handleSubmit(e) {
        e.preventDefault();
        const registeredData = `Username: ${userdata.username}, Email: ${userdata.email}, Password: ${userdata.password}`;
        setData(registeredData);
    }

    return (
        <div>
            <h2>Registration Form</h2>
            <form>
                <div>
                    <label>Username:</label>
                    <input type='text' value={userdata.username} />
                </div>
                <div>
                    <label>Email:</label>
                    <input type='email' value={userdata.email} />
                </div>
                <div>
                    <label>Password:</label>
                    <input type='password' value={userdata.password} />
                </div>
                <button type='submit' onClick={handleSubmit}>Register</button>
            </form>
        <div> 
            <h3>{data}</h3>
        </div>
        </div>
    );
}

export default Form;