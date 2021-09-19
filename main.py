from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
SIMILAR_ACCOUNT = os.environ.get('SIMILAR_ACCOUNT')
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        cookie = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]')
        cookie.click()
        time.sleep(2)
        username = self.driver.find_element_by_name('username')
        username.send_keys(EMAIL)
        password = self.driver.find_element_by_name('password')
        password.send_keys(PASSWORD)
        login_b = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_b.click()

    def find_followings(self):
        time.sleep(5)
        search_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_input.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)
        search_click = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        search_click.click()
        time.sleep(2)
        followings_click = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        followings_click.click()
        time.sleep(5)
        scr1 = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(2)

    def follow(self):
        followings = self.driver.find_elements_by_css_selector('li button')
        for element in followings:
            time.sleep(3)
            try:
                element.click()
            except ElementClickInterceptedException:
                cancel_b = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_b.click()


instabot = InstaFollower()
instabot.login()
instabot.find_followings()
instabot.follow()
