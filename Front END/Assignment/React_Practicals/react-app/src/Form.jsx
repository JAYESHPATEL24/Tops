import {useState} from 'react';

function Form() {
    const [userdata, setUserdata] = useState({
        username: '',
        email: '',
        password: ''
    });

    const [data, setData] = useState('');

    const [errormsg, setErrormsg] = useState('');

    function handleSubmit(e) {
        if (!validateEmail(userdata.email)) {
            e.preventDefault();
            return;
        }
        else
        {            
            setErrormsg('');
            e.preventDefault();
            const registeredData = `Username: ${userdata.username}, Email: ${userdata.email}, Password: ${userdata.password}`;
            setData(registeredData);
        }
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!email) 
            return false;
        else if (!re.test(email))
        {
            setErrormsg('Invalid email format');
            return false;
        }
        else
            return true;
    }

    return (
        <div>
            <h2>Registration Form</h2>
            <form>
                <div>
                    <label>Username:</label>
                    <input type='text' value={userdata.username} onChange={(e)=>setUserdata({...userdata, username: e.target.value})}/>
                </div>
                <div>
                    <label>Email:</label>
                    <input type='email' value={userdata.email} onChange={(e)=>setUserdata({...userdata, email: e.target.value})} />
                    {errormsg && <p style={{color: 'red'}}>{errormsg}</p>}
                </div>
                <div>
                    <label>Password:</label>
                    <input type='password' value={userdata.password} onChange={(e)=>setUserdata({...userdata, password: e.target.value})}  />
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


