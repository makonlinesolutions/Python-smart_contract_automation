from web3 import Web3
from utils.env_loader import RPC_URL, TOKEN_ADDRESS, SPENDER_ADDRESS, APPROVE_AMOUNT, GAS_FEE
import json

with open("abis/token_abi.json") as f:
    token_abi = json.load(f)

def run_approve(wallet):
    print(f"\n🟡 Approving token for wallet: {wallet['address']}")
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    acct = w3.eth.account.from_key(wallet['privateKey'])

    contract = w3.eth.contract(address=Web3.to_checksum_address(TOKEN_ADDRESS), abi=token_abi)

    txn = contract.functions.approve(
        Web3.to_checksum_address(SPENDER_ADDRESS),
        w3.to_wei((APPROVE_AMOUNT), 'gwei')
    ).build_transaction({
        'from': acct.address,
        'nonce': w3.eth.get_transaction_count(acct.address),
        'gas': 200000,
        'gasPrice': w3.to_wei((GAS_FEE), 'gwei')
    })

    signed_txn = acct.sign_transaction(txn)
    raw_tx = signed_txn.raw_transaction

    tx_hash = w3.eth.send_raw_transaction(raw_tx)
    print("✅ Approve Tx:", tx_hash.hex())