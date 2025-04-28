from dotenv import load_dotenv
import os

load_dotenv()

# Blockchain config
RPC_URL = os.getenv("RPC_URL")

# Token Approve config
TOKEN_ADDRESS = os.getenv("TOKEN_ADDRESS")
print("✅ Final TOKEN_ADDRESS loaded:", repr(TOKEN_ADDRESS))
SPENDER_ADDRESS = os.getenv("SPENDER_ADDRESS")
APPROVE_AMOUNT = float(os.getenv("APPROVE_AMOUNT", "1000000"))

# Swap config
SWAP_ROUTER_ADDRESS = os.getenv("SWAP_ROUTER_ADDRESS")
TOKEN_IN_ADDRESS = os.getenv("TOKEN_IN_ADDRESS")
TOKEN_OUT_ADDRESS = os.getenv("TOKEN_OUT_ADDRESS")
SWAP_AMOUNT = float(os.getenv("SWAP_AMOUNT", "0.01"))

# ✅ Add this line for liquidity and Gas Fee
LIQUIDITY_AMOUNT = float(os.getenv("LIQUIDITY_AMOUNT", "0.01"))
GAS_FEE = float(os.getenv("GAS_FEE","100"))

# Mint config
MINT_CONTRACT_ADDRESS = os.getenv("MINT_CONTRACT_ADDRESS")
MINT_AMOUNT = float(os.getenv("MINT_AMOUNT", "50"))

#Dry Run setup
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"

#Sociel Media Code
DISCORD_CODE = os.getenv("DISCORD_CODE")
TELEGRAM_CODE = os.getenv("TELEGRAM_CODE")
TWITTER_CODE = os.getenv("TWITTER_CODE")


