import React from "react";
import  { useNavigate } from "react-router-dom";

export default function HomePage(){
    const navigate = useNavigate();

    const registerNav = () => {
        navigate("/register");
    };

    const loginNav = () => {
        navigate("/login")
    };

    return (
        <div>
            <h1>Welcome to Job Tracker</h1>
            <button onClick={registerNav}>Sign Up</button>
            <br></br>
            <button onClick={loginNav}>Log In</button>
        </div>
    );
}