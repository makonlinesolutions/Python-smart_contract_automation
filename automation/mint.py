from web3 import Web3
from utils.env_loader import RPC_URL, MINT_CONTRACT_ADDRESS, MINT_AMOUNT, GAS_FEE
import json

with open("abis/token_abi.json") as f:
    mint_abi = json.load(f)

def run_mint(wallet):
    print(f"\n🪙 Minting token for wallet: {wallet['address']}")
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    acct = w3.eth.account.from_key(wallet['privateKey'])

    contract = w3.eth.contract(address=Web3.to_checksum_address(MINT_CONTRACT_ADDRESS), abi=mint_abi)

    txn = contract.functions.mint(
        acct.address,
        w3.to_wei(MINT_AMOUNT, 'ether')
    ).build_transaction({
        'from': acct.address,
        'nonce': w3.eth.get_transaction_count(acct.address),
        'gas': 200000,
        'gasPrice': w3.to_wei((GAS_FEE), 'gwei')
    })

    signed_txn = acct.sign_transaction(txn)
    raw_tx = signed_txn.raw_transaction

    tx_hash = w3.eth.send_raw_transaction(raw_tx)
    print("✅ Mint Tx:", tx_hash.hex())