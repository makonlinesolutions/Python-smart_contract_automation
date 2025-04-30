from automation.approve import run_approve
from automation.swap import run_swap
from social.telegram import simulate_telegram
from social.twitter import simulate_twitter
from social.discord import simulate_discord
from utils.notifications import send_telegram, send_discord
import json
import os
import time
from datetime import datetime

def run_master():
    print("🚀 run_master.py started")

    payload_path = os.path.join(os.path.dirname(__file__), "../payloads/last-run.json")
    logs_path = os.path.join(os.path.dirname(__file__), "../logs")
    os.makedirs(logs_path, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_path = os.path.join(logs_path, f"run_{timestamp}.log")

    def log(message):
        print(message)
        with open(log_file_path, "a", encoding="utf-8") as f:
            f.write(message + "\n")

    # ✅ Load the payload file
    try:
        with open(payload_path, "r") as f:
            payload = json.load(f)
    except Exception as e:
        error_msg = f"❌ Failed to load last-run.json: {e}"
        log(error_msg)
        send_telegram(error_msg)
        send_discord(error_msg)
        return

    wallets = payload.get("wallets", [])
    wallet_count = int(payload.get("walletCount", len(wallets)))
    telegram_handle = payload.get("telegram")
    twitter_handle = payload.get("twitter")
    discord_handle = payload.get("discord")
    proxy = payload.get("proxy")

    log(f"Payload loaded: {payload}")
    log(f"Executing {wallet_count} wallet(s)\n")

    for index, wallet in enumerate(wallets[:wallet_count]):
        log(f"Wallet {index+1}: {wallet['address']}")
        try:
            run_approve(wallet)
            time.sleep(1)
            run_swap(wallet)
            time.sleep(1)

            # ✅ Social Simulation
            simulate_telegram(wallet, telegram_handle, proxy)
            simulate_twitter(wallet, twitter_handle, proxy)
            simulate_discord(wallet, discord_handle, proxy)

            msg = f"✅ Wallet {wallet['address']} — Approve, Swap & Social done."
            log(msg)
            send_telegram(msg)

        except Exception as e:
            err = f"❌ Error for {wallet['address']}: {e}"
            log(err)
            send_telegram(err)
            send_discord(err)

        log("")

    log("✅ Script finished.")
    send_telegram("✅ All wallets processed successfully.")

if __name__ == "__main__":
    run_master()
