import React from "react";
import { Grid, Typography } from "@mui/material";
import { Box } from "@mui/system";
import PriceCard from "../../Components/card"
import Container from '@mui/material/Container';

function Pricing() {
  return (
    <Box sx={{ flexGrow: 1, mt:15 }}>
      <Container>
      <Box sx={{ display: "flex", flexDirection: "column", mb:5 , justifyContent: "center", alignItems: "center" }}>
      <Typography variant="subtitle1" sx={{color: "#023047"}}>Learn English on the move</Typography>
      <Typography variant="h4" sx={{mb: 2, color: "primary.main"}}>Download our Android App today</Typography>
      </Box>
      <Grid container spacing={2}>
        <Grid item sm={12} md={4}>
        <PriceCard/>
        </Grid>
        <Grid item  sm={12} md={4}>
        <PriceCard/>
        </Grid>
        <Grid item  sm={12} md={4}>
        <PriceCard/>
        </Grid>
       
      </Grid>
      </Container>
    </Box>
  );
}
export default Pricing;