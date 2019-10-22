from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://github.com/AarashFarahani/basic-selenium")

def printText(contents):
    for a in contents:
        if(a.text):
            print(a.text)

contents = driver.find_elements_by_css_selector("a.js-navigation-open")
printText(contents)

print("************************************")

contents = driver.find_elements_by_xpath("//a[contains(@class, 'js-navigation-open')]")
printText(contents)

driver.quit()