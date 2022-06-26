import React from "react";
import { Helmet } from "react-helmet";
import GlobalStyle from "./globalStyles";
import Home from "./Pages/Home/index";
import AppBar from '@mui/material/AppBar';
import CssBaseline from '@mui/material/CssBaseline';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import CameraIcon from '@mui/icons-material/PhotoCamera';
import MenuSharp from '@mui/icons-material/MenuSharp';
import Navbar from "./Components/Navbar"


// import About from "./pages/About/About";
// import Support from "./pages/Support/Support";
// import PasswordReset from "./pages/PasswordReset/PasswordReset";
// import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
// import ScrollToTop from "./components/ScrollToTop";
import Footer  from "./Components/Footer";
// import Privacy from ". /pages/Privacy/privacy";

function App() {
  return (
    <BrowserRouter>
      {/* <GlobalStyle /> */}
      {/* <ScrollToTop /> */}
      <Helmet>
        <meta charSet="utf-8" />
        <title>Laam Academy | Learn English online</title>
        <meta name="description" content="Learn English from Laam Academy" />
        <link rel="canonical" href="http://laamacademy.com" />
      </Helmet>
      {/* <Navbar /> */}
      <CssBaseline />
      {/* <AppBar position="relative">
        <Toolbar>
          <MenuSharp sx={{ mr: 2 }} />
          <Typography variant="h6" color="inherit" noWrap>
            Laam Academy
          </Typography>
        </Toolbar>
      </AppBar> */}
      <Navbar/>
    
    <Routes>
        <Route path="/"  element={<Home/>} />
        {/* <Route path="/about" component={About} /> */}
        {/* <Route path="/support" component={Support} /> */}
        {/* <Route
          path="/dj-rest-auth/password/reset/confirm/:id/:token"
          component={PasswordReset}
        /> */}
        {/* <Route path="/privacy-policy" exact component={Privacy} /> */}
        </Routes>
 
      <Footer />
      </BrowserRouter>
  );
}

export default App;