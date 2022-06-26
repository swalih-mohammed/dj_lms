import React from "react";
import { Helmet } from "react-helmet";
import GlobalStyle from "./globalStyles";
import Home from "./pages/HomePage/Home";
import About from "./pages/About/About";
import Support from "./pages/Support/Support";
import PasswordReset from "./pages/PasswordReset/PasswordReset";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import ScrollToTop from "./components/ScrollToTop";
import { Navbar, Footer } from "./components";
import Privacy from "./pages/Privacy/privacy";

function App() {
  return (
    <Router>
      <GlobalStyle />
      <ScrollToTop />
      <Helmet>
        <meta charSet="utf-8" />
        <title>Laam Academy | Learn English online</title>
        <meta name="description" content="Learn English from Laam Academy" />
        <link rel="canonical" href="http://laamacademy.com" />
      </Helmet>
      <Navbar />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/about" component={About} />
        <Route path="/support" component={Support} />
        <Route
          path="/dj-rest-auth/password/reset/confirm/:id/:token"
          component={PasswordReset}
        />
        <Route path="/privacy-policy" exact component={Privacy} />
      </Switch>
      <Footer />
    </Router>
  );
}

export default App;