from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install)

driver.get("https://jqueryui.com/resources/demos/dropable/default.html")
driver.maximize_window()
driver.implicity_wait(1)

draggable = driver.find_elements_by_i("draggable")
droppable = driver.find_elements_by_i("droppable")


ActionChains(driver).drag_and_drop(draggable, droppable).perform()

