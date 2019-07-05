# -*- coding: utf-8 -*-
import time, os,sys
sys.path.append('./BeautifulReport')
import unittest
from BeautifulReport import BeautifulReport
import multiprocessing
from tomorrow import threads

curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath,'test_case')
reportpath =os.path.join(curpath,'test_report')

now=time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
report_title = 'report'+now+".html"
desc='test selenium website report'

if not os.path.exists(casepath):
    print("folder 'test_case' is genarated, please put the test cases into it")
    os.mkdir(casepath)

if not os.path.exists(reportpath):os,mkdir(reportpath)

def add_case(case_path=casepath, rule='test*.py'):
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule,top_level_dir=None)
    return discover

@threads(3)
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename=report_title,description=desc, log_path = reportpath)
    


if __name__ == "__main__":
    cases = add_case()
    #print(cases)

    for i in cases:
        
        run(i)
        print(i)

