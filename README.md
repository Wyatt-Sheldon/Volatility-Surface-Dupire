# Volatility Surface Modeling with the Dupire Local Volatility Framework

This project demonstrates the construction, visualization, and comparison of implied and local volatility surfaces using real market options data for a publicly traded asset (e.g., AAPL).

**Key Deliverables:**
- 3D interactive implied volatility surface 
- Dupire local volatility surface derived from interpolated call prices
- Smoothed final surface with Gaussian filtering
- No-arbitrage checks and practical insights into surface structure

---

## Project Overview

A volatility surface models how implied volatility varies with strike price and time to maturity. While implied volatility surfaces are observed directly from market prices, **local volatility surfaces** (via the Dupire PDE) provide a framework for modeling deterministic, path-dependent volatility under no-arbitrage conditions.

This notebook:
- Downloads live options chain data using `yfinance`
- Interpolates a call price surface: `C(K, T)`
- Computes numerical derivatives: `∂C/∂T`, `∂²C/∂K²`

- Applies Dupire’s equation:
  
  `σ²_loc(K, T) = [∂C / ∂T] / [0.5 * K² * ∂²C / ∂K²]`


- Smooths the surface using Gaussian filters to reduce noise
- Saves results in interactive Plotly HTML

---

## Technologies & Libraries

- Python 3.11
- [yfinance](https://github.com/ranaroussi/yfinance) – to fetch options chain data
- NumPy & Pandas – numerical operations
- SciPy – 2D interpolation and smoothing
- Plotly – interactive 3D surface visualization
- Jupyter Notebook – development environment

---

## Example Visualizations

**Implied Volatility Surface:**  
See [Implied Volatility Surface](https://wyatt-sheldon.github.io/Volatility-Surface-Dupire/implied_vol_surface.html)

**Smoothed Dupire Local Volatility Surface:**  
See [Smoothed Dupire Local Volatility Surface](https://wyatt-sheldon.github.io/Volatility-Surface-Dupire/smoothed_local_vol_surface.html)


---

## How to Run

Clone the repo and install dependencies:

```bash
git clone https://github.com/your-username/volatility-surface-dupire.git
cd volatility-surface-dupire
pip install -r requirements.txt

