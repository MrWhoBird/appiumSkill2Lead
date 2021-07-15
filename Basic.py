from appium import webdriver

desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "Pixel 3a",
    "app": ("C:/Users/hkaluza/PycharmProjects/AppiumFramework/Android_Appium_Demo.apk"),
    "appPackage": "com.skill2lead.appiumdemo",
    "appActivity": "com.skill2lead.appiumdemo.MainActivity",
    'adbExecTimeout': "20000"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

el = driver.find_element_by_id("com.skill2lead.appiumdemo:id/EnterValue")
el.click()