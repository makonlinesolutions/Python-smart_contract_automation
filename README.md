# 🚀 Wallet Automation Backend (Python + Flask)

This repository contains the backend server for the Wallet Automation Platform.  
It automates smart contract interactions (Approve, Swap, Liquidity, Mint) and handles wallet batches with support for social media simulation (Telegram, Twitter, Discord).

---

## Features

- Batch wallet automation using a simple JSON input
- Approve, Swap, Liquidity, Mint flows (EVM compatible)
- Flask REST API (`/api/start`) for integration with frontend
- Telegram, Twitter, Discord simulation via Playwright (Premium)
- .env configuration for contract addresses, tokens, proxies, etc.
- Logging and error notifications

---

## Setup

### Prerequisites

- Python 3.10 or higher
- `pip` package manager
- (Optional) [Node.js](https://nodejs.org/) for social media simulation with Playwright

### Installation

```bash
git clone https://github.com/your-org/python-smart_contract_automation.git
cd python-smart_contract_automation

# Create virtual environment
python -m venv venv
venv\Scripts\activate         # Windows
# or
source venv/bin/activate      # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# (If using social features)
python -m playwright install

# Start Flask server
python app.py
