import './usercard.css';

function UserCard(props) {
    return (
        <div className="user-card">
            <h2>{props.name}</h2>
            <p>Age: {props.age}</p>
            <p>Location: {props.location}</p>
        </div>
    );  
}

function Userdata() {
    return (
        <div>
            <UserCard name="Jayesh" age={30} location="Ahemdabad" />
            <UserCard name="Jay" age={25} location="Surat" />
            <UserCard name="Jignesh" age={35} location="Vadodara" />
        </div>
    );
}

export default Userdata;