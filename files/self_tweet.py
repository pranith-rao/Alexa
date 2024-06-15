from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def account_info():
    with open('./twitter_info.txt','r') as file:
        info = file.read().split()
        email = info[0]
        password = info[1]
    return email,password

def tweet(tweet):
    email,password = account_info()

   #tweet = "Hello World! Alex here.."

    options = Options()
    options.use_chromium = True
    options.add_argument("start-maximized")
    options.add_argument("--disable-notifications")
    driver = webdriver.Edge(executable_path=r"..\\drivers\\msedgedriver.exe")

    driver.get("https://twitter.com/login")

    time.sleep(3)

    email_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
    next_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]'
    password_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
    loginbtn_xpath = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button'

    time.sleep(2)

    driver.find_element_by_xpath(email_xpath).send_keys(email)
    time.sleep(0.5)
    driver.find_element_by_xpath(next_xpath).click()
    time.sleep(2)
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    time.sleep(0.5)
    driver.find_element_by_xpath(loginbtn_xpath).click()

    tweetbtn_xpath = '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
    textarea_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div'
    sendtweet_xpath = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button'

    time.sleep(2)

    driver.find_element_by_xpath(tweetbtn_xpath).click()
    time.sleep(0.5)
    driver.find_element_by_xpath(textarea_xpath).send_keys(tweet)
    time.sleep(0.5)
    driver.find_element_by_xpath(sendtweet_xpath).click()