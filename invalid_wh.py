from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=Home/bot/.config/chromium/Profile 1")  #chrome configuration file path for user

driver = webdriver.Chrome(executable_path='<chrome driver file path>',options=options)
driver.get("https://web.whatsapp.com/send?phone=<invalid_number>&text=hi")

while(1):
    try:
        user = driver.find_element_by_class_name('_2fuxX').text
        print(user)
    except:
        print("************************")
        pass
