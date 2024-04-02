# QUANTT Derivatives Pricing — 2023/2024

Welcome to the official repository for the QUANTT 2023-2024 derivatives pricing team. This repository is a comprehensive collection of models, research findings, and insights developed by our team over the course of the year. Our goal is to provide details of our approaches to derivatives pricing, data sources, challenges, and the accuracy and predictions of our models.

![Banner](https://drive.google.com/uc?export=download&id=1cd3UN4nEdmHOHb9JQiZUovlGWXSpP8kg)

## Overview
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Our project aims to explore and develop traditional models for pricing derivatives. Through rigorous research and practical implementation, we strive to enhance our understanding of financial models applied in real-world scenarios.

## Models

#### Black-Scholes-Merton Model

- The Black-Scholes-Merton model is a cornerstone of modern financial theory, providing a mathematical framework for pricing European options. Our implementation...

#### Monte-Carlo Simulation Model

- The Monte-Carlo simulation model leverages random sampling and statistical modelling to estimate mathematical functions and mimic the operations of complex systems. Our application...

#### Heston Model

- The Heston distinguishes from the Black-Scholes-Merton by modelling variable volatility, rather than a constant volatility. This makes the Heston...

## Data Sources

Initially, Yahoo Finance was our primary data source. However, after identifying innumerable discrepancies between it and market data from other verifiable sources, we transitioned to exclusively using data from Interactive Broker's API. This decision was driven by our commitment to precision, acknowledging that even minimal inaccuracies can significantly impact model performance.

## Research

Our research concentrated on several key areas, including, but not limited to, the volatility smile & skew and the impact of news, like macroeconomic announcements and geopolitical events, on market volatility, which affects option pricing.

### Volatility Smile & Skew

- Placeholder

### News' Impact on Implied Volatility

- Placeholder

## Accuracy & Predictions

- Given our limited access to historical option data, our models follow their standard — albeit basic — implementation. Hence, none of the models were particularly accurate when tested against real-market data. Nonetheless, our Monte-Carlo model had the highest accuracy of forecasting AMD pricing, thus it had the best performance when used for predicting option prices on AMD.
- If we made predictions solely from our quantitative models, they *essentially* suggest buying most available put permutations on the AMD options chain as it forecasts AMD's stock price to be quite lower than it's current price. Realistically though, there are factors that they cannot take into account. Firstly, Jerome Powell, the chair of the United States Federal Reserve, announced on March 20, 2024 that there are still three interest rate cuts planned for this fiscal year. Further, AMD is *largely* a semiconductor stock, which is apart of a stock group with roughly cyclical movement. Hence, our actual chosen AMD option to purchase would be AMD240920C00230000 (230C for Sept 20, 2024).

## Team
| ![Jordan Matus](https://drive.google.com/uc?export=download&id=1Ucw8tXeEeIzCuUz67dVtSeDBWi382w9z) | ![Anthony Galassi](https://drive.google.com/uc?export=download&id=1KNzJPQauTXHuwcw-eQplb_f1gPE81mHh) | ![Denis Khatnyuk](https://drive.google.com/uc?export=download&id=1zmHMrE9AEOIGz7zXIm16ksioyz2gER6q) | ![Owen Martens](https://drive.google.com/uc?export=download&id=1buxXAQyzZheQrh3jZMb-RU9G9MQMYYu0) | ![Jack Switzer](https://drive.google.com/uc?export=download&id=1VTrLpG2Qcvc54Kdc3PSz2SmBCbZpcld4) | ![Daryan Fadavi](https://drive.google.com/uc?export=download&id=1RpmcVph-HPidpxulkwfeYPEt3d2B63Mr) |
|:-----------------------------:|:-----------------------:|:-------------------------:|:----------------------------:|:-------------------------:|:-------------------------:|
| [Jordan Matus](https://www.linkedin.com/in/jordanmatus/) <br> Project Manager | [Anthony Galassi](https://www.linkedin.com/in/anthonygalassi/) <br> Team Lead | [Denis Khatnyuk](https://www.linkedin.com/in/dkhatnyuk/) <br> Team Member | [Owen Martens](https://www.linkedin.com/in/owen-martens-28239b261/) <br> Team Member | [Jack Switzer](https://www.linkedin.com/in/jack-switzer-ba102418a/) <br> Team Member | [Daryan Fadavi](https://www.linkedin.com/in/daryanfadavi/) <br> Team Member |

## Acknowledgements

We sincerely thank the QUANTT 2023-2024 executive team for their unwavering support, leadership, and organization. Their initiative to introduce the derivatives pricing team this year has been instrumental in providing us with invaluable learning opportunities. Here's hoping that next year will be an even greater success for the club!

We want to acknowledge Interactive Brokers as our intermediary in obtaining high-quality CBOE market data, which was essential for being able to test the accuracy of our models.

We look forward to continuing our journey in the field of quantitative finance!

---

For more information or questions, please get in touch with us through LinkedIn.
