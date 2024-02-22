def test_check_title(browser):
    browser.get(browser.base_url)

    assert "Google" in browser.title
