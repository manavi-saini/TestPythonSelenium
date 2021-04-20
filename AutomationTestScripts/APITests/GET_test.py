from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


def test_get_log():
    log = get_perf_log_on_load()
    for l in log:
        print(l)


def get_perf_log_on_load(headless=True, filter=None):
    # init Chrome driver (Selenium)
    options = Options()
    options.headless = headless
    cap = DesiredCapabilities.CHROME
    cap['goog:loggingPrefs'] = {'performance': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=cap, options=options, executable_path="C:/KBData/PyCharmProjects/PythonSeleniumFrame/Webdrivers/chromedriver.exe")

    # record and parse performance log
    driver.get("https://www.test.retrofit.bendix.knorr-bremse.com/")
    if filter:
        log = [item for item in driver.get_log('performance')
               if filter in str(item)]
    else:
        log = driver.get_log('performance')
    driver.close()

    return log
