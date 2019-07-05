from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re,os
from page import Page

from xml.dom import minidom
from data.projectpath import ProjectPath
dom = minidom.parse(ProjectPath+'\\data\\info.xml')
root = dom.documentElement
usernames = dom.getElementsByTagName('username')
passwords = dom.getElementsByTagName('password')

class login(Page):
    url =''

    username_loc=(By.ID,'UserName')
    
    password_loc=(By.ID,'Password')
   
    submit_loc=(By.ID,'submitButton')
    

    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def click_login(self):
        self.find_element(*self.submit_loc).click()

    def click_ok(self):
        xf = self.find_element(*self.frame_loc)
        self.driver.switch_to.frame(xf)
        self.find_element(*self.ok_loc).click()

        

    def user_login(self,username=usernames[0].firstChild.data,password=passwords[0].firstChild.data):
        self.open()
        self.type_username(username)
        sleep(1)
        self.type_password(password)
        self.type_password(password)
        self.click_login()
        sleep(1)

    def confirm_caution(self):
        self.click_ok()
        sleep(3)

    error_hint_loc1 = (By.XPATH,"/html/body/div/div[1]/div[2]/form/div[1]/ul/li[1]")
    error_hint_loc2 = (By.XPATH,"/html/body/div/div[1]/div[2]/form/div[1]/ul/li[2]")
    error_hint_loc = (By.XPATH,"/html/body/div/div[1]/div[2]/form/div[1]/ul/li")
    success_loc = (By.XPATH,"/html/body/div[1]/span[1]")
    frame_loc=(By.XPATH,'//*[@class="designer-client-frame"]')
    ok_loc = (By.XPATH,"//button[@type='button']")
    
    

    def error_hint(self):
        return self.find_element(*self.error_hint_loc).text

    def error_hint1(self):
        return self.find_element(*self.error_hint_loc1).text

    def error_hint2(self):
        return self.find_element(*self.error_hint_loc2).text

    def login_success(self):
        return self.find_element(*self.success_loc).text
  
    
    
    
        
        

