from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


driver.get("http//www.wikipedia.org/")
driver.maximize_window()
driver.implicity_wait(10)
wait = WebDriverWait(driver, 10)

dropdown = driver.find_element_by_id("searchLanguage")
select = Select(dropdown)

select.select_by_value("hi")

options = dropdown.find_elements_by_tag_name("option")

for option in options:
    print("Text is : ",option.text, "Lang is : "+option.get_attribute("lang"))

print("Total dropdown values are ", len(options))

print("-----Printing all links-------")

block = driver.find_element_by_xpath("//*[@id=\"www-wikipedia-org\"]/div[11]/div[3]")

links = block.find_elements_by_tag_name("a")

print("1st link is : ",block.find_elements_by_tag_name("a").__getitem__(0).text)

print(len(links))

for links in links:
    print("Text is : ",link.text," ---URL is : "+link.get_attribute("href"))