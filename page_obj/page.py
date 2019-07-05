from xml.dom import minidom

from data.projectpath import ProjectPath



class Page(object):
    dom = minidom.parse(ProjectPath+'\\data\\info.xml')
    root = dom.documentElement
    urls = dom.getElementsByTagName('url')
    login_url = urls[0].firstChild.data
    #login_url = 'http://bc-extensions.adnm.net:82/NAV/'
    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url=base_url
        self.driver=selenium_driver
        self.timeout=30

    def on_page(self):
        print(self.driver.current_url)
        print(self.base_url+self.url)
        return (self.base_url+self.url) in self.driver.current_url

    def _open(self,url):
        url = self.base_url +url
        self.driver.get(url)
        url1=self.driver.current_url
        assert self.on_page(),"curren url is %s,Did not land on %s" %url1 %url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


