import { BrowserRouter, Link, Route, Routes } from "react-router-dom";

function Routing() {
  return (
    <BrowserRouter>

    <Link to="/">Home</Link>
    <Link to="/about">About</Link>
    <Link to="/contact">Contact</Link>
    <Link to="/service">Service</Link>

      <Routes>
        <Route path="/" element={<h1>This is Home Page</h1>} />
        <Route path="/about" element={<h1>This is About Page</h1>} />
        <Route path="/contact" element={<h1>This is Contact Page</h1>} />
        <Route path="/service" element={<h1>This is Service Page</h1>} />
      </Routes>
    </BrowserRouter>
  );
}

export default Routing;
