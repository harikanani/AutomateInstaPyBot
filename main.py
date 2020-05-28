from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time
import sys
import  random

class InstagramBot() :
    def __init__(self,username,password):
        self.username = 'username'
        self.password = 'password'
        self.driver = webdriver.Chrome("C:\\webdriver\\chromedriver.exe")

    def closeBrowser(self):
        self.driver.close()

    def Login(self):
        driver = self.driver
        driver.get("https://instagram.com")
        time.sleep(2)

        login_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')

        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.send_keys(self.username)

        time.sleep(2)

        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.ENTER)
        time.sleep(3)

        # login_button.click()

        time.sleep(5)

        not_now = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        not_now.click()

    def FollowWithUsername(self,username):
        self.driver.get('https://www.instagram.com/' + username + '/')

        time.sleep(3)

        follow_button = self.driver.find_element_by_css_selector('button')
        if(follow_button.text != 'Following') :
            follow_button.click()
            time.sleep(2)
        else :
            print('Already Following' + username)
        self.driver.back()
        time.sleep(2)



    def UnFollowWithUsername(self,username):
        self.driver.get('https://www.instagram.com/' + username + '/')

        time.sleep(3)

        follow_button = self.driver.find_element_by_css_selector('button')
        if(follow_button.text == 'Following') :
            follow_button.click()
            time.sleep(2)
        else :
            print('You are Not Following' + username)
        self.driver.back()
        time.sleep(2)


    def SelectProfile(self):
        my_profile = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img')
        my_profile.click()

    def RemoveProfilePicture(self):
        self.SelectProfile()
        ProfilePic = self.driver.find_element_by_class_name('be6sR')
        ProfilePic.click()

        RemovePic_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[2]')
        RemovePic_button.click()
        time.sleep(2)


    def selectUserProfile(self,username):
        selectProfile = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/button/span')
        selectProfile.click()

    def WriteUserName(self,username):
        to_btn = self.driver.find_element_by_name('queryBox')
        to_btn.send_keys(username)
        time.sleep(2)

    def NextClick(self):
        nxt_btn = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div/button")
        nxt_btn.click()
        time.sleep(2)

    def TextMessage(self, user):
        msg = 'Hey, There! @' + user + '. How are you?' + ' This is AutomatedBot Messages.'
        txt_box = self.driver.find_element_by_tag_name('textarea')
        txt_box.send_keys(msg)
        txt_box.send_keys(Keys.ENTER)
        time.sleep(1)

    def send_message(self, usernames, message):

        for usr in usernames :
            print(usr)
            self.driver.get('https://instagram.com/direct/new/')
            time.sleep(3)
            self.WriteUserName(usr)
            self.selectUserProfile(usr)
            self.NextClick()
            self.TextMessage(usr)


        # chk_mrk = self.driver.find_element_by_class_name('dCJp8')
        # chk_mrk.click()
        # time.sleep(3)


        # snd_btn = self.driver.find_element_by_tag_name('button')
        # snd_btn = snd_btn.__getitem__(3)
        # snd_btn.click()
        # time.sleep(3)

        # count = 0;
        # try :
        #     for username in usernames:
        #         self.WriteUserName(usernames)
        #         self.selectUserProfile(usernames)
        #         time.sleep(1)
        #         message = 'Hii, There! ' + username + '.' + 'This is AutomatedBot Messages.'
        #         self.send_msg(username,message)
        #         count += 1
        # except TypeError:
        #     print('Failed')

        # -------------- ************** Here is my Stuff ******************** -----------------

        # # NotSeenChat = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[2]/a/svg/path')
        # NotSeenChat.click()
        #
        # textArea = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        # textArea.click()
        # textArea.send_keys('Hii There!!')
        # textArea.send_keys(Keys.ENTER)


username = 'username'
password = 'password'

myUsernames = ['username_1', 'username_2', 'username_3', 'username_4', 'username_5']
myMessage = 'Hii, There! this is AutomatedBot Message.'

ig = InstagramBot(username, password)
ig.Login()
time.sleep(2)
ig.UnFollowWithUsername('username')
time.sleep(2)
ig.FollowWithUsername('username')
time.sleep(2)
ig.send_message(myUsernames, myMessage)
time.sleep(2)
ig.closeBrowser()
