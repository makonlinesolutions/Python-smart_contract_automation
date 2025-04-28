from playwright.sync_api import sync_playwright
import os

def simulate_twitter(wallet, handle, proxy=None):
    print(f"🐦 Simulating Twitter for {wallet['address']} | Handle: {handle}")

    screenshot_dir = os.path.join(os.path.dirname(__file__), "../logs/screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    try:
        with sync_playwright() as p:
            browser_args = [f'--proxy-server={proxy}'] if proxy else []
            browser = p.chromium.launch(headless=True, args=browser_args)
            context = browser.new_context()
            page = context.new_page()

            if handle:
                page.goto(f"https://twitter.com/{handle}", timeout=60000)
                page.wait_for_timeout(3000)  # wait for content
                screenshot_path = os.path.join(screenshot_dir, f"twitter_{wallet['address']}.png")
                page.screenshot(path=screenshot_path)
                print(f"✅ Twitter page loaded and screenshot saved: {screenshot_path}")
            else:
                print("⚠️ No Twitter handle provided in payload.")

            context.close()
            browser.close()

    except Exception as e:
        print(f"❌ Twitter simulation failed for {wallet['address']}: {e}")
