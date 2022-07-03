import React from "react";
import { WhatsAppButton } from "../../Components/Utils";
import { Grid, Typography } from "@mui/material";
import { Box } from "@mui/system";
import Container from '@mui/material/Container';

function SectionOne() {
  return (
      <Box sx={{ flexGrow: 1, paddingTop:15, paddingBottom:15,  }}>
      <Container>
      <Grid container >
        <Grid item  xs={12} md={6}>
        <Typography variant="subtitle1" sx={{color: "#023047"}}>Take your English skill to the next level</Typography>
          <Typography variant="h4" sx={{mb: 2, color: "primary.main"}}>Speak English with Confidence</Typography>
          <Typography variant="body2" sx={{color: "#023047"}}>
            Learn English online and improve your skills through our
            high-quality courses and resources, all designed for adult
            language learners. Everything you find here has been specially
            created by Laam Academy, as per CEFR (Common European
            Framework of Reference for Languages) standard.
          </Typography>
          <WhatsAppButton  />
        </Grid>
        <Grid item xs={12} md={6}>
        <img src={require("../../images/section_1.png")} alt={""} />
        </Grid>
      </Grid>
      </Container>
      </Box>
  );
}

export default SectionOne;