from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


driver.get("https://gmail.com")
driver.maximize_window()
driver.implicity_wait(10)
wait = WebDriverWait(driver, 10)

driver.find_element_by_id("identifierId").send_keys("alexanderbritcliffe@gmail.com")
driver.find_element_by_xpath("//*[@id=\"identifierNext\"]/div/button/div[2]").click()

wait.until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id=\"password\"]/div[1]/div/div[1]/input"))).send_keys("hello")


driver.find_element_by_xpath("//*[@id=\"passwordNext\"]/div/button/div[1]").click
error_msg = driver.find_element_by_xpath("//*[@id=\"view_container\"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]").text
print(error_msg)


