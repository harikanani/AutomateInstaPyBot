from selenium import webdriver
from time import sleep
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
        name=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a')
        name.click()
        self.driver.implicitly_wait(18)
        self.like()
    def like(self):
        self.driver.implicitly_wait(4)
        sleep(2)
        start = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]")
        
        a=0
        self.driver.execute_script('arguments['+str(a)+'].scrollIntoView()',start)
        
        for i in range(10):
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(3)
            pics=self.driver.find_elements_by_class_name("v1Nh3")
            sleep(1)
            for p in pics:
                if(a==0):
                    p.click()
                    self.driver.implicitly_wait(4)
                like=self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
                like.click()
                sleep(2)
                if(a==0):
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()
                else:
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
                a+=1
                print(a)

my_bot = InstaBot('##USERNAME HERE##','##PSWD##')
my_bot.go_home()