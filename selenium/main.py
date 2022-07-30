from selenium import webdriver

from selenium.webdriver.common.by import By

chrome_driver_path= "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)



# driver.get("https://www.amazon.in/Apple-iPad-Air-10-9-inch-27-69-Wi-Fi/dp/B09V4D952H/ref=sr_1_3?crid=1OV71LNWFW4HE&keywords=ipad&qid=1659166470&sprefix=ipad%2Caps%2C320&sr=8-3&th=1")
# elem = driver.find_element(By.CLASS_NAME, 'a-price-whole')
# helper = elem.get_attribute("innerHTML").split("<")
# price = helper[0]

#------Challenge 1 ----------------#
# driver.get("https://www.cinemablend.com/new/upcoming-marvel-movies-release-dates-phase-4-67944.html")
# elem = driver.find_elements(By.TAG_NAME, "h2")

# movies_list = [movie.get_attribute("innerHTML") for movie in elem]
# print(movies_list)






# driver.close() #-----> only closes one tab
driver.quit() #------->closes whole browser