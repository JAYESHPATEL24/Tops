function abc(){
    return 10+50
}

function alert_fun(){
    alert("Ghar chala jaaaaa")
}

function Imagesetup() {

   let imge = "https://images.hdqwalls.com/download/i-am-iron-man-4k-ky-3840x2400.jpg" 
    return (
        <>
        <h1>{abc()}</h1>
        <img src={imge} height="300px"/>
        <br/>
        <button onClick={alert_fun}>alert</button>
        </>
    )
    }

export default Imagesetup
