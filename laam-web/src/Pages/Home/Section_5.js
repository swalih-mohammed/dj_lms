import React from "react";
import { WhatsAppButton } from "../../Components/Utils";
import { Grid, Typography } from "@mui/material";
import { Box } from "@mui/system";
import Container from '@mui/material/Container';

function SectionOne() {
  return (
      <Box sx={{ flexGrow: 1, paddingTop:15, paddingBottom:15,  }}>
        <Container>
      <Grid container>
        <Grid item  xs={12} md={6}>
        <Typography variant="subtitle1" sx={{color: "#023047"}}> Boost your skill with Laam Academy Certificate</Typography>
          <Typography variant="h4" sx={{mb: 2, color: "primary.main"}}>Be a certified professional</Typography>
          <Typography variant="body2" sx={{color: "#023047"}}>
          Get a certificate when you successfully complete each course.
                  Courses are available at different levels. Demonstrate your
                  achievements.
          </Typography>
          <WhatsAppButton  />
        </Grid>
        <Grid item xs={12} md={6}>
        <img src={require("../../images/professional.png")} alt={""} />
        </Grid>
      </Grid>
      </Container>
      </Box>
  
  );
}

export default SectionOne;