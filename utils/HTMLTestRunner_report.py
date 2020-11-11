#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: HTMLTestRunner_report.py
# @time: 2020-11-11 12:48
# @desc:
import HTMLTestRunner
import unittest, os, time
from utils.read_conf import read_conf

case_path_01 = os.path.join(os.path.dirname(__file__), '..', read_conf.get_conf_case_path)
report_path_01 = os.path.join(os.path.dirname(__file__), '..', read_conf.get_conf_report_path, '接口自动化测试报告_%s.html') % time.strftime('%Y%m%d_%H%M%S')
report_title_01 = '接口自动化标题'
report_description_01 = '接口自动化描述'


class HtmlTestRunner:
    def __init__(self, pattern, case_path=case_path_01):
        self.case_path = case_path
        self.pattern = pattern
        self.discover = unittest.defaultTestLoader.discover(start_dir=self.case_path, pattern=self.pattern,
                                                            top_level_dir=self.case_path)

    def html_test_runner(self, report_path=report_path_01, report_title=report_title_01,
                         report_description=report_description_01):
        file = open(report_path, 'w', encoding='utf-8')
        html_runner = HTMLTestRunner.HTMLTestRunner(stream=file, title=report_title, description=report_description)
        test_suite = unittest.TestSuite()
        test_suite.addTest(self.discover)
        html_runner.run(test_suite)


if __name__ == '__main__':
    testrunner = HtmlTestRunner('*test.py')
    testrunner.html_test_runner()
