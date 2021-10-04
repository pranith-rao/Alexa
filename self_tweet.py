from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def account_info():
    with open('twitter_info.txt','r') as file:
        info = file.read().split()
        email = info[0]
        password = info[1]
    return email,password

def tweet(tweet):
    email,password = account_info()

    #tweet = "Hello World! Alex here.."

    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get("https://twitter.com/login")

    time.sleep(3)

    email_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
    next_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span'
    password_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input'
    loginbtn_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div'

    time.sleep(2)

    driver.find_element_by_xpath(email_xpath).send_keys(email)
    time.sleep(0.5)
    driver.find_element_by_xpath(next_xpath).click()
    time.sleep(2)
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    time.sleep(0.5)
    driver.find_element_by_xpath(loginbtn_xpath).click()

    tweetbtn_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
    textarea_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
    sendtweet_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span'

    time.sleep(2)

    driver.find_element_by_xpath(tweetbtn_xpath).click()
    time.sleep(0.5)
    driver.find_element_by_xpath(textarea_xpath).send_keys(tweet)
    time.sleep(0.5)
    driver.find_element_by_xpath(sendtweet_xpath).click()