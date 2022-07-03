import React from "react";
import styled from "styled-components";
// import { Button } from "../globalStyles";
import { AiOutlineWhatsApp } from "react-icons/ai";
import Button from '@mui/material/Button';
// import { Link } from "react-router-dom";


export const Section = styled.div`
  color: #fff;
  /* padding: 160px 0; */
  padding: 70px 0px;
  background: "#002240";
`;
export const TopLine = styled.div`
  color: "#4B59F7";
  font-size: 18px;
  line-height: 16px;
  font-weight: 700;
  letter-spacing: 1.4px;
  margin-bottom: 16px;
`;

export const Row = styled.div`
  display: flex;
  margin: 0 -15px -15px -15px;
  /* margin: 15px; */
  /* margin: auto 15px; */
  flex-wrap: wrap;
  align-items: center;
  flex-direction: "row";
`;

export const Column = styled.div`
  margin-bottom: 15px;
  padding-right: 15px;
  padding-left: 15px;
  flex: 1;
  max-width: 50%;
  flex-basis: 50%;

  @media screen and (max-width: 768px) {
    max-width: 100%;
    flex-basis: 100%;
    display: flex;
    justify-content: center;
  }
`;

export const ImgWrapper = styled.div`
  max-width: 555px;
  display: flex;
  justify-content: "flex-end";
`;

export const Img = styled.img`
  padding-right: 0;
  border: 0;
  max-width: 100%;
  vertical-align: middle;
  display: inline-block;
  max-height: 500px;
`;

export const TextWrapper = styled.div`
  max-width: 540px;
  padding-top: 0;
  padding-bottom: 60px;

  @media screen and (max-width: 768px) {
    padding-bottom: 65px;
    /* padding-left: 20px; */
    /* padding-right: 20px; */
  }
`;

export const Title = styled.h1`
  margin-bottom: 24px;
  font-size: 48px;
  line-height: 1.1;
  font-weight: 600;
  color: "#f7f8fa";
  @media screen and (max-width: 768px) {
    font-size: 38px;
  }
`;

export const Subtitle = styled.p`
  max-width: 440px;
  margin-bottom: 35px;
  font-size: 18px;
  line-height: 24px;
  color: ${({ lightTextDesc }) => (lightTextDesc ? "#a9b3c1" : "#1c2237")};
`;

const handleButtonClick = ()=>{
  const link = "https://wa.me/7207724191/?text=Please%20help%20me%20to%20join%20the%20course"
  window.open(link, "_blank")
}
export const WhatsAppButton = () => {
  return (
    <Button sx={{mt:2}} onClick={handleButtonClick} variant="contained">Join today</Button>
  );
};

