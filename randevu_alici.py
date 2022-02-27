from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import schedule

def randevu_al():
    path = "C:\chromedriver.exe"
    driver = webdriver.Chrome(path)
    url = "https://sport.sabanciuniv.edu/reservation/new/4"
    driver.get(url)
    ka = driver.find_element_by_id("username")
    ka.send_keys("{username}")
    s = driver.find_element_by_id("password")
    s.send_keys("{password}")
    driver.find_element_by_name("submit").click()
    driver.get("https://sport.sabanciuniv.edu/reservation/add?area=121")
    general = "https://sport.sabanciuniv.edu/en/reservation/add?area="
    tbw = "reservation-202111251100"
    for element_num in [126,125,129,131,132,145,121,150,148,123,122,147,135,124,149,146,128,127,130,133,134]:
        if len(driver.find_elements(By.ID,tbw))== 0:
            time.sleep(1)
            driver.back()
            element_num += 1
            new = general+str(element_num)
            driver.get(new)
        else:
            driver.find_element_by_id(tbw).click()
            driver.find_element_by_name("formSubmit").click()
            driver.find_element_by_name("formConfirm").click()
            break

schedule.every().day.at("00:00").do(randevu_al)
schedule.every().day.at("00:01").do(randevu_al)

while True:
    schedule.run_pending()
    time.sleep(60)
    
