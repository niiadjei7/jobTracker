import React, { useState } from "react";
import api, { registerUser } from "../services/api";
import { useNavigate } from "react-router-dom";
import { useUser } from "../userContext";

export default function RegisterPage() {
    const [first_name, setFirstName] = useState("");
    const [last_name, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const navigate = useNavigate();

    const { setUser } = useUser(); 

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const user = await registerUser(first_name, last_name, email, password);
            console.log("User created:", user);
            setUser(user);
            navigate("/login");
        } catch (err) {
            console.error(err.response?.data || err.message);
            setMessage("Registration failed.");
        }
    }
    return (
        <div>
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="first_name"
                    placeholder="First Name"
                    value={first_name}
                    onChange={(e) => setFirstName(e.target.value)}
                    required
                /><br />
                <input
                    type="lastName"
                    placeholder="Last Name"
                    value={last_name}
                    onChange={(e) => setLastName(e.target.value)}
                    required
                /><br />
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                /><br />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                /><br />
                <button type="submit">Register</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
}


