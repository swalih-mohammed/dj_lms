import React from "react";
import styled from "styled-components";

import {
  FaFacebook,
  FaInstagram,
  FaYoutube,
  FaTwitter,
  FaLinkedin,
} from "react-icons/fa";

import { FaMagento } from "react-icons/fa";
import { Link } from "react-router-dom";

export const FooterContainer = styled.div`
  /* background-color: #101522; */
  background-color: #fff;
  padding: 4rem 0 2rem 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`;

export const FooterSubscription = styled.section`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin-bottom: 24px;
  padding: 24px;
  color: #fff;
`;

export const FooterSubHeading = styled.p`
  font-family: "Trebuchet MS", "Lucida Sans Unicode", "Lucida Grande",
    "Lucida Sans", Arial, sans-serif;
  margin-bottom: 24px;
  font-size: 24px;
  color: "#f7f8fa";
`;

export const FooterSubText = styled.p`
  margin-bottom: 24px;
  font-size: 20px;
  /* color: "#f7f8fa"; */
  color: #f7f8fa;
`;

export const Form = styled.form`
  display: flex;
  justify-content: center;
  align-items: center;

  @media screen and (max-width: 820px) {
    flex-direction: column;
    width: 80%;
  }
`;

export const FormInput = styled.input`
  padding: 10px 20px;
  border-radius: 2px;
  margin-right: 10px;
  outline: none;
  border: none;
  font-size: 16px;
  border: 1px solid #fff;

  &::placeholder {
    color: #242424;
  }

  @media screen and (max-width: 820px) {
    width: 100%;
    margin: 0 0 16px 0;
  }
`;

export const FooterLinksContainer = styled.div`
  width: 100%;
  max-width: 1000px;
  display: flex;
  justify-content: center;

  @media screen and (max-width: 820px) {
    padding-top: 32px;
  }
`;

export const FooterLinksWrapper = styled.div`
  display: flex;
  justify-content: space-evenly;

  @media screen and (max-width: 820px) {
    flex-direction: column;
  }
`;

export const FooterLinkItems = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* align-items: flex-start; */
  margin: 16px;
  padding-right: 20px;
  text-align: left;
  width: 160px;
  box-sizing: border-box;
  color: #fff;
  /* color: #141413; */
  /* color: #f7f8fa; */

  a {
    text-decoration: none;
    /* color: #fff; */
    color: #141413;
  }

  @media screen and (max-width: 420px) {
    margin: 0;
    padding: 10px;
    width: 100%;
  }
`;

export const FooterLinkTitleLocality = styled.h2`
  margin-bottom: 15px;
  display: flex;
  justify-content: center;
  /* color: #fff; */
  /* color: #141413; */
  margin-top: 10px;
  color: #f7f8fa;
`;

export const FooterLinkTitle = styled.h2`
  margin-bottom: 1opx;
`;
export const FooterDescription = styled.p`
  max-width: 440px;
  margin-bottom: 35px;
  font-size: 18px;
  line-height: 24px;
  color: #f7f8fa;
`;

export const FooterLink = styled(Link)`
  /* color: #fff; */
  /* color: #141413; */
  color: #f7f8fa;
  text-decoration: none;
  margin-bottom: 0.5rem;

  &:hover {
    color: #0467fb;
    transition: 0.3s ease-out;
  }
`;

export const SocialMedia = styled.section`
  max-width: 1000px;
  width: 100%;
`;

export const SocialMediaWrap = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 90%;
  max-width: 1000px;
  margin: 40px auto 0 auto;

  @media screen and (max-width: 820px) {
    flex-direction: column;
  }
`;

export const SocialLogo = styled(Link)`
  /* color: #fff; */
  color: #141413;
  justify-self: start;
  cursor: pointer;
  text-decoration: none;
  font-size: 2rem;
  display: flex;
  align-items: center;
  margin-bottom: 16px;
`;

export const SocialIcon = styled(FaMagento)`
  margin-right: 10px;
`;

export const WebsiteRights = styled.small`
  /* color: #fff; */
  color: #141413;
  margin-bottom: 16px;
`;

