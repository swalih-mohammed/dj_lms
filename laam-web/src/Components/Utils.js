import React from "react";
import Button from '@mui/material/Button';

const handleButtonClick = ()=>{
  const link = "https://wa.me/7207724191/?text=Please%20help%20me%20to%20join%20the%20course"
  window.open(link, "_blank")
}
export const WhatsAppButton = () => {
  return (
    <Button sx={{mt:2}} onClick={handleButtonClick} variant="contained">Join today</Button>
  );
};

