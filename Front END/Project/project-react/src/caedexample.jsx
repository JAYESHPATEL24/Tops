import { useState, useEffect } from "react";

function Card() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts/1")
        .then((res) => res.json())
        .then((data) => setPosts(data))
        .catch((err) => console.log(err));
    });

  return (
    <>
      <div className="card text-white bg-success mb-3" style={{ maxWidth: "18rem" }}>
        <div className="card-header">{posts.userId}</div>
        <div className="card-body">
          <h5 className="card-title">{posts.title}</h5>
          <p className="card-text">
            {posts.body}
          </p>
        </div>
      </div>
    </>
  );
}

export default Card;
