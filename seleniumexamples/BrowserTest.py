from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


driver.get("http://way2automation.com")

driver.maximize_window()

title = driver.title

print(title)