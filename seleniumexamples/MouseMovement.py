from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install)

driver.get("http://www.way2automation.com/")
driver.maximize_window()
driver.implicity_wait(1)

menu = driver.find_element_by_xpath("//*[@id=\"menu-item-25091\"]/a")

action = ActionChains(driver)
action.move_to_element(menu).perform()

driver.find_element_by_xpath("//*[@id=\"menu-item-25092\"]/a").click()