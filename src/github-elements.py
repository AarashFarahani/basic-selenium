from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://github.com/AarashFarahani/basic-selenium")

def printText(filesName):
    for a in filesName:
        if(a.text):
            print(a.text)

filesName = driver.find_elements_by_css_selector("a.js-navigation-open")
printText(filesName)

print("************************************")

filesName = driver.find_elements_by_xpath("//a[contains(@class, 'js-navigation-open')]")
printText(filesName)

driver.quit()