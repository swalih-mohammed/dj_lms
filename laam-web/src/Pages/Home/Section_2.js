import React from "react";
import styled from "styled-components";
import { WhatsAppButton } from "../../Components/Utils";
import { Grid, Typography } from "@mui/material";
import { Box } from "@mui/system";
import Container from '@mui/material/Container';


function SectionOne() {
  return (
      <Box sx={{ flexGrow: 1, paddingTop:15, paddingBottom:15, backgroundColor: "#e5e8eb" }}>
      <Container>
      <Grid container >
        <Grid item xs={12} md={6}>
        <img src={require("../../images/section_1.png")} alt={""} />
        </Grid>
        <Grid item  xs={12} md={6}>
        <Typography variant="subtitle1" sx={{color: "#023047"}}>Learn English on the move</Typography>
          <Typography variant="h4" sx={{mb: 2, color: "primary.main"}}>Download our Android App today</Typography>
          <Typography variant="body2" sx={{color: "#023047"}}>
          Improve your English with our fun and exciting learning app!
                  Designed for adult learners. Our lessons and quizzes will help
                  you learn English at home or on the move
          </Typography>
          <WhatsAppButton  />
        </Grid>
      </Grid>
      </Container>
      </Box>

  );
}

export default SectionOne;