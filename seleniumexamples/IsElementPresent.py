from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from seleniumm.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def is_element_present(id):
    try:
        driver.find_element_by_id(id)
        return True
    except NoSuchElementException:
        return False

def is_element_present(how, what):
    try:
         driver.find_element(by=how, value=what)
         return True
    except NoSuchElementException:
         return False

def is_element_present(how, what):
    if len(driver.find_elements(by=how, value=what)) == 0:
        return False
    else:
        return True



driver = webdriver.Chrome(executable_path=ChromeDriverManager().install)

driver.get("http://www.gmail.com/")
driver.maximize_window()
driver.implicity_wait(1)

print(driver.find_element_by_id("identifierId").is_displayed())
print(is_element_present("identifierId"))

print(is_element_present(By.ID, "identifierId"))
print(is_element_present(By.XPATH, "//*[@id='identifierId'"))


#this checks visibility not presence of an element