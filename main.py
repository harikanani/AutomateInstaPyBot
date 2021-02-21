from selenium import webdriver
from time import sleep
import pyautogui

class InstaBot:
    def __init__(self,username,pwd):
        # CHANGE THE LOCATION OF CHROMEDRIVER BELOW #
        self.driver=webdriver.Chrome("D:\chromedriver\chromedriver.exe")        
        self.username=username

        self.driver.get("https://instagram.com")
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pwd)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
    

    def go_home(self):
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a")\
        .click()
        sleep(3)
        self.search = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        self.search.send_keys("###PROFILE TO LIKE POSTS####")
        self.driver.implicitly_wait(3)
        name=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        name.click()
        
    def like(self):
        sleep(2)
        driver=self.driver
        driver.find_element_by_class_name("v1Nh3").click()  # To select the post

        i=1
        number=10 # No of posts to be liked
        like="True"
        action='Like' if like else 'Unlike'
        while i<=number:
            sleep(1)
            driver.find_element_by_class_name("fr66n").click() #like a posts
            sleep(1)
            driver.find_element_by_xpath("//*[@aria-label='{}']".format(action)).click() #To check post like or unlike 
            driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click() #Go to next post
            sleep(1)
            i=i+1 
        
    def autoliker(self,num):
        self.driver.get("https://www.instagram.com/")
        sleep(3)
        pyautogui.moveTo(625,657)
        for i in range(num):
            sleep(1)
            pyautogui.click()
            pyautogui.click()
            pyautogui.scroll(-800) 
            sleep(1)
    
my_bot = InstaBot('coder.602','adventure')
my_bot.go_home()
my_bot.like()
num=30 # Likes 15 images
my_bot.autoliker(num)
