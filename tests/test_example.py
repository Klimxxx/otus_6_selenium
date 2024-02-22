def test_check_title(browser):
    browser.get(browser.base_url)

    assert "OpenCart" in browser.title
