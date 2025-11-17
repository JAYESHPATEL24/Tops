export function Userdata({user}){
    return (
        <>
            <marquee><h1>User Intro</h1>
            </marquee>  
            <h2>Name: {user.name}</h2>
            <h2>Age: {user.age}</h2>
            <h2>City: {user.city}</h2>
        </>
    )
}


function Main_propexam(){
    let userinfo = {
        name: "Jayesh",
        age: 24,
        city: "Ahemdabad"
    };

    let userinfo2 = {
        name: "Mahrshi",
        age: 20,
        city: "Ahemdabad"
    };

    return(
        <>
        <Userdata user={userinfo} />
        <Userdata user={userinfo2}/>
        </>
    )
}

export default Main_propexam;
