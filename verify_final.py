from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()

    # Projects page
    page = browser.new_page(viewport={"width": 375, "height": 812})
    page.goto('http://localhost:3000/projects')
    page.wait_for_timeout(3000)
    page.screenshot(path='mobile_projects_fixed.png')

    page_desktop = browser.new_page(viewport={"width": 1280, "height": 800})
    page_desktop.goto('http://localhost:3000/projects')
    page_desktop.wait_for_timeout(3000)
    page_desktop.screenshot(path='desktop_projects_fixed.png')

    # Speaking page
    page2 = browser.new_page(viewport={"width": 375, "height": 812})
    page2.goto('http://localhost:3000/speaking')
    page2.wait_for_timeout(3000)
    page2.screenshot(path='mobile_speaking_fixed.png')

    page_desktop2 = browser.new_page(viewport={"width": 1280, "height": 800})
    page_desktop2.goto('http://localhost:3000/speaking')
    page_desktop2.wait_for_timeout(3000)
    page_desktop2.screenshot(path='desktop_speaking_fixed.png')

    browser.close()
