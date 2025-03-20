import { useState, useEffect } from "react";
import axios from "axios";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  useLocation,
} from "react-router-dom";
import Login from "./components/Login";
import Navbar from "./components/Navbar";
import AboutUs from "./pages/AboutUs";
import NotFound from "./pages/404";
import { AnimatePresence } from "framer-motion";

const AnimatedRoutes = () => {
  const location = useLocation();
  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route path="/login" element={<Login />} />
        <Route path="/about" element={<AboutUs />} />
        <Route path="/" element={<Home />} />
        <Route path="*" element={<NotFound />} />{" "}
        {/*Es para 404 personalizado */}
      </Routes>
    </AnimatePresence>
  );
};

//Home component
function Home() {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        setError("Error al obtener los datos" + error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Cargando...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h1>Datos de la API desde Django</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id}>{JSON.stringify(item)}</li>
        ))}
      </ul>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Navbar />
      <div className="container mt-4">
        <div className="row">
          <div className="col-12">
            <AnimatedRoutes />
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
