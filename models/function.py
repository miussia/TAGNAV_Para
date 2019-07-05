from selenium import webdriver
import os
import time

def insert_img(driver, file_name):
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    file_name = now+ file_name
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    #base = base_dir.split('/RemoteTest')[0]
    file_path =  base_dir + '/test_report/image/'+file_name
    driver.get_screenshot_as_file(file_path)
    

if __name__== '__main__':
    driver= webdriver.Chrome()
    driver.get('https://baidu.com')
    insert_img(driver,"baidu.png")
    driver.quit()
