import os
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


login = input("ETRADE Login: ")
password = getpass.getpass("ETRADE Password: ")

options = webdriver.FirefoxOptions()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", os.path.abspath("."))
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")
options.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(options=options)

driver.get("https://us.etrade.com/home/welcome-back")

login_box = driver.find_element_by_name("USER")
password_box = driver.find_element_by_name("PASSWORD")

login_box.send_keys(login)
password_box.send_keys(password)
password_box.send_keys(Keys.RETURN)


element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "application"))
)


driver.get("https://us.etrade.com/etx/pxy/tax-center?resource=stock-plan")

download_links = driver.find_elements_by_class_name("btn-link")

for link in download_links:
    if link.text == "get_appDownload PDF":
        link.click()

driver.close()
