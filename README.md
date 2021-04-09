# python-pirate
Automate the world and become the king of pirates!
One step at a time ;)

# what is this?
This program utilizes the Selenium framework imported by Python to automate a simple process

# how to setup python
Install the latest version of python @ (https://www.python.org/downloads/)
Make sure you use custom installation and include pip
Save python on C:\ drive

# how to setup pycharm 
Install the latest version of pycharm @ (https://www.jetbrains.com/pycharm/)
![image](https://user-images.githubusercontent.com/74867958/114215938-3ca92800-9934-11eb-96c0-0490aef331d2.png)
Make sure you dont import settings and that the system interpretor is python from C drive

# how to setup selenium
Pip install selenium in pycharm terminal  
Download latest version of chromedriver from (https://sites.google.com/a/chromium.org/chromedriver/)
Save to C:\Selenium\chromedriver.exe (example)

# import automation software and get to conquering the grand line
from selenium import webdriver
browser = webdriver.Chrome(executable_path=r'C:\Selenium\chromedriver.exe')
browser.get(www.whateveryouwant.com)
