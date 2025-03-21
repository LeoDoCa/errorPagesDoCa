import React, { useState, useEffect } from "react";
import axios from "axios";
import { Form, Button, Container, Row, Col } from "react-bootstrap";
import { useNavigate } from "react-router-dom";

const CustomUserForm = () => {
  const [formFields, setFormFields] = useState([]);
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    name: "",
    surname: "",
    control_number: "",
    age: "",
    tel: "",
  });
  const nav = useNavigate();

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/form/")
      .then((response) => {
        console.log(response.data); 
        setFormFields(response.data);
      })
      .catch((error) => console.error("Error al obtener los datos", error));
  }, []);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Enviar la solicitud POST para registrar el usuario
    axios
      .post("http://127.0.0.1:8000/users/form/", formData)
      .then((response) => {
        alert(response.data.message); // Mensaje de éxito
        nav("/login");
      })
      .catch((error) => {
        alert("Hubo un error al crear el usuario.");
        console.error("Error al enviar el formulario", error);
      });
  };

  return (
    <Container className="mt-5 ">
      <Row className="justify-content-md-center">
        <Col md={6}>
          <h2 className="text-center mb-4">Nuevo Usuario</h2>

          <Form onSubmit={handleSubmit}>
            {formFields &&
              Object.keys(formFields).map((field) => {
                const { label, input, type } = formFields[field];

                return (
                  <Form.Group key={field} className="mb-3">
                    <Form.Label>{label}</Form.Label>
                    <Form.Control
                      {...input}
                      value={formData[field] || ""}
                      onChange={handleInputChange}
                      name={field}
                      type={type || "text"}
                    />
                    {field === "password" && (
                      <Form.Text className="text-muted">
                        <ul className="small">
                          <li>Al menos un número.</li>
                          <li>Al menos una letra mayúscula.</li>
                          <li>Al menos un carácter especial (!#$%&?).</li>
                          <li>Mínimo de 8 caracteres en total.</li>
                        </ul>
                      </Form.Text>
                    )}
                  </Form.Group>
                );
              })}
            <Button variant="primary" type="submit" className="w-100 mt-3">
              Enviar
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};

export default CustomUserForm;
