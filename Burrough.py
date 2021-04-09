#importing automation software
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Change to synology path
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "Z:\\Burrough"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "path/to/chromedriver.exe"
driver = webdriver.Chrome(executable_path=r'C:\Selenium\chromedriver.exe', chrome_options=chromeOptions)

#Goes to teams website
driver.get('https://web.microsoftstream.com/user/d31d2b7c-417a-4ec1-800d-704ba40fdb86')
time.sleep(3)

#Logs in with Intern's credentials
search = driver.find_element_by_name('loginfmt')
search.send_keys('itintern1@theacademyofscholars.onmicrosoft.com')
search.send_keys(Keys.RETURN)
time.sleep(4)
find = driver.find_element_by_name('passwd')
find.send_keys('Xun55317')
find.send_keys(Keys.RETURN)
time.sleep(4)
yes = driver.find_element_by_id('idSIButton9')
yes.send_keys(Keys.RETURN)
time.sleep(10)

#Defines Main Code
def vids1():
    time.sleep(5)
    # Selects elipses
    no = driver.find_element_by_css_selector('body > div.ng-scope > div > div.ng-scope > user-page > section > div.list-container.new-list-page-style > div > div > user-video-results > video-results > div.row.column.row-size1.items-list.relativeposition > items-list > div > div.ng-scope.ng-isolate-scope > div:nth-child(1) > item > item > video-item > div > list-row > ng-transclude > list-cell.actions-column.ng-scope.ng-isolate-scope > div > div > ng-transclude > div > flex-drawer > div > div > span.ng-scope > button').click()
    time.sleep(3)
    # Selects download button
    download = driver.find_element_by_css_selector('body > div.ng-scope > div > div.ng-scope > user-page > section > div.list-container.new-list-page-style > div > div > user-video-results > video-results > div.row.column.row-size1.items-list.relativeposition > items-list > div > div.ng-scope.ng-isolate-scope > div:nth-child(1) > item > item > video-item > div > list-row > ng-transclude > list-cell.actions-column.ng-scope.ng-isolate-scope > div > div > ng-transclude > div > flex-drawer > div > div > ul > li:nth-child(4) > button > span').click()
    time.sleep(5)
    # Selects elipses again then delete and confirm
    no1 = driver.find_element_by_css_selector('body > div.ng-scope > div > div.ng-scope > user-page > section > div.list-container.new-list-page-style > div > div > user-video-results > video-results > div.row.column.row-size1.items-list.relativeposition > items-list > div > div.ng-scope.ng-isolate-scope > div:nth-child(1) > item > item > video-item > div > list-row > ng-transclude > list-cell.actions-column.ng-scope.ng-isolate-scope > div > div > ng-transclude > div > flex-drawer > div > div > span.ng-scope > button').click()
    time.sleep(3)
    delete = driver.find_element_by_css_selector('body > div.ng-scope > div > div.ng-scope > user-page > section > div.list-container.new-list-page-style > div > div > user-video-results > video-results > div.row.column.row-size1.items-list.relativeposition > items-list > div > div.ng-scope.ng-isolate-scope > div:nth-child(1) > item > item > video-item > div > list-row > ng-transclude > list-cell.actions-column.ng-scope.ng-isolate-scope > div > div > ng-transclude > div > flex-drawer > div > div > ul > li:nth-child(2) > button').click()
    time.sleep(3)
    delete2 = driver.find_element_by_css_selector('#ngdialog1 > div.ngdialog-content > div > div > div > div > div.right > button').click()
    time.sleep(3)
    driver.refresh()
    time.sleep(6)

#Iterates main code to custom settings
x = 3000
while (x > 0):
    time.sleep(5)
    vids1()
    time.sleep(5)
    vids1()
    time.sleep(5)
    vids1()
    time.sleep(100)
    x -= 1