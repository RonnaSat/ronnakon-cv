from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page(viewport={"width": 375, "height": 812}) # Mobile viewport
    page.goto('http://localhost:3000/projects')
    page.wait_for_selector('h3')
    page.screenshot(path='mobile_projects.png')

    page_desktop = browser.new_page(viewport={"width": 1280, "height": 800})
    page_desktop.goto('http://localhost:3000/projects')
    page_desktop.wait_for_selector('h3')
    page_desktop.screenshot(path='desktop_projects.png')

    browser.close()
