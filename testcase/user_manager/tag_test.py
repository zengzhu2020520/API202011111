#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: tag_testcases.py
# @time: 2020-11-11 8:57
# @desc:
import unittest, requests, time
from utils.common_api import API_INFO


class TagTest(unittest.TestCase):
    def setUp(self) -> None:
        self.api_info = API_INFO()

    def tearDown(self) -> None:
        pass

    def test_success_creat_tag(self):
        name_str = '深圳' + str(time.time())
        response_object = self.api_info.create_tag_api(name_str)
        name = response_object.json()['tag']['name'].encode('utf-8').decode('unicode_escape')
        self.assertEqual(name, name_str, '新建标签成功')

    def test_create_tag_too_long(self):
        response_object = self.api_info.create_tag_api('亚洲亚洲人亚洲人亚洲人亚洲人亚洲人亚洲人亚洲人亚洲人亚洲人亚洲人亚洲人亚洲人人')
        errcode = response_object.json()['errcode']
        self.assertEqual(errcode, 45158, 'test_create_tag_too_long用例执行失败')


if __name__ == '__main__':
    unittest.main()
