import React from "react";
import { Button } from "../../globalStyles";
import { AiFillThunderbolt } from "react-icons/ai";
import { GiCrystalBars } from "react-icons/gi";
import { GiCutDiamond, GiRock } from "react-icons/gi";
import { MdSchool } from "react-icons/md";
import { AiOutlineLaptop, AiOutlineMobile } from "react-icons/ai";
import { IconContext } from "react-icons/lib";
import { FaRupeeSign } from "react-icons/fa";

import { Link } from "react-router-dom";
import styled from "styled-components";

const PricingSection = styled.div`
  padding: 100px 0 160px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* background: #4b59f7; */
  background: #fff;
`;

export const PricingWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 auto;

  @media screen and (max-width: 960px) {
    margin: 0 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
`;

export const PricingHeading = styled.h1`
  /* color: #fff; */
  color: #262626;
  font-size: 40px;
  margin-bottom: 24px;
  @media screen and (max-width: 960px) {
    font-size: 38px;
  }
`;

export const PricingContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;

  @media screen and (max-width: 960px) {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
  }
`;

const PricingCard = styled(Link)`
  background: #242424;
  box-shadow: 0 6px 20px rgba(56, 125, 255, 0.2);
  width: 280px;
  /* height: 500px; */
  text-decoration: none;
  border-radius: 4px;

  /* &:nth-child(4) { */
  margin: 24px;
  /* } */

  &:hover {
    transform: scale(1.06);
    transition: all 0.3s ease-out;
    color: #1c2237;
  }

  @media screen and (max-width: 960px) {
    width: 90%;

    &:hover {
      transform: none;
    }
  }
`;

const PricingCardInfo = styled.div`
  display: flex;
  flex-direction: column;
  /* height: 500px; */
  padding: 24px;
  align-items: center;
  color: #fff;
`;

const PricingCardIcon = styled.div`
  margin: 24px 0;
`;

const PricingCardPlan = styled.h3`
  margin-bottom: 5px;
  font-size: 24px;
`;

const PricingCardCostContainer = styled.div`
  display: flex;
  flex-direction: row;
  /* height: 500px; */
  /* padding: 24px; */
  align-items: center;
  color: #fff;
`;

const PricingCardCost = styled.h4`
  font-size: 40px;
`;

const PricingCardLength = styled.p`
  font-size: 14px;
  margin-bottom: 24px;
`;

const PricingCardFeatures = styled.ul`
  margin: 16px 0 32px;
  list-style: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #a9b3c1;
`;

const PricingCardFeature = styled.li`
  margin-bottom: 10px;
`;

function Pricing() {
  return (
    <IconContext.Provider value={{ color: "#a9b3c1", size: 64 }}>
      <PricingSection>
        <PricingWrapper>
          <PricingHeading>FOUR LEVELS OF CERTIFICATION</PricingHeading>
          <PricingContainer>
            <PricingCard to="/">
              <PricingCardInfo>
                <PricingCardIcon>
                  <MdSchool />
                </PricingCardIcon>
                <PricingCardPlan>SARTER</PricingCardPlan>
                <PricingCardCost>
                  <FaRupeeSign size={30} />
                  250
                </PricingCardCost>
                <PricingCardLength>per month</PricingCardLength>
                <PricingCardFeatures>
                  <PricingCardFeature>Weekly Live Classes</PricingCardFeature>
                  <PricingCardFeature>Grammar Excercise</PricingCardFeature>
                  <PricingCardFeature>Speaking Excercise</PricingCardFeature>
                  <PricingCardFeature>
                    Commuincation Strategy
                  </PricingCardFeature>
                </PricingCardFeatures>
                <Button primary>Join</Button>
              </PricingCardInfo>
            </PricingCard>
            <PricingCard to="/">
              <PricingCardInfo>
                <PricingCardIcon>
                  <MdSchool />
                </PricingCardIcon>
                <PricingCardPlan>PRE-INTERMEDIATE</PricingCardPlan>
                <PricingCardCost>
                  <FaRupeeSign size={30} />
                  500
                </PricingCardCost>
                <PricingCardLength>per month</PricingCardLength>
                <PricingCardFeatures>
                  <PricingCardFeature>Weekly Live Classes</PricingCardFeature>
                  <PricingCardFeature>Grammar Excercise</PricingCardFeature>
                  <PricingCardFeature>Speaking Excercise</PricingCardFeature>
                  <PricingCardFeature>
                    Commuincation Strategy
                  </PricingCardFeature>
                </PricingCardFeatures>
                <Button primary>Join</Button>
              </PricingCardInfo>
            </PricingCard>
            <PricingCard to="/">
              <PricingCardInfo>
                <PricingCardIcon>
                  <MdSchool />
                </PricingCardIcon>
                <PricingCardPlan>INTERMEDIATE</PricingCardPlan>
                <PricingCardCost>
                  <FaRupeeSign size={30} />
                  1000
                </PricingCardCost>{" "}
                <PricingCardLength>per month</PricingCardLength>
                <PricingCardFeatures>
                  <PricingCardFeature>Weekly Live Classes</PricingCardFeature>
                  <PricingCardFeature>Grammar Excercise</PricingCardFeature>
                  <PricingCardFeature>Speaking Excercise</PricingCardFeature>
                  <PricingCardFeature>
                    Commuincation Strategy
                  </PricingCardFeature>
                </PricingCardFeatures>
                <Button primary>Join</Button>
              </PricingCardInfo>
            </PricingCard>
            <PricingCard to="/">
              <PricingCardInfo>
                <PricingCardIcon>
                  <MdSchool />
                </PricingCardIcon>
                <PricingCardPlan>ADVANCED</PricingCardPlan>
                <PricingCardCost>
                  <FaRupeeSign size={30} />
                  2000
                </PricingCardCost>
                <PricingCardLength>per month</PricingCardLength>
                <PricingCardFeatures>
                  <PricingCardFeature>Weekly Live Classes</PricingCardFeature>
                  <PricingCardFeature>Grammar Excercise</PricingCardFeature>
                  <PricingCardFeature>Speaking Excercise</PricingCardFeature>
                  <PricingCardFeature>
                    Commuincation Strategy
                  </PricingCardFeature>
                </PricingCardFeatures>
                <Button primary>Join</Button>
              </PricingCardInfo>
            </PricingCard>
          </PricingContainer>
        </PricingWrapper>
      </PricingSection>
    </IconContext.Provider>
  );
}
export default Pricing;