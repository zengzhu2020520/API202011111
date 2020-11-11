#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: HTMLTestReportCN_report.py
# @time: 2020-11-11 13:21
# @desc:
import unittest
import os, time
from utils import HTMLTestReportCN
from utils.read_conf import read_conf

case_path_01 = os.path.join(os.path.dirname(__file__), '..', read_conf.get_conf_case_path)
report_path_01 = os.path.join(os.path.dirname(__file__), '..', read_conf.get_conf_report_path,
                              'report_%s') % time.strftime(
    '%Y%m%d_%H%M%S')
report_title_01 = '接口自动化标题'
report_description_01 = '接口自动化描述'


class HTMLTestRCN:
    def __init__(self, pattern, case_path=case_path_01):
        self.case_path = case_path
        self.pattern = pattern
        self.discover = unittest.defaultTestLoader.discover(start_dir=self.case_path, pattern=self.pattern,
                                                            top_level_dir=self.case_path)

    def html_test_reportCN(self, report_path=report_path_01, report_title=report_title_01,
                           report_description=report_description_01):
        report_dir = HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.create_dir(report_title)
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        file = open(report_path, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=file, title=report_title, description=report_description)
        test_suite = unittest.TestSuite()
        test_suite.addTest(self.discover)
        runner.run(test_suite)


if __name__ == '__main__':
    html = HTMLTestRCN('*test.py')
    html.html_test_reportCN()
