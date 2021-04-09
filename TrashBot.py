#importing automation software
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r'C:\Selenium\chromedriver.exe', chrome_options=chromeOptions)

#Goes to teams website
driver.get('https://web.microsoftstream.com/admin?view=RecycleBin')
time.sleep(3)

#Logs in with Elijah's credentials
search = driver.find_element_by_name('loginfmt')
search.send_keys('itintern1@theacademyofscholars.onmicrosoft.com')
search.send_keys(Keys.RETURN)
time.sleep(4)
find = driver.find_element_by_name('passwd')
find.send_keys('Xun55317')
find.send_keys(Keys.RETURN)
time.sleep(5)
yes = driver.find_element_by_id('idSIButton9')
yes.send_keys(Keys.RETURN)
time.sleep(10)

#Defines emptying the recycling bin
def TrashBot():
    time.sleep(2)
    delete = driver.find_element_by_css_selector('body > div.ng-scope > div > div.ng-scope > admin-setting-detail > div > section > div > div.tab-page > recycle-bin > div > recycle-bin-list > div.row.column.row-size1.items-list.recycle-bin-list.relativeposition > items-list > div > div.ng-scope.ng-isolate-scope > div:nth-child(1) > item > recycle-bin-video-item > div > list-row > ng-transclude > list-cell.actions-column.ng-scope.ng-isolate-scope > div > div > ng-transclude > button.delete-button.c-action-trigger.ng-scope.ng-isolate-scope').click()
    time.sleep(2)
    confirm = driver.find_element_by_css_selector('#ngdialog1 > div.ngdialog-content > div > div > div > div > button.stream-btn.btn-primary.dialog-confirm-button.ng-binding.ng-scope').click()
    driver.refresh()
    time.sleep(3)

#Executes Bot
x = 3000
while (x > 0):
    time.sleep(1)
    TrashBot()
    time.sleep(1)

