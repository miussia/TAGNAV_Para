from time import sleep
from selenium import webdriver
import unittest, time, re, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import mytest,function
from page_obj.loginPage import login
from mytest import *
from selenium.webdriver.common.by import By
from xml.dom import minidom
from data.projectpath import ProjectPath
dom = minidom.parse(ProjectPath+'\\data\\info.xml')
#dom = minidom.parse('C:\\Project\\TAGNAV_para\\data\\info.xml')
root = dom.documentElement
usernames = dom.getElementsByTagName('username')
Chs=dom.getElementsByTagName('Chrome')
Ies=dom.getElementsByTagName('IE')
Ffs=dom.getElementsByTagName('Firefox')
Eds=dom.getElementsByTagName('Edge')
Ch=int(Chs[0].firstChild.data)
Ie=int(Ies[0].firstChild.data)
Ff=int(Ffs[0].firstChild.data)
Ed=int(Eds[0].firstChild.data)


unittest.skipIf(Ch==0,'skip')        
class loginTest_Chrome(Mytest):
    '''Test Login into NAV in chrome'''
    print(Ch,Ie,Ff,Ed,usernames[0])
    def user_login_verify(self,username='',password=''):
        '''function note'''
        login(self.driver).user_login(username,password)
    
    def test_login1(self):
        '''login with username,password empty'''
        self.user_login_verify()
        po=login(self.driver)
        try:
            print ("cuowutishi",(po.error_hint()),'woshitishijieshu')
            self.assertEqual(po.error_hint1(),'User name is required.')
            self.assertEqual(po.error_hint2(),'Password is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_pawd_empty.png')
       
    def test_login2(self):
        '''login with username empty'''
        self.user_login_verify(password='123')
        po=login(self.driver)
        try:
            self.assertEqual(po.error_hint1(),'User name is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_empty.png')
    
    def test_login3(self):
        '''login with password empty'''
        self.user_login_verify(username='123')
        po=login(self.driver)
        try:
            self.assertEqual(po.error_hint1(),'Password is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'pawd_empty.png')
    
    def test_login4(self):
        '''login with wrong username password'''
        self.user_login_verify(password='123',username='123')
        po=login(self.driver)
        try:
            self.assertEqual(po.error_hint1(),'The specified user name or password is not correct, or you do not have a valid user account in Dynamics 365 Business Central.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_pawd_wrong.png')

    def test_login5(self):
        '''login with correct username password'''
        self.user_login_verify(username='adnm',password='@dnm2012')
        po=login(self.driver)
        try:
            
            self.assertEqual(po.login_success(),'Dynamics 365 Business Central')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_pawd_correct.png')
        login(self.driver).confirm_caution()


    

@unittest.skipIf(Ie==0,'skip') 
class loginTest_IE(TFS_5555_ie):
    '''Test Login into NAV in ie'''    
    def user_login_verify(self,username='',password=''):
        '''function note'''
        login(self.driver).user_login(username,password)
    
    def test_login1(self):
        '''login with username,password empty'''
        self.user_login_verify()
        po=login(self.driver)
        
        try:
            self.assertEqual(po.error_hint1(),'User name is required.')
            self.assertEqual(po.error_hint2(),'Password is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_pawd_empty.png')

    def test_login2(self):
        '''login with username empty'''
        self.user_login_verify(password='123')
        po=login(self.driver)
        try:
            self.assertEqual(po.error_hint1(),'User name is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_empty.png')
    
    def test_login3(self):
        '''login with password empty'''
        self.user_login_verify(username='123')
        po=login(self.driver)
        
        try:
            self.assertEqual(po.error_hint1(),'Password is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'pawd_empty.png')
    
    def test_login4(self):
        '''login with wrong username password'''
        self.user_login_verify(password='123',username='123')
        po=login(self.driver)
        sleep(3)
        try:
            self.assertEqual(po.error_hint1(),'The specified user name or password is not correct, or you do not have a valid user account in Dynamics 365 Business Central.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_pawd_wrong.png')

    def test_login5(self):
        '''login with correct username password'''
        self.user_login_verify(username='adnm',password='@dnm2012')
        po=login(self.driver)
        sleep(3)
        try:
            
            self.assertEqual(po.login_success(),'Dynamics 365 Business Central')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_pawd_correct.png')
        login(self.driver).confirm_caution()
        
@unittest.skipIf (Ff==0,'skip') 
class loginTest_FF(L_5557_firefox):
    '''Test Login into NAV in firefox'''    
    def user_login_verify(self,username='',password=''):
        '''function note'''
        login(self.driver).user_login(username,password)
   
    def test_login1(self):
        '''login with username,password empty'''
        self.user_login_verify()
        po=login(self.driver)
        
        try:
            self.assertEqual(po.error_hint1(),'User name is required.')
            self.assertEqual(po.error_hint2(),'Password is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_pawd_empty.png')
        

    def test_login2(self):
        '''login with username empty'''
        self.user_login_verify(password='123')
        po=login(self.driver)
        try:
            self.assertEqual(po.error_hint1(),'User name is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_empty.png')
    
    def test_login3(self):
        '''login with password empty'''
        self.user_login_verify(username='123')
        po=login(self.driver)
        try:
            self.assertEqual(po.error_hint1(),'Password is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'pawd_empty.png')
    
    def test_login4(self):
        '''login with wrong username password'''
        self.user_login_verify(password='123',username='123')
        po=login(self.driver)
        sleep(30)
        try:
            self.assertEqual(po.error_hint1(),'The specified user name or password is not correct, or you do not have a valid user account in Dynamics 365 Business Central.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_pawd_wrong.png')

    def test_login5(self):
        '''login with correct username password'''
        self.user_login_verify(username='adnm',password='@dnm2012')
        po=login(self.driver)
        sleep(30)
        try:
            
            self.assertEqual(po.login_success(),'Dynamics 365 Business Central')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        login(self.driver).confirm_caution()
        function.insert_img(self.driver,'user_pawd_correct.png')

@unittest.skipIf (Ed==0,'skip') 
class loginTest_Edge(L_5558_edge):
    '''Test Login into NAV in edge'''
    
    def user_login_verify(self,username='',password=''):
        '''function note'''
        login(self.driver).user_login(username,password)

    def test_login1(self):
        '''login with username,password empty'''
        self.user_login_verify()
        po=login(self.driver)
        
        try:
            self.assertEqual(po.error_hint1(),'User name is required.')
            self.assertEqual(po.error_hint2(),'Password is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_pawd_empty.png')

    def test_login2(self):
        '''login with username empty'''
        self.user_login_verify(password='123')
        po=login(self.driver)
        try:
            self.assertEqual(po.error_hint1(),'User name is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_empty.png')
   
    def test_login3(self):
        '''login with password empty'''
        self.user_login_verify(username='123')
        po=login(self.driver)
        try:
            self.assertEqual(po.error_hint1(),'Password is required.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'pawd_empty.png')

    def test_login4(self):
        '''login with wrong username password'''
        self.user_login_verify(password='123',username='123')
        po=login(self.driver)
        sleep(5)
        try:
            self.assertEqual(po.error_hint1(),'The specified user name or password is not correct, or you do not have a valid user account in Dynamics 365 Business Central.')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        function.insert_img(self.driver,'user_pawd_wrong.png')

    def test_login5(self):
        '''login with correct username password'''
        self.user_login_verify(username='adnm',password='@dnm2012')
        po=login(self.driver)
        sleep(5)
        try:
            self.assertEqual(po.login_success(),'Dynamics 365 Business Central')
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        login(self.driver).confirm_caution()
        function.insert_img(self.driver,'user_pawd_correct.png')
            
if __name__ == "__main__":
    unittest.main()
    
   