export const SocialIcons = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 240px;
`;

export const SocialIconLink = styled.a`
  /* color: #fff; */
  color: #141413;
  font-size: 24px;
`;

const Section = styled.div`
  color: #fff;
  padding: 160px 0;
  padding: 70px 0px;
  background: "#002240";
  /* background-color: "#002240"; */
`;
const TopLine = styled.div`
  color: ${"#4B59F7"};
  font-size: 18px;
  line-height: 16px;
  font-weight: 700;
  letter-spacing: 1.4px;
  margin-bottom: 16px;
`;

const Row = styled.div`
  display: flex;
  margin: 0 -15px -15px -15px;
  margin-bottom: 20;
  flex-wrap: wrap;
  /* align-items: center; */
  /* flex-direction: "row"; */
  /* justify-content: "center"; */
  /* align-items: "center"; */
`;

const Column = styled.div`
  margin-bottom: 15px;
  padding-right: 15px;
  padding-left: 15px;
  flex: 1;
  max-width: 50%;
  flex-basis: 50%;
  justify-content: "center";
  align-items: "center";

  @media screen and (max-width: 768px) {
    max-width: 100%;
    flex-basis: 100%;
    display: flex;
    justify-content: center;
  }
`;

function Footer() {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        backgroundColor: "#002240",
        paddingBottom: 50,
      }}
    >
      <div
        style={{
          flex: 2,
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-around",
          flexWrap: "wrap",
        }}
      >
        <div style={{ justifyContent: "center", alignItems: "center" }}>
          <FooterLinkTitleLocality style={{ justifyContent: "center" }}>
            Addresss
          </FooterLinkTitleLocality>
          <FooterDescription>
            104, Crescent Heights, Kismathpur,<br></br> Hyderabad, Telengana,
            500030.
          </FooterDescription>
        </div>
        <div
          style={{
            marginBottom: 20,
            // justifyContent: "center",
            // alignItems: "flex-start",
            // backgroundColor: "red",
          }}
        >
          <FooterLinkTitleLocality>CONTACT US</FooterLinkTitleLocality>
          <FooterLinkItems style={{ color: "#f7f8fa" }}>
            <a style={{ color: "#f7f8fa" }} href="tel:+91 7207724191">
              7207724191
            </a>
            <a
              style={{ color: "#f7f8fa" }}
              href="mailto:support@laamacademy.com"
            >
              support@laamacademy.com
            </a>
          </FooterLinkItems>
        </div>
      </div>
      <div
        style={{
          flex: 1,
          // backgroundColor: "green",
          display: "flex",
          justifyContent: "center",
          marginBottom: 10,
        }}
      >
        <div>
          <SocialIcons>
            <SocialIconLink href="/" target="_blank" aria-label="Facebook">
              <FaFacebook color="#ffff" />
            </SocialIconLink>
            <SocialIconLink href="/" target="_blank" aria-label="Instagram">
              <FaInstagram color="#ffff" />
            </SocialIconLink>
            <SocialIconLink
              href={"/"}
              rel="noopener noreferrer"
              target="_blank"
              aria-label="Youtube"
            >
              <FaYoutube color="#ffff" />
            </SocialIconLink>
            <SocialIconLink href="/" target="_blank" aria-label="Twitter">
              <FaTwitter color="#ffff" />
            </SocialIconLink>
            <SocialIconLink href="/" target="_blank" aria-label="LinkedIn">
              <FaLinkedin color="#ffff" />
            </SocialIconLink>
          </SocialIcons>
        </div>
      </div>
      <div
        style={{
          flex: 1,
          // backgroundColor: "red",
          display: "flex",
          justifyContent: "center",
        }}
      >
        <div>
          <SocialIconLink
            href="/privacy-policy"
            style={{ marginRight: 10, fontSize: 14, color: "#ffff" }}
          >
            Privacy Policy
          </SocialIconLink>
          <WebsiteRights style={{ color: "#ffff" }}>
            Laam Academy © 2022
          </WebsiteRights>
        </div>
      </div>
    </div>

  );
}

export default Footer;