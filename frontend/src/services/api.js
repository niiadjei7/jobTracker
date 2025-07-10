import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000", // FastAPI backend
    headers: {
        "Content-Type": "application/json", 
    }
});


//Register new User
export const registerUser = async (firstName, lastName, email, password) => {
    const response = await api.post("/users/", {
        first_name: firstName,
        last_name: lastName,
        email,
        password
    });
    return response.data;
};

//Sign in 
export const loginUser = async (email, password) => {
    console.log("calling loginUser...")
    const response = await api.post("/users/login", {
        email,
        password
    });
    return response.data;
};


export default api;