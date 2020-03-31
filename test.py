from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '127.0.0.1:62001 device'
desired_caps['appPackage'] = 'com.yingying.yingyingnews'
desired_caps['appActivity'] = '.ui.SplashActivity'
#desired_caps['noReset'] = 'True'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
driver.find_element_by_xpath('''/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]
''').click()
driver.implicitly_wait(10)
driver.find_element_by_id('com.yingying.yingyingnews:id/rb_mine').click()