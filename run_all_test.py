#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: run_all_test.py
# @time: 2020-11-10 15:53
# @desc:

import HTMLTestRunner
import os
import unittest
import time
from utils.HTMLTestRunner_report import HtmlTestRunner
from utils.HTMLTestReportCN_report import HTMLTestRCN
from utils.email_utils import EmailUtils
from utils.read_conf import read_conf

case_path_01 = os.path.join(os.path.dirname(__file__), read_conf.get_conf_case_path)
RC_report_path_01 = os.path.join(os.path.dirname(__file__), read_conf.get_conf_report_path,
                                 'report_%s') % time.strftime(
    '%Y%m%d_%H%M%S')
html_test_report_path_01 = os.path.join(os.path.dirname(__file__), read_conf.get_conf_report_path,
                                        '接口自动化测试报告_%s.html') % time.strftime('%Y%m%d_%H%M%S')
report_title_01 = '接口自动化标题'
report_description_01 = '接口自动化描述'


class RunAllTest:
    def __init__(self, pattern, case_path=case_path_01, report_title=report_title_01,
                 report_desription=report_description_01):
        self.patter = pattern
        self.case_path = case_path
        self.report_title = report_title
        self.report_desription = report_desription

    def run_all_test_by_htmltest_report(self, html_test_report_path=html_test_report_path_01):
        html_runner = HtmlTestRunner(self.patter)
        html_runner.html_test_runner()
        report_path = os.path.dirname(html_test_report_path)
        send_emial = EmailUtils(report_path)
        msg = send_emial.mail_content()
        send_emial.semnd_email(msg)

    def run_all_test_by_htmlRC_report(self, RC_report_path=RC_report_path_01):
        HTMLTestRCN(self.patter).html_test_reportCN()
        send_emial = EmailUtils(os.path.dirname(RC_report_path))
        msg = send_emial.mail_content()
        send_emial.semnd_email(msg)


if __name__ == '__main__':
    RunAllTest('*test.py').run_all_test_by_htmlRC_report()
    # RunAllTest('*test.py').run_all_test_by_htmltest_report()
