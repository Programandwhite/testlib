from selenium import webdriver
path = r'/usr/local/bin/chromedriver'   #mac保存谷歌浏览器地址
def chrome_start(url):
    chrome = webdriver.Chrome(path)
    chrome.get(url)
    return  chrome
def chrome_end(driver):
    driver.quit()
