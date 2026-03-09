

import yfinance as yf
import numpy as np
import pandas as pd

#Module 1: Ask for user input

user_ticker = input ("Please enter the ticker symbol of your stocks, comma as a divider: ")

ticker_list = [t.strip().upper() for t in user_ticker.split(',')]

  #Check if ticker symbol input is valid
valid_tickers = []
for t in ticker_list:
    stock = yf.Ticker(t)
    if len(stock.history(period="1d")) > 0:
      valid_tickers.append(t)
    else:
      print(f"Invalid ticker symbol: {t} or missing data")
print(f"Valid ticker symbols: {valid_tickers}")

  #Module 2: Weight input

while True:
    weights_input = input(f"Please enter the weights for {len(valid_tickers)} stock(s), comma as a divider: ")
    try:
        weights = [float(w.strip()) for w in weights_input.split(',')]

        if len(weights) != len(valid_tickers):
            print(f"Error: You provided {len(weights)} weights for {len(valid_tickers)} stocks. Try again!")
            continue

        if abs(sum(weights) - 1.0) > 1e-6:
            print(f"Invalid weight input. Total is {sum(weights)}, must add up to 1. Try again!")
            continue

        print("Valid weights inputted")
        break

    except ValueError:
        print("Error: Please enter numbers only (e.g., 0.5, 0.5).")

  #Module 3: VaR calculation

raw_data = yf.download(valid_tickers, start="2020-01-01", auto_adjust=True)

if raw_data.empty:
  raise SystemExit("No data available for your chosen tickers.")


data = raw_data['Close']

if len (valid_tickers) == 1:
  if hasattr(data, 'to_frame'):
    data = data.to_frame()
  data.columns = valid_tickers

data = data.dropna()

data = data.reindex(columns=valid_tickers)

returns = np.log(data / data.shift(1)).dropna()

portfolio_returns = returns.dot(weights)

var_95 = portfolio_returns.quantile(0.05)
print ("-" * 30)

#Conditional VaR (Expected Shortfall)
cvar_95 = portfolio_returns[portfolio_returns <= var_95].mean()

#Annualized Volatility
annual_vol = portfolio_returns.std() * (252**0.5)

print("-" * 30)
print("PORTFOLIO RISK ANALYSIS REPORT")
print(f"Confidence Level: 95%")
print(f"Time Horizon: 1-Day")
print(f"Historical Value at Risk (VaR): {var_95:.2%}")
print(f"Conditional VaR (CVaR/Expected Shortfall): {cvar_95:.2%}")
print(f"Annualized Portfolio Volatility: {annual_vol:.2%}")
print("-" * 30)

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

#figure 1: tail risk diagram
plt.figure()
ax = sns.histplot(portfolio_returns, bins=50, kde=True, color='slategray', edgecolor='white', alpha=0.7)

#Color for risky area
line = ax.get_lines()[0]
x, y = line.get_data()
ax.fill_between(x, 0, y, where=(x <= var_95), color='red', alpha=0.3, label='Risk Zone (Tail)')

#Add VaR and CVaR
plt.axvline(var_95, color='darkred', linestyle='--', linewidth=2, label=f'VaR 95%: {var_95:.2%}')
plt.axvline(cvar_95, color='orange', linestyle='-', linewidth=2, label=f'CVaR 95%: {cvar_95:.2%}')

plt.title("Portfolio Daily Returns Distribution & Tail Risk Analysis", fontsize=15, fontweight='bold')
plt.xlabel("Daily Log Returns", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.legend(loc='upper right', frameon=True)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

#figure 2: correlation matrix to judge portfolio concentration
#Only draw if portfolio has more than 1 stock
if len(valid_tickers) > 1:
    plt.clf()
    plt.figure(figsize=(10, 8))
    corr_matrix = returns.corr()

    sns.heatmap(corr_matrix,
                annot=True,
                cmap='RdYlGn',
                fmt=".2f",
                linewidths=0.5,
                center=0,
                square=True,
                cbar_kws={"shrink": .8})

    plt.title("Correlation Matrix (Diversification Check)", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
else:
    print("\n💡 Tip: Add more tickers to see the Correlation Matrix and check diversification.")