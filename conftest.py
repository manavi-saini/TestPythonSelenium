import pytest


# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")

# @pytest.fixture(scope="class")
@pytest.fixture()
def test_setup(request):
    # global driver
    from selenium import webdriver

    # browser = request.config.getoption("--browser")

    # if browser == 'chrome':
    #     options = webdriver.ChromeOptions()
    #     options.add_experimental_option('useAutomationExtension', False)
    #     driver = webdriver.Chrome(options=options, executable_path="C:/KBData/PyCharm Projects/SeleniumPython/Webdrivers/chromedriver.exe")
    # elif browser == 'firefox':
    #     # Do nothing yet

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # For Headless Automation Test Run
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options,
                              executable_path="C:/KBData/PyCharmProjects/SeleniumPython/Webdrivers/chromedriver.exe")

    driver.set_page_load_timeout(10)
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
