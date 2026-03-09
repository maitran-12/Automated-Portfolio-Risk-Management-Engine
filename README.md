# ⚙️ Automated Portfolio Risk Management Engine

### Objective
- A high-performance, automated pipeline designed to quantify market risk for global asset portfolios. This engine demonstrates advanced Python proficiency in data engineering, statistical modeling, and automated visualization.

- The system is built with a **"Framework First"** mindset, ensuring scalability and robustness across diverse asset classes.

### 1. Robust Data Engineering
- **Asset-Agnostic Ingestion:** Dynamically fetches and cleans historical data for any ticker (Equities, Forex, Crypto) via `yfinance` across global exchanges (e.g. NYSE, LSE, SGX).

- **Crash Handling:** Implemented `hasattr` reflection logic to handle polymorphic data structures (Series vs DataFrame), ensuring zero-crash execution during automated runs.

- **Matrix Alignment:** Features a specialized `reindexing` layer to enforce strict synchronization between Asset Returns and Weight Vectors—critical for multi-asset accuracy.

### 2. Quantitative Analytics
- **Vectorized Computation:** Utilizes NumPy for high-speed matrix dot-products, bypassing inefficient loops to calculate Portfolio Daily Returns.

- **Risk Modeling:** Automated calculation of **95% Value at Risk (VaR)** and **Conditional VaR (CVaR/Expected Shortfall)** using non-parametric historical simulation.

- **Logarithmic Transformation:** Standardizes daily price changes into Log Returns to ensure time-additivity and statistical normality for long-term analysis.

### 3. Smart Visualization
- **Dynamic Heatmaps:** A self-adjusting correlation matrix that automatically scales based on portfolio size, using `RdYlGn` encoding for instant concentration-risk assessment.

- **Tail-Risk Diagnostics:** Automated distribution plotting with shaded "Risk Zones" to highlight extreme loss scenarios beyond the VaR threshold.

---

## 📊 Sample Output: Global Portfolio Analysis
To demonstrate the engine's capability, the following analysis was generated for a diversified global portfolio:

**Test Portfolio Composition:**
* **Tech (US):** Apple (AAPL), Microsoft (MSFT)
* **Energy (UK):** BP (BP.L)
* **Finance & Telco (Singapore):** United Overseas Bank (U11.SI), Singtel (Z74.SI)

### Terminal Result: Risk metrics calculations

![Risk metrics](https://github.com/maitran-12/Automated-Portfolio-Risk-Management-Engine/blob/e1cf78102ea67a5c89de26ee3f81f49db12701c6/Portfolio%20risk%20metrics.png)

### 📈 Visual 1: Distribution & Tail Risk
*The engine identifies the 5% worst-case daily losses and visualizes the 'Expected Shortfall' (CVaR).*

![Tail Risk Chart](https://github.com/maitran-12/Automated-Portfolio-Risk-Management-Engine/blob/e1cf78102ea67a5c89de26ee3f81f49db12701c6/Figure_1.png)


### 📊 Visual 2: Correlation Matrix
*The engine reveals sector-specific correlations (e.g., how Singaporean banking relates to US Big Tech) to optimize diversification.*
![Correlation Matrix](https://github.com/maitran-12/Automated-Portfolio-Risk-Management-Engine/blob/e1cf78102ea67a5c89de26ee3f81f49db12701c6/Figure_2.png)


---
## 🚀 How to run


```
# Clone the repository
git clone https://github.com/maitran-12/Automated-Portfolio-Risk-Management-Engine.git

# Install required dependencies
pip install -r requirements.txt
```

```
Developed by Ngoc Mai Tran, to turn raw market data into actionable investment insights.
```



