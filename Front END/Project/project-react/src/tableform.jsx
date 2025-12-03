import axios from 'axios';
import React, { useEffect, useState } from 'react';

function Tabledata() {
    const [card, setcard] = useState([]);

    useEffect(() => {
        fetchdata()
    }, []);

    const fetchdata = async () => {
        const res = await axios.get("https://fakestoreapi.com/products");
        console.log(res.data);
        setcard(res.data);
    };

    // return (
    //     <div ClassName ="container">
    //         <div className="row">
    //             {
    //                 card && card.map((card) => {
    //                     console.log(card);
    //                     return (
    //                     <div className="col-md-4">
    //                         <div className="card" style={{ width: "18rem" }}>
    //                             <img src={card.image} style={{ height: "300px" }} className="card-img-top" alt="..." />
    //                             <div className="card-body">
    //                                 <h5 className="card-title">{card.title}</h5>
    //                                 <p className="card-text">{card.description}</p>
    //                                 <a href="#" className="btn btn-primary">
    //                                     Price: {card.price}
    //                                 </a>
    //                             </div>
    //                         </div>
    //                     </div>
    //                 );
    //                 }
    //             )}
    //         </div>
    //     </div>
    // );

    return (
    <div className="container mt-4">
      <h2 className="mb-3">Product Table</h2>

      <table className="table table-bordered table-striped">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Image</th>
            <th>Title</th>
            <th>Description</th>
            <th>Price ($)</th>
          </tr>
        </thead>

        <tbody>
          {card &&
            card.map((card) => (
              <tr key={card.id}>
                <td>{card.id}</td>

                <td>
                  <img
                    src={card.image}
                    alt="product"
                    style={{ width: "60px", height: "60px", objectFit: "contain" }}
                  />
                </td>

                <td>{card.title}</td>
                <td style={{ maxWidth: "300px" }}>{card.description}</td>
                <td>{card.price}</td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );

}






export default Tabledata;