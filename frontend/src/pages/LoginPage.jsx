import React, { useState } from "react";
import api, { loginUser } from "../services/api";
import { useNavigate } from "react-router-dom";
import { useUser } from "../userContext";

export default function LoginPage(){
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const navigate = useNavigate(); 
    const { setUser } = useUser();

    const handleSubmit = async (e) => {
        e.preventDefault();

        try{
            const user = await loginUser(email, password);
            console.log("User data retrieved:" , user);
            setUser(user);
            localStorage.setItem("user", JSON.stringify(user));
            navigate("/dashboard");
        } catch (err) {
            console.error(err.response?.data || err.message);
            setMessage("User not found, Email or Password invalid")
        }
    }
    return (
        <div>
            <h2>Log In</h2>
            <form onSubmit={handleSubmit}>
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
                <button type="submit">Log In</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
}