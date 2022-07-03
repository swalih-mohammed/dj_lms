import React from "react";
import styled from "styled-components";
import FacebookIcon from '@mui/icons-material/Facebook';
import YouTubeIcon from '@mui/icons-material/YouTube';
import InstagramIcon from '@mui/icons-material/Instagram';
import { Box, Grid, Typography } from "@mui/material";
import { Container } from "@mui/system";
import Link from '@mui/material/Link';



function Footer() {
  return (
      <Box sx={{ flexGrow: 1, paddingBottom:10 , paddingTop:15, backgroundColor: "#002240"}}>
      <Container >
       <Grid container spacing={2}>
       <Grid  item gap={2} xs={12} md={6}>
        <Box>
        <Typography  sx={{mb: 1, color: "#f1faee"}}>ADDRESS</Typography>
        <Typography> 104, Crescent Heights, Kismathpur,<br></br> Hyderabad, Telengana,
       500030.</Typography>
       </Box>
      </Grid>
      <Grid  item gap={2}  xs={12} md={6}>
        <Box sx={{display: "flex", flexDirection: "column"}}>
        <Typography  sx={{mb: 1, color: "#f1faee"}}>CONTACT US</Typography>
          <Link href="tel:+91 7207724191" underline="none">
          {"7207724191"}
          </Link>
          <Link href="mailto:support@laamacademy.com" underline="none">
          {" support@laamacademy.com"}
          </Link>
        </Box>
      </Grid>
       </Grid>
       <Box>
        <Grid container sx={{paddingTop: 10, flexGrow: 1}}>
          <Grid gap={2} item xs={12} md={12} sx={{ display: "flex",  justifyContent: "center", alignItems: "center"}}>
              <FacebookIcon/>
              <YouTubeIcon/>
              <InstagramIcon/>
          </Grid>
        </Grid>
        <Box sx={{ display: "flex",  justifyContent: "center", alignItems: "center", paddingTop:1}}>
        <Typography  sx={{mb: 1, color: "#f1faee"}}> Laam Academy © 2022</Typography>
        </Box>
       </Box>
      </Container>
    </Box>
   
  );
}

export default Footer;