from playwright.sync_api import sync_playwright
import os

def simulate_telegram(wallet, group_link, proxy=None):
    print(f"📲 Simulating Telegram for {wallet['address']} | Group: {group_link}")

    screenshot_dir = os.path.join(os.path.dirname(__file__), "../logs/screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    try:
        with sync_playwright() as p:
            browser_args = [f'--proxy-server={proxy}'] if proxy else []
            browser = p.chromium.launch(headless=True, args=browser_args)
            context = browser.new_context()
            page = context.new_page()

            if group_link:
                page.goto(group_link, timeout=60000)
                page.wait_for_timeout(3000)  # wait for page load
                screenshot_path = os.path.join(screenshot_dir, f"telegram_{wallet['address']}.png")
                page.screenshot(path=screenshot_path)
                print(f"✅ Telegram page loaded and screenshot saved: {screenshot_path}")
            else:
                print("⚠️ No Telegram group link provided in payload.")

            context.close()
            browser.close()

    except Exception as e:
        print(f"❌ Telegram simulation failed for {wallet['address']}: {e}")
