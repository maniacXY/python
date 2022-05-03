# Upgrades: id=upgrade0 -> class="crate upgrade enabled"
# max products: product17 -> class="product locked disabeled/enabled"
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
from time import sleep
  
class FirstCookie:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        
    def clicking(self,zeit):
        self.cookie = self.driver.find_element(By.ID, "bigCookie")
        actual_time = time.time()
        while time.time() - actual_time < zeit: 
            self.cookie.click()
        return False

    def clickerloop(self, zeit_between_upgrades):
        
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        sleep(3)
        a = 0
        while True:
            if self.clicking(zeit_between_upgrades) == False:
                if a == 1:
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
                        
                    else:
                        continue
    