import React from "react";
import { Grid, Typography } from "@mui/material";
import { Box } from "@mui/system";
import PriceCard from "../../Components/card"
import Container from '@mui/material/Container';
import {PriceCard1, PriceCard2, PriceCard3} from "../../data"

function Pricing() {
  return (
    <Box sx={{ flexGrow: 1, mt:10 }}>
      <Container>
      <Box sx={{ display: "flex", flexDirection: "column", mb:5 , justifyContent: "center", alignItems: "center" }}>
      <Typography variant="subtitle1" sx={{color: "#023047"}}>Enroll to a course today</Typography>
      <Typography variant="h4" sx={{mb: 2, color: "primary.main"}}>Three levels of certifications</Typography>
      </Box>
      <Grid container spacing={2}>
        <Grid item sm={12} md={4}>
        <PriceCard PriceCard={PriceCard1}/>
        </Grid>
        <Grid item  sm={12} md={4}>
        <PriceCard PriceCard={PriceCard2}/>
        </Grid>
        <Grid item   sm={12} md={4}>
        <PriceCard PriceCard={PriceCard3}/>
        </Grid>
       
      </Grid>
      </Container>
    </Box>
  );
}
export default Pricing;