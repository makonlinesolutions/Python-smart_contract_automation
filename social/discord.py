from playwright.sync_api import sync_playwright
import os

def simulate_discord(wallet, invite_code, proxy=None):
    print(f"🎮 Simulating Discord for {wallet['address']} | Invite: {invite_code}")

    screenshot_dir = os.path.join(os.path.dirname(__file__), "../logs/screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    try:
        with sync_playwright() as p:
            browser_args = [f'--proxy-server={proxy}'] if proxy else []
            browser = p.chromium.launch(headless=True, args=browser_args)
            context = browser.new_context()
            page = context.new_page()

            if invite_code:
                page.goto(f"https://discord.com/invite/{invite_code}", timeout=60000)
                page.wait_for_timeout(3000)
                screenshot_path = os.path.join(screenshot_dir, f"discord_{wallet['address']}.png")
                page.screenshot(path=screenshot_path)
                print(f"✅ Discord invite page loaded and screenshot saved: {screenshot_path}")
            else:
                print("⚠️ No Discord invite code provided in payload.")

            context.close()
            browser.close()

    except Exception as e:
        print(f"❌ Discord simulation failed for {wallet['address']}: {e}")
