from selenium.webdriver import Remote
from selenium import webdriver
class browser():
    
    def browser():
        lists = {'http://127.0.0.1:5556/wd/hub':'chrome'}
        
        for host, browser in lists.items():
            print(host, browser)
            driver= Remote(command_executor=host,
                        desired_capabilities={'platform':'ANY',
                                              'browserName':browser,
                                              'version':'',
                                              'javascriptEnabled':True
                                              }
                        )

    
        return driver

    def browser_L_5556_chrome():
        lists = {'http://127.0.0.1:5556/wd/hub':'chrome'}
        
        for host, browser in lists.items():
            print(host, browser)
            driver= Remote(command_executor=host,
                        desired_capabilities={'platform':'ANY',
                                              'browserName':browser,
                                              'version':'',
                                              'javascriptEnabled':True
                                              }
                        )

        
        return driver
    
    def browser_L_5557_firefox():
        lists = {'http://127.0.0.1:5557/wd/hub':'firefox'}
        
        for host, browser in lists.items():
            print(host, browser)
            driver= Remote(command_executor=host,
                        desired_capabilities={'platform':'ANY',
                                              'browserName':browser,
                                              'version':'',
                                              'javascriptEnabled':True
                                              }
                        )

        
        return driver
    
    def browser_TFS_5555_ie():
        lists = {'http://10.0.0.132:5555/wd/hub':'internet explorer'}
        
        for host, browser in lists.items():
            print(host, browser)
            driver= Remote(command_executor=host,
                        desired_capabilities={'platform':'ANY',
                                              'browserName':browser,
                                              'version':'',
                                              'javascriptEnabled':True
                                              }
                        )

        
        return driver
    
    def browser_L_5558_edge():
        lists = {'http://127.0.0.1:5558/wd/hub':'MicrosoftEdge'}
        
        for host, browser in lists.items():
            print(host, browser)
            driver= Remote(command_executor=host,
                        desired_capabilities={'platform':'ANY',
                                              'browserName':browser,
                                              'version':'',
                                              'javascriptEnabled':True
                                              }
                        )

        
        return driver
    
if __name__== '__main__':
    dr = browser.browser()
    dr.get('http://bc-extensions.adnm.net:82/NAV')
    dr.quit()

