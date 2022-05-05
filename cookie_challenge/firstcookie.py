from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
from time import sleep

class FirstCookie:
    def __init__(self) -> None:
        self.firstround = 0
        self.driver = webdriver.Firefox()
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")

    def clicking(self, clickerzeit=20):
        self.cookie = self.driver.find_element(By.ID, "bigCookie")
        actual_time = time.time()
        while time.time() - actual_time < clickerzeit: 
            self.cookie.click()
        return False

    def clickerloop(self):
        if self.firstround == 1:
            upgrade = self.driver.find_element(By.ID, "upgrade0").get_attribute("class")
            if "enabled" in upgrade:
                clicker = self.driver.find_element(By.ID, "upgrade0")
                clicker.click()
        for i in range(18):
            element = self.driver.find_element(By.ID, f"product{17-i}").get_attribute("class")
                
            if "enabled" in element:
                clicker = self.driver.find_element(By.ID, f"product{17-i}")
                clicker.click()
                a = 1
                break
        self.firstround = 1


delay = 180



cookie = FirstCookie()
sleep (10)
now = time.time() + delay
while time.time() < now: 
    cookie.clicking(15)
    cookie.clickerloop()

print("Ready ")

