import React from "react";
import SectionOne from "./Section_1";
import SectionTwo from "./Section_2";
import SectionThree from "./Section_3";
import SectionFour from "./Section_4";
import SectionFive from "./Section_5";

function Home() {

  React.useEffect(() => {
    console.log("Home");
  }, []);
  return (
    <>
<SectionOne/>
<SectionTwo/>
<SectionThree/>
<SectionFour/>
<SectionFive/>

    </>
  );
}

export default Home;