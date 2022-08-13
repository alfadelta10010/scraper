from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import csv
print("Running")
opts = Options()
opts.headless = True
browser = Firefox(options=opts)
print("Browser running")
browser.get('https://pesuacademy.com')
sleep(5)
browser.find_element(By.ID, "knowClsSection").click()
f = open("freshers.csv", "a")
print("File created")
for i in range(1, 3000):
    browser.get('https://pesuacademy.com')
    sleep(3)
    browser.find_element(By.ID, "knowClsSection").click()
    inp = browser.find_element(By.ID, "knowClsSectionModalLoginId")
    if (i >= 1 and i <= 9):
        s = "000" + str(i)
    elif (i >= 10 and i <= 99):
        s = "00" + str(i)
    elif (i >= 100 and i <= 999):
        s = "0" + str(i)
    else:
        s = str(i)
    inputPRN = "PES220210" + s
    inp.send_keys(inputPRN)
    try:
        browser.find_element(By.ID, "knowClsSectionModalSearch").click()
        sleep(3)
        prn = browser.find_element(By.XPATH, "//*[@id='knowClsSectionModalTableDate']/tr/td[1]").text
        srn = browser.find_element(By.XPATH, "//*[@id='knowClsSectionModalTableDate']/tr/td[2]").text
        semValue = browser.find_element(By.XPATH, "//*[@id='knowClsSectionModalTableDate']/tr/td[4]").text
        section = browser.find_element(By.XPATH, "//*[@id='knowClsSectionModalTableDate']/tr/td[5]").text
        cycle = browser.find_element(By.XPATH, "//*[@id='knowClsSectionModalTableDate']/tr/td[6]").text
        strCamp = browser.find_element(By.XPATH, "//*[@id='knowClsSectionModalTableDate']/tr/td[7]").text
        stream = browser.find_element(By.XPATH, "//*[@id='knowClsSectionModalTableDate']/tr/td[8]").text
        campus = browser.find_element(By.XPATH, "//*[@id='knowClsSectionModalTableDate']/tr/td[9]").text
        strRow = prn + "," + srn + "," + semValue + "," + section + "," + cycle + "," + strCamp + "," + stream + "," + campus
        print("Got for", prn)
        f.write(strRow + "\n")
    except:
        print(inputPRN, "error")
f.close()
print("File closed")
browser.close()
print("Browser closed")
