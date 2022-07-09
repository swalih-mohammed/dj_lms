import React from "react";
import { Helmet } from "react-helmet";
import Home from "./Pages/Home/index";
import CssBaseline from '@mui/material/CssBaseline';
import Navbar from "./Components/Navbar"
import Privacy from "./Pages/Privacy"
import { createTheme, ThemeProvider } from '@mui/material/styles';

import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import Footer  from "./Components/Footer";

const theme = createTheme({
  palette: {
    primary: {
      main: "#14a800",
    },
    secondary: {
      main: '#651fff',
    },
    text:{
      primary: "#14a800"
    }
  },
});

function App() {
  return (
    <ThemeProvider theme={theme} >
    <BrowserRouter>
      <Helmet>
        <meta charSet="utf-8" />
        <title>Laam Academy | Learn English online</title>
        <meta name="description" content="Learn English from Laam Academy" />
        <link rel="canonical" href="http://laamacademy.com" />
      </Helmet>
      <CssBaseline />
      <Navbar/>
    <Routes>
        <Route path="/"  element={<Home/>} />
        <Route path="privacy-policy" element={<Privacy/>} />
        </Routes>
      <Footer />
      </BrowserRouter>
      </ThemeProvider>
  );
}

export default App;