# 🚀 Binance Futures Trading Bot (Testnet)

## 📌 Overview

This project is a simplified **Python-based trading bot** that interacts with the **Binance Futures API (Testnet/Demo)**.
It allows users to place **MARKET**, **LIMIT**, and **STOP-LIMIT** orders via a clean and user-friendly CLI interface.

The application is designed with a modular architecture, proper logging, validation, and error handling to simulate a real-world trading system.

---

## ✨ Features

### Core Features

* ✅ Place **MARKET orders** (instant execution)
* ✅ Place **LIMIT orders** (execution at specified price)
* ✅ Place **STOP-LIMIT orders** (trigger-based execution)
* ✅ Supports both **BUY** and **SELL**
* ✅ CLI-based input using `argparse`

### Code Quality

* ✅ Modular architecture (client, orders, validators, CLI)
* ✅ Input validation with meaningful error messages
* ✅ Exception handling for API and runtime errors
* ✅ Logging of requests, responses, and errors

### Bonus Features Implemented

* 🚀 **Enhanced CLI UX**

  * Interactive prompts (fallback if arguments not provided)
  * Clean formatted output using **Rich library**
* 🚀 **STOP-LIMIT Order Support**

  * Includes `stop_price` trigger logic

---

## 🛠️ Tech Stack

* Python 3.x
* python-binance
* argparse
* python-dotenv
* rich (for CLI UI)
* logging

---

## 📂 Project Structure

```
trading_bot/
│
├── client.py            # Binance API client setup
├── orders.py            # Order execution logic
├── validators.py        # Input validation
├── logging_config.py    # Logging configuration
├── cli.py               # CLI entry point
├── trading_bot.log      # Log file (generated)
├── requirements.txt
├── .env                 # API credentials (not shared)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## ▶️ Usage

### 🔹 MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### 🔹 LIMIT Order

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 60000
```

---

### 🔹 STOP-LIMIT Order

```
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.002 --price 80000 --stop_price 79000
```

---

### 🔹 Interactive Mode (Bonus UX)

```
python cli.py
```

👉 Prompts user for inputs interactively

---

## 📊 Sample Output

```
📌 Order Request Summary
┏━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Field      ┃ Value      ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ symbol     │ BTCUSDT    │
│ side       │ BUY        │
│ type       │ MARKET     │
│ quantity   │ 0.001      │
└────────────┴────────────┘

✅ Order Successful!
Order ID: 12345678
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00
```

---

## 📝 Logging

All API interactions are logged in:

```
trading_bot.log
```

Includes:

* Order requests
* Order responses
* Errors

---

## ⚠️ Important Notes / Assumptions

* Binance Futures Testnet/Demo environment is used
* Minimum order notional value must be **≥ 100 USDT**
* STOP-LIMIT order rules:

  * BUY → `stop_price > current price`
  * SELL → `stop_price < current price`
* API keys must have Futures trading enabled

---

## 🧪 Test Coverage

* ✅ MARKET order execution
* ✅ LIMIT order placement
* ✅ STOP-LIMIT order validation and execution
* ✅ Invalid input handling
* ✅ API error handling

---

## 📦 Deliverables Included

* Source code (modular structure)
* README.md (setup + usage)
* requirements.txt
* Log file containing:

  * MARKET order
  * LIMIT order

---

## 🚀 Future Improvements

* Add OCO / TWAP / Grid trading strategies
* Add web-based UI (Streamlit / React)
* Add automated trading strategies
* Add unit tests

---

## 👨‍💻 Author

Kalpesh Sonar
GitHub: https://github.com/sonar-kalpesh-18
