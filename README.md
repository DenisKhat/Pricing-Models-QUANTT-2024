# QUANTT Derivatives Pricing — 2023/2024

Welcome to the official repository for the QUANTT 2023-2024 derivatives pricing team. This repository is a comprehensive collection of models, research findings, and insights developed by our team over the course of the year. Our goal is to provide details of our approaches to derivatives pricing, data sources, challenges, and the accuracy and predictions of our models.

![Banner](https://drive.google.com/uc?export=download&id=1cd3UN4nEdmHOHb9JQiZUovlGWXSpP8kg)

## Overview
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Our project aims to explore and develop traditional models for pricing derivatives. Through rigorous research and practical implementation, we strive to enhance our understanding of financial models applied in real-world scenarios.

## Models

#### Black-Scholes-Merton Model

- The Black-Scholes-Merton model is a cornerstone of modern financial theory, providing a mathematical framework for pricing European options. This was the simplest model for us to implement as the parameters were readily available, except for volatility, which was calculated by taking the standard deviation of AMD's daily percent returns.
- We found that it was analytically simple making it computationally fast, but it's overly simplistic and the key assumption that volatility is constant limits its accuracy compared to real market conditions. Overall, it's a good foundational model, hence why it's been subject to various extensions to aaddress its limitations, such as our third model.

#### Monte-Carlo Simulation Model

- The Monte-Carlo simulation model leverages random sampling and statistical modelling to estimate mathematical functions and mimic the operations of complex systems. It's extremely well-documented since it's a common model to use in more domains than just option pricing, which made it easy to examine similar implementations for Python libraries to potentially utilize.
- We found that it's fairly accurate and really excels with minimal historical data (a luxury for this project). However, it also makes too many assumptions, such as volatility being constant as well as AMD's movement following a random distribution. These assumptions resulted in it being poor at forecasting overlying market conditions or reacting to short-term market changes.
- Here's a sample of some of the random walks in our Monte-Carlo simulation:
<!--
insert image here
-->

#### Hybrid Model
- We tried a hybrid Monte-Carlo model as volatility shouldn't be a constant. It differed from the Monte-Carlo by calculating volatility and skew at each time step. Nonetheless, it ended up being more conservative in pricing than the original Monte-Carlo model. We believe this is due to our historical data with low volatility creates a feedback loop since any new prices generated would be *close* to the original historical data, so when added to that data over and over again, the overall volatility of the data gets closer to it's mean. Thus, implementing a non-constant volatility this way was flawed.

#### Heston Model

- The Heston is an extension of the Black-Scholes-Merton by modelling variable volatility, rather than a constant volatility. This made the Heston much more complex to implement than our other models as it involved findings way to calculate AMD's mean reversion rate, volatility of volatility, and numerous other model parameters.
<!--
insert two gif diagrams from the presentation here in two table columns
-->
- We found that it's pricing was still generally conservative. It had a tendency to predict better than the Black-Scholes-Merton, but worse than either our original Monte-Carlo or our hybrid Monte-Carlo. Although, there is a higher chance of an error in our implementation with this model, as estimating certain parameters was difficult and probably requires a higher level knowledge of math than our team possesses. Overall, if our findings are to be believed, we found that treating volatility as a random variable didn't improve our predictions

## Data Sources

Initially, Yahoo Finance was our primary data source. However, after identifying innumerable discrepancies between it and market data from other verifiable sources, we transitioned to exclusively using data from Interactive Broker's API. This decision was driven by our commitment to precision, acknowledging that even minimal inaccuracies can significantly impact model performance.

## Research

Our research concentrated on several key areas, including, but not limited to, the volatility smile & skew and the impact of news, like macroeconomic announcements and geopolitical events, on market volatility, which affects option pricing.

### Volatility Smile & Skew

- The volatility smile is a phenomenon where implied volatilities varying across strike prices are graphed and look like a smile. The primary cause for the changes in implied volatility is supply and demand, as simply further ITM or OTM options have less demand, and thus less the market's supply for them is much lower and the risk of providing liquidity for these options is higher, hence the higher IV.
<!--
insert altered diagram from Investopedia
-->
- The volatility skew describes AMD's changing IV with respect to strike price. A stock's skew can be used as an insight into it's risk assessment, option pricing, and hedging strategies.
<!--
insert diagram from Optionistics
-->

### Impact of News on Implied Volatility

- Macroeconomic announcements and geopolitical events can greatly affect market volatility, and thus options pricing as a result.
- Our first example was the most recent FOMC meeting (March 20, 2024), where Jerome Powell, the United States Federal Reserve Chair announced that they were still expecting to have three interest rate cuts this year. The uncertainty around the outcome of the meeting led market IV to jump significantly, for instance on SPX shorter-term option chains had IV jump to as high as 28%.
- Our second example is that when the Russia-Ukraine war started, overnight the S&P 500 dropped over 2.5% due to this unexpected event. As a result, the pricing of options the next morning on this drop had changed significantly as IV jumped. Nonetheless, the market recovered quite quickly and the options pricing balance was restored within a couple days. 

## Accuracy & Predictions
<!--
insert pictures of SPY & AMD's movement over the year
-->

- Given our limited access to historical option data, our models follow their standard — albeit basic — implementation. Hence, none of the models were particularly accurate when tested against real-market data. Nonetheless, our Monte-Carlo model had the highest accuracy of forecasting AMD pricing, thus it had the best performance when used for predicting option prices on AMD.
- If we made predictions solely from our quantitative models, they *essentially* suggest buying most available put permutations on the AMD options chain as it forecasts AMD's stock price to be quite lower than it's current price. Realistically though, there are factors that they cannot take into account. Firstly, Jerome Powell, the chair of the United States Federal Reserve, announced on March 20, 2024 that there are still three interest rate cuts planned for this fiscal year. Further, AMD is *largely* a semiconductor stock, which is apart of a stock group with roughly cyclical movement. Hence, our actual chosen AMD option to purchase would be AMD240920C00230000 (230C for Sept 20, 2024).

## Team
| ![Jordan Matus](https://drive.google.com/uc?export=download&id=1Ucw8tXeEeIzCuUz67dVtSeDBWi382w9z) | ![Anthony Galassi](https://drive.google.com/uc?export=download&id=1KNzJPQauTXHuwcw-eQplb_f1gPE81mHh) | ![Denis Khatnyuk](https://drive.google.com/uc?export=download&id=1zmHMrE9AEOIGz7zXIm16ksioyz2gER6q) | ![Owen Martens](https://drive.google.com/uc?export=download&id=1m_Ce3Da90u63LLQj6DOJEpoAM-dCAw0U) | ![Jack Switzer](https://drive.google.com/uc?export=download&id=1VTrLpG2Qcvc54Kdc3PSz2SmBCbZpcld4) | ![Daryan Fadavi](https://drive.google.com/uc?export=download&id=1RpmcVph-HPidpxulkwfeYPEt3d2B63Mr) |
|:-----------------------------:|:-----------------------:|:-------------------------:|:----------------------------:|:-------------------------:|:-------------------------:|
| [Jordan Matus](https://www.linkedin.com/in/jordanmatus/) <br> Project Manager | [Anthony Galassi](https://www.linkedin.com/in/anthonygalassi/) <br> Team Lead | [Denis Khatnyuk](https://www.linkedin.com/in/dkhatnyuk/) <br> Team Member | [Owen Martens](https://www.linkedin.com/in/owen-martens-28239b261/) <br> Team Member | [Jack Switzer](https://www.linkedin.com/in/jack-switzer-ba102418a/) <br> Team Member | [Daryan Fadavi](https://www.linkedin.com/in/daryanfadavi/) <br> Team Member |

## Acknowledgements

We sincerely thank the QUANTT 2023-2024 executive team for their unwavering support, leadership, and organization. Their initiative to introduce the derivatives pricing team this year has been instrumental in providing us with invaluable learning opportunities. Here's hoping that next year will be an even greater success for the club!

We want to acknowledge Interactive Brokers as our intermediary in obtaining high-quality CBOE market data, which was essential for being able to test the accuracy of our models.

We look forward to continuing our journey in the field of quantitative finance!

---

For more information or questions, please get in touch with us through LinkedIn.
