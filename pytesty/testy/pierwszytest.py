from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")



desiredCapabilities = DesiredCapabilities.CHROME.copy()
chromeOptionsRemote = webdriver.ChromeOptions()
chromeOptionsRemote.add_argument("--start-maximized")
chromeOptionsRemote.add_argument("--disable-session-crashed-bubble")

initRemoteDriver = webdriver.Remote(options=chromeOptionsRemote, command_executor='http://localhost:4444/wd/hub/', desired_capabilities=desiredCapabilities)
print(initRemoteDriver.current_url)


#driver = webdriver.Firefox(executable_path=r"C:\geckodriver.exe")
#driver.maximize_window()
webdriver.get("https://www.duckduckgo.com")
webdriver.delete_all_cookies()
title = webdriver.title
print(title)
assert title == "DuckDuckGo — Prywatność — jeszcze prostsza.", "Tytuł nie zgadza się z " + title

wpisz = webdriver.find_element_by_id("search_form_input_homepage")
szukaj = webdriver.find_element_by_id("search_button_homepage")
wpisz.send_keys("pogoda Lublin")
szukaj.click()
webdriver.save_screenshot("screnshot.png")
#driver.close()