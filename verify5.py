from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page(viewport={"width": 375, "height": 812})
    page.goto('http://localhost:3000/projects')
    page.wait_for_timeout(3000)
    # Scroll down to make sure projects are visible
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1000)
    page.screenshot(path='mobile_projects_scroll.png')

    page2 = browser.new_page(viewport={"width": 375, "height": 812})
    page2.goto('http://localhost:3000/speaking')
    page2.wait_for_timeout(3000)
    page2.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
    page2.wait_for_timeout(1000)
    page2.screenshot(path='mobile_speaking_scroll.png')

    browser.close()
