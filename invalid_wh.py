from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=<any empty directory to store user's data of browser")  #chrome configuration file path for user

driver = webdriver.Chrome(executable_path='<chrome driver file path>',options=options)
driver.get("https://web.whatsapp.com/send?phone=<invalid_number>&text=hi")

while(1):
    try:
        user = driver.find_element_by_class_name('_2fuxX').text
        print(user)
    except:
        print("************************")
        pass
