from selenium import webdriver
import time
import xlsxwriter

#Connecting Google chrome to work with our Script
PATH = "/opt/homebrew/bin/chromedriver"

driver = webdriver.Chrome(PATH)

#directing to the desired website
link = "https://www.flipkart.com/mobiles/pr?sid=tyy,4io&marketplace=FLIPKART"
driver.get(link)
time.sleep(5)


#scraping the desired data from first 2 pages
for i in range(2):
    time.sleep(2)
    product = driver.find_elements_by_class_name("_4rR01T")
    for name in product:
        print(name.text)

    price = driver.find_elements_by_class_name("_1_WHN1")
    for cost in price:
        print(cost.text)
        
    time.sleep(2)

    element = driver.find_element_by_class_name("_1LKTO3")
    element.click()


#closing our program and Chrome driver
print("Workdone and successfully scraped")
driver.quit()

