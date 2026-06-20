from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page(viewport={"width": 375, "height": 812}) # Mobile viewport
    page.goto('http://localhost:3000/speaking')
    page.wait_for_timeout(3000)
    page.screenshot(path='mobile_speaking.png')

    page_desktop = browser.new_page(viewport={"width": 1280, "height": 800})
    page_desktop.goto('http://localhost:3000/speaking')
    page_desktop.wait_for_timeout(3000)
    page_desktop.screenshot(path='desktop_speaking.png')

    browser.close()
