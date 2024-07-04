from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time
from random import randint


def wait(minim=300, maxim=600):
    time.sleep(randint(minim, maxim) / 100)


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up_speed = 0
        self.down_speed = 0
        self.SPEED_URL = "https://www.speedtest.net/"
        self.X_URL = "https://twitter.com/"
        self.X_USERNAME = os.environ.get("X_USERNAME")
        self.X_USER = os.environ.get("X_USER")
        self.X_PASSWORD = os.environ.get("X_PASSWORD")
        self.CONTRACT_UP_SPEED = 100
        self.CONTRACT_DOWN_SPEED = 100

    def get_internet_speed(self) -> None:
        self.driver.get(self.SPEED_URL)
        go_button = self.driver.find_element(By.XPATH,
                                             value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        go_button.click()
        time.sleep(60)
        self.up_speed = float(self.driver.find_element(By.XPATH, value="//*[@id='container']/div/div["
                                                                       "3]/div/div/div/div[2]/div[3]/div[3]/div/div["
                                                                       "3]/div/div/div[2]/div[1]/div[1]/div/div["
                                                                       "2]/span").text)

        self.down_speed = float(self.driver.find_element(By.XPATH, value="//*[@id='container']/div/div["
                                                                         "3]/div/div/div/div[2]/div[3]/div["
                                                                         "3]/div/div[3]/div/div/div[2]/div[1]/div["
                                                                         "2]/div/div[2]/span").text)

    def tweet_at_provider(self) -> None:
        if self.up_speed < self.CONTRACT_UP_SPEED or self.down_speed < self.CONTRACT_DOWN_SPEED:
            self.driver.get(self.X_URL)
            wait()
            x_signin = self.driver.find_element(By.XPATH, value="//*[@id='react-root']/div/div/div[2]/main/div/div/div["
                                                                "1]/div/div/div[3]/div[5]/a/div/span/span")
            x_signin.click()
            wait()
            for char in self.X_USERNAME:
                wait(minim=5, maxim=10)
                self.driver.find_element(By.XPATH, value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div["
                                                         "2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div["
                                                         "2]/div/input").send_keys(char)

            wait()
            next_button = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div[2]/div/div/div/div/div/div["
                                                                   "2]/div[2]/div/div/div[2]/div[2]/div/div/div/div["
                                                                   "6]/div")
            next_button.click()
            wait()
            for char in self.X_USER:
                wait(minim=5, maxim=10)
                self.driver.find_element(By.XPATH, value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div["
                                                         "2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div["
                                                         "2]/div/input").send_keys(char)
            wait()
            next_button2 = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div[2]/div/div/div/div/div/div["
                                                                    "2]/div[2]/div/div/div[2]/div[2]/div["
                                                                    "2]/div/div/div/div/div/span")
            next_button2.click()

            wait()
            for char in self.X_PASSWORD:
                wait(minim=5, maxim=10)
                self.driver.find_element(By.XPATH, value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div["
                                                         "2]/div/div/div[2]/div[2]/div[1]/div/div/div["
                                                         "3]/div/label/div/div[2]/div[1]/input").send_keys(char)
            wait()
            login_button = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div["
                                                                    "2]/div/div/div/div/div/div[2]/div["
                                                                    "2]/div/div/div[2]/div[2]/div[2]/div/div["
                                                                    "1]/div/div/div/div")
            login_button.click()
            wait()

            tweet = (
                f"Hey @TELMEXSoluciona ¿Por qué la velocidad de mi internet es {self.up_speed}/{self.down_speed} "
                f"cuando mi contrato especifica un mínimo de {self.CONTRACT_UP_SPEED}/{self.CONTRACT_DOWN_SPEED}?"
                )

            for char in tweet:
                wait(minim=5, maxim=10)
                try:
                    self.driver.find_element(By.XPATH, value="//*[@id='react-root']/div/div/div["
                                                             "2]/main/div/div/div/div/div/div["
                                                             "3]/div/div[2]/div[1]/div/div/div/div[2]/div["
                                                             "1]/div/div/div/div/div/div/div/div/div/div/label/div["
                                                             "1]/div/div/div/div/div/div[2]/div").send_keys(char)
                except NoSuchElementException:
                    self.driver.find_element(By.XPATH, value="//*[@id='react-root']/div/div/div["
                                                             "2]/main/div/div/div/div/div/div[3]/div/div[2]/div["
                                                             "1]/div/div/div/div[2]/div["
                                                             "1]/div/div/div/div/div/div/div/div/div/div/label/div["
                                                             "1]/div/div/div/div/div/div/div").send_keys(char)
            wait()
            post_button = self.driver.find_element(By.XPATH, value="//*[@id='react-root']/div/div/div["
                                                                   "2]/main/div/div/div/div/div/div[3]/div/div["
                                                                   "2]/div[1]/div/div/div/div[2]/div[2]/div["
                                                                   "2]/div/div/div/div[3]/div/span/span")
            post_button.click()
