from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

studentID = "00000"
studentPW = "*****"
work_name = "工讀：地科系-勞僱型教學助理"
work_info = "協助教學"

driver = webdriver.Firefox()
driver.get("https://cis.ncu.edu.tw/HumanSys/")

# HumanSys login
login_button = driver.find_element_by_xpath("/html/body/header/nav/ul/li/a")
login_button.click()

# Portal login
account = driver.find_element_by_xpath('//*[@id="userid_input"]')
password = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/form/fieldset/div[2]/div/input")
submit_button = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div/form/fieldset/div[3]/div/button")

account.send_keys(studentID)
password.send_keys(studentPW)
submit_button.click()

# HumanSys home
driver.get("https://cis.ncu.edu.tw/HumanSys/student/stdSignIn")

# HumanSys sign in
table = driver.find_element_by_xpath('//*[@id="table1"]')
rows = table.find_elements_by_tag_name("tr")
try:
    for row in rows:
        cols = row.find_elements_by_tag_name("td")
        for col in cols:
            if col.text == work_name:
                a = cols[5].find_elements_by_tag_name("a")
                a[0].click()
except StaleElementReferenceException:
    pass

#  HumanSys work sign in
try:
    signin_button = driver.find_element_by_xpath('//*[@id="signin"]')
    signin_button.click()


except NoSuchElementException:
    info = driver.find_element_by_xpath('//*[@id="AttendWork"]')
    signout_button = driver.find_element_by_xpath('//*[@id="signout"]')
    info.send_keys(work_info)
    signout_button.click()
