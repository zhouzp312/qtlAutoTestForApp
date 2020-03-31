from appium import webdriver
import time
import pytest
desired_caps = {
    'platformName':'android',
     #用真机的时候，这个参数deviceName没什么用，但是还是必须要有这个参数，值的话随便填就行了
    'deviceName':'127.0.0.1:7555',
    'platformVersion':'6.0.1',
    'appPackage':'com.yingying.yingyingnews',
    'appActivity':'.ui.SplashActivity',
    'unid':'127.0.0.1:7555',
    'noReset':'True',
    'automationName':'UiAutomator2'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(3)
driver.quit()

if __name__ == '__main__':
    pytest.main(["-s"])