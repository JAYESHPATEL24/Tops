function Greeting(props) {
    return (
        <h1>Hello, {props.name}!</h1>
    );
}

function Entername() {
    return (
        <div>
            <Greeting name="Tony Stark" />
        </div>
    );
}

export default Entername;