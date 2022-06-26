import React from "react";
import styled, { createGlobalStyle } from "styled-components";
import { AiOutlineWhatsApp } from "react-icons/ai";

const GlobalStyle = createGlobalStyle`
  * {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Source Sans Pro', sans-serif;
 } 
`;

export const Container = styled.div`
  z-index: 1;
  width: 100%;
  max-width: 1300px;
  margin-right: auto;
  margin-left: auto;
  padding-right: 50px;
  padding-left: 50px;

  @media screen and (max-width: 991px) {
    padding-right: 30px;
    padding-left: 30px;
    max-width: 90%;
  }
`;

export const Button = styled.button`
  border-radius: 4px;
  background: ${({ primary }) => (primary ? "#4B59F7" : "#0467FB")};
  white-space: nowrap;
  padding: ${({ big }) => (!big ? "12px 64px" : "10px 20px")};
  color: #fff;
  font-size: ${({ fontBig }) => (fontBig ? "20px" : "16px")};
  border-radius: 20px;
  /* width: 150px; */
  /* min-width: "500px"; */
  outline: none;
  border: none;
  cursor: pointer;

  &:hover {
    transition: all 0.3s ease-out;
    background: #fff;
    background-color: ${({ primary }) => (primary ? "#0467FB" : "#4B59F7")};
  }

  @media screen and (max-width: 960px) {
    width: 100%;
  }
`;

export const WhatsAppButton = () => {
  return (
    <a href="https://wa.me/7207724191/?text=Please%20help%20me%20to%20join%20the%20course">
      <Button>
        {"Join today"} <AiOutlineWhatsApp />
      </Button>
    </a>
  );
};

export default GlobalStyle;