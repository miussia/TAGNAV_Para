def startBrowser(name):
    """
    打开浏览器函数，"firefox"、"chrome"、"ie"、"phantomjs"
    """
    try:
        if name == "firefox" or name == "Firefox" or name == "ff":
            print("start browser name :Firefox")
            driver = webdriver.Firefox()
            return driver
        elif name == "chrome" or name == "Chrome":
            print("start browser name :Chrome")
            driver = webdriver.Chrome()
            return driver
        elif name == "ie" or name == "Ie":
            print("start browser name :Ie")
            driver = webdriver.Ie()
            return driver
        elif name == "phantomjs" or name == "Phantomjs":
            print("start browser name :phantomjs")
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("Not found this browser,You can use 'firefox', 'chrome', 'ie' or 'phantomjs'")
    except Exception as msg:
        print("启动浏览器出现异常：%s" % str(msg))
