from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os
from models.driver import browser


            

class Mytest(unittest.TestCase):
    def setUp(self):
        self.driver = browser.browser()        
        self.driver.implicitly_wait(30)        
        self.verificationErrors = []
        self.accept_next_alert = True 
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class L_5557_firefox(Mytest):
    def setUp(self):       
        self.driver = browser.browser_L_5557_firefox()
        self.driver.implicitly_wait(30)        
        self.verificationErrors = []
        self.accept_next_alert = True
        
class L_5558_edge(Mytest):
    def setUp(self): 
        self.driver = browser.browser_L_5558_edge()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        
class TFS_5555_ie(Mytest):
    def setUp(self):       
        self.driver = browser.browser_TFS_5555_ie()
        self.driver.implicitly_wait(30)        
        self.verificationErrors = []
        self.accept_next_alert = True

