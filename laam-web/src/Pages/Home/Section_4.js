import React from "react";
import styled from "styled-components";
import { WhatsAppButton } from "../../Components/Utils";
import { Grid, Typography } from "@mui/material";
import { Box } from "@mui/system";
import Container from '@mui/material/Container';


function SectionOne() {
  return (
  <Box sx={{ flexGrow: 1, mt:15 , backgroundColor: "#e5e8eb", paddingTop:15, paddingBottom:15,  }}>
    <Container>
      <Grid container >
        <Grid item xs={12} md={6}>
        <img src={require("../../images/weeklyclass.png")} alt={""} />
        </Grid>
        <Grid item  xs={12} md={6}>
        <Typography variant="subtitle1" sx={{color: "#023047"}}>Weekly Grammar Sessions</Typography>
          <Typography variant="h4" sx={{mb: 2, color: "primary.main"}}>Weekly Live session</Typography>
          <Typography variant="body2" sx={{color: "#023047"}}>
          Our English Online courses offer different activities to ensure that you get the most of your learning experience. Improve your English in live online classes, with students from around the world. Each class is delivered by experienced teachers who will give you individual feedback and guidance.
          </Typography>
          <WhatsAppButton  />
        </Grid>
      </Grid>
      </Container>
      </Box>
    
  );
}

export default SectionOne;