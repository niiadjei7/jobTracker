import React from "react";
import { useNavigate } from "react-router-dom";
import { useUser } from "../userContext";

export default function HomePage(){
    const navigate = useNavigate();
    const { user } = useUser();

    return (
        <div>
            <h1>Welcome, {user?.first_name}!</h1>
            
        </div>
    );
}