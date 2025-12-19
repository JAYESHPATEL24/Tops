function Example() {
    const Headername = "Welcome to JSX";
    const Description = "JSX (JavaScript XML) is a syntax extension for JavaScript used in React to make writing UI components easier and more readable. It allows you to write HTML-like code directly inside JavaScript, which React then compiles into standard JavaScript function calls. This means you can mix markup and logic in the same file, making components more intuitive to build.";

    return (
        <div>
            <h1>Welcome to JSX</h1>
            <p>{Description}</p>
        </div>
    );
}


export default Example;
