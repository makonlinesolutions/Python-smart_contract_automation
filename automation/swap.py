from web3 import Web3
from utils.env_loader import RPC_URL, SWAP_ROUTER_ADDRESS, TOKEN_IN_ADDRESS, TOKEN_OUT_ADDRESS, SWAP_AMOUNT, GAS_FEE
import json

with open("abis/router_abi.json") as f:
    router_abi = json.load(f)

def run_swap(wallet):
    print(f"\n🔁 Performing token swap for wallet: {wallet['address']}")
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    acct = w3.eth.account.from_key(wallet['privateKey'])

    router = w3.eth.contract(address=Web3.to_checksum_address(SWAP_ROUTER_ADDRESS), abi=router_abi)

    txn = router.functions.swapExactTokensForTokens(
        w3.to_wei(SWAP_AMOUNT, 'ether'),
        0,
        [Web3.to_checksum_address(TOKEN_IN_ADDRESS), Web3.to_checksum_address(TOKEN_OUT_ADDRESS)],
        acct.address,
        w3.eth.get_block('latest')['timestamp'] + 1200
    ).build_transaction({
        'from': acct.address,
        'nonce': w3.eth.get_transaction_count(acct.address),
        'gas': 300000,
        'gasPrice': w3.to_wei((GAS_FEE), 'gwei')
    })

    signed_txn = acct.sign_transaction(txn)
    raw_tx = signed_txn.raw_transaction

    tx_hash = w3.eth.send_raw_transaction(raw_tx)
    print("✅ Swap Tx:", tx_hash.hex())