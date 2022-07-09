import React from "react";
import styled from "styled-components";
import { WhatsAppButton } from "../../Components/Utils";
import { Grid, Typography } from "@mui/material";
import { Box } from "@mui/system";
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';



const handleButtonClick = ()=>{
  const link = "https://play.google.com/store/apps/details?id=com.sibiyan.laamacademy"
  window.open(link, "_blank")
}

function SectionOne() {
  return (
      <Box sx={{ flexGrow: 1, paddingTop:15, paddingBottom:15, backgroundColor: "#e5e8eb" }}>
      <Container>
      <Grid container >
        <Grid item xs={12} md={6}>
        <img src={require("../../images/phone.png")} alt={""} />
        </Grid>
        <Grid item  xs={12} md={6}>
        <Typography variant="subtitle1" sx={{color: "#023047"}}>Learn English on the move</Typography>
          <Typography variant="h4" sx={{mb: 2, color: "primary.main"}}>Download our Android App today</Typography>
          <Typography variant="body2" sx={{color: "#023047"}}>
          Improve your English with our fun and exciting learning app!
                  Designed for adult learners. Our lessons and quizzes will help
                  you learn English at home or on the move
          </Typography>
          <Box sx={{widht:200, width:200, mt: 2}}>
            <a href="https://play.google.com/store/apps/details?id=com.sibiyan.laamacademy">
          <img style={{height:100, widht: 100, }} src={require("../../images/playstore.png")} alt={""} />
          </a>
          </Box>
         
           <Button sx={{mt:2}} variant="contained" onClick={handleButtonClick}>Download</Button>
        </Grid>
      </Grid>
      </Container>
      </Box>

  );
}

export default SectionOne;