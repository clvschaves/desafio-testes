import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(params=['chrome'], scope='class')
def browser(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        browser = webdriver.Chrome(options=options)

    request.cls.browser = browser

    #return browser
    yield browser
    browser.close()
