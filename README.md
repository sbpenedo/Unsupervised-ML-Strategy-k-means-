# Using Machine Learning to Build a Trading Strategy

This project was my deep dive into building a full quantitative trading strategy using Python. The goal was to see if an unsupervised machine learning algorithm, **KMeans clustering**, could find patterns in the market and pick a portfolio of S&P 500 stocks that could keep up with, or even beat, a simple buy and hold strategy on the SPY.

The repo contains two main files:
* `get_data.py`: The script that downloads and prepares 8 years of S&P 500 stock data.
* `unsupervised_ML_trading.ipynb`: The Jupyter Notebook where the entire strategy is built, backtested, and analyzed.

---
## How It Works

The strategy's approach is broken down into a few key steps that run on a monthly cycle:

1.  **Data & Features**: I started by downloading 8 years of daily stock prices for the S&P 500. Then, for each stock, I created a bunch of features—things like common technical indicators (RSI, MACD, Bollinger Bands) and even calculated their risk using the Fama-French 5-Factor Model.

2.  **Filtering the Universe**: To make sure the picks are tradable, the strategy narrows its focus each month to the top 150 most liquid stocks, based on their 5-year rolling average dollar volume.

3.  **Finding Market Regimes with ML**: This is the core machine learning part. I used the KMeans algorithm to group those 150 stocks into 4 different clusters. The idea is that each cluster represents a "market regime"—a group of stocks that are behaving in a similar way based on their features.

4.  **Building the Portfolio**: Once the clusters were formed, the strategy was to invest in the stocks from one of those groups. For the chosen stocks, I used the `PyPortfolioOpt` library to find the best way to allocate money between them, aiming to get the highest risk-adjusted return (Max Sharpe Ratio). If that failed, it would just equal-weight them.

---
## Performance Results
The results were pretty interesting. The strategy managed to keep pace with the SPY benchmark and even beat it for a good stretch of time between 2020 and early 2021.

However, the algorithm struggled a lot in recent years and fell behind the simple buy and hold strategy.

<img width="1335" height="490" alt="image" src="https://github.com/user-attachments/assets/b90e236b-7958-4a5b-8809-355f61c463d8" />


---
## What I Learned
This was a huge learning project for me. I got hands-on experience with the whole quantitative workflow:
-   Building a full backtesting engine from scratch.
-   Engineering a wide range of features, including integrating an academic model like Fama-French.
-   Applying an unsupervised learning model with k-means to find patterns in financial data.
-   Using new libraries likePyPortfolioOpt for portfolio construction.

For the next version, I want to improve the clustering part. I committed to using k-means but after doing more reseach I though other algorithms like **DBSCAN** could be more effective since it can find more unique patterns or identify outlier stocks.

---
## How to Run It

You'll need Python and a few libraries to run this.

### Requirements
```bash
pip install pandas numpy yfinance pandas_ta pandas-datareader scikit-learn pypfopt matplotlib statsmodels
