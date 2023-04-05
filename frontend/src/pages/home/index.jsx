import React from "react";
import Header from "./components/Header";
import SubmitForm from "./components/SubmitForm";
import Footer from "./components/Footer";
import config from "../../config";
import "./index.css";
import "tailwindcss/tailwind.css";

const client = new FastAPIClient(config);

const Home = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <SubmitForm />
      <Footer />
    </div>
  );
};

export default Home;
