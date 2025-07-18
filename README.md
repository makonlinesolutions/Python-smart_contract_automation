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
```

## Usage

- Configure .env file with your blockchain settings.
- Prepare a wallets.json file (sample format below).
- Send a POST request to /api/start from your frontend or Postman.
- Check logs and outputs in /logs folder.

## API
- POST /api/start : <br>
Starts the automation process with uploaded wallets and parameters.

## Sample .env
```bash
RPC_URL=https://monad-testnet.rpc
TOKEN_IN_ADDRESS=0x...
TOKEN_OUT_ADDRESS=0x...
SWAP_ROUTER_ADDRESS=0x...
TELEGRAM_HANDLE=your_handle
TELEGRAM_GROUP_LINK=https://t.me/yourgroup
```
## Sample wallets.json
```bash
[
  { "address": "0x123...", "privateKey": "0xabc..." },
  { "address": "0x456...", "privateKey": "0xdef..." }
]
```

## Support
For questions, contact: <br>
<strong> MAK Online Solutions Pvt Ltd </strong>
📧 onkar@makonlinesolutions.com
