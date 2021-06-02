from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import gspread
import urllib

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=<any empty directory to store user's data of browser>")

gc = gspread.service_account(filename= "<Google sheets credential.json file>")
sheet = gc.open_by_key('gogle sheet key from url').worksheet("Sheet number")
row = 1
link = "https://web.whatsapp.com/send?phone=%s&text=%s"
def string(data):
    i=1
    data1 = ""
    while(1):
        if data[i]=='"':
            break
        data1 = data1 + data[i]
        i+=1
    return data1 

with open('<message.txt file>', 'r') as f:
    msg = f.read()
while(1):
    if row== #<max row count in sheet>:
        break
    time.sleep(1)
    try:
        ph_no = "+91" + string(sheet.cell(row,4).value)
        name = string(sheet.cell(row,2).value)
        msg1 = "*hello " + name + "*" + "\r\n" + msg
        print(ph_no)
        ack_url = urllib.parse.quote(msg1, safe='')
        url = link%(ph_no, ack_url)
        try:
            driver = webdriver.Chrome(executable_path='<chrome driver file path>',options=options)
            driver.get(url)
            date1 = datetime.datetime.today()
            while(True):
                try:
                    user = driver.find_element_by_class_name('_2fuxX').text
                    if(not(len(user)==0)):
                        row+=1
                        driver.close()
                        break
                except:
                    pass
                try:
                    driver.find_element_by_css_selector('._2Ujuu').click()
                    print("sent to %s"%(name))
                    while(1):
                        try:
                            sheet.update_cell(row,6, "pdf")
                            with open('<txt file to save the updated count>', 'w') as f:
                                f.write(str(row))
                            row+=1
                            break
                        except:
                            print("problem updating sheets.....retrying")
                    break        

                except:
                    print("page still loading")

                    
        except:
            print("problem loading whatsapp...reloading")
        time.sleep(3)
        driver.close()     
    except:
        print("problem with sheets...retrying")

    
            

