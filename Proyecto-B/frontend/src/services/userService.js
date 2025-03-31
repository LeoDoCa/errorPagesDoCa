import apiClient from "./tokenService";

const userService = {
  // Obtener todos los usuarios
  getAllUsers: async () => {
    try {
      const response = await apiClient.get("api/");
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Obtener un usuario por ID
  getUserById: async (id) => {
    try {
      const response = await apiClient.get(`api/${id}/`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Actualizar un usuario
  updateUser: async (id, userData) => {
    try {
      const response = await apiClient.put(`api/${id}/`, userData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Eliminar un usuario
  deleteUser: async (id) => {
    try {
      const response = await apiClient.delete(`api/${id}/`);
      return response;
    } catch (error) {
      throw error;
    }
  },

  // Obtener el ID del usuario actualmente logueado
  getCurrentUserId: () => {
    const token = localStorage.getItem("accessToken");
    if (!token) return null;
    
    // Decodificar el token JWT para obtener la información del usuario
    try {
      // JWT está dividido en tres partes separadas por puntos
      const payload = token.split(".")[1];
      // Decodificar la parte del payload
      const decodedPayload = JSON.parse(atob(payload));
      // Obtener el ID del usuario desde el payload
      return decodedPayload.user_id;
    } catch (error) {
      console.error("Error decoding token:", error);
      return null;
    }
  }
};

export default userService;