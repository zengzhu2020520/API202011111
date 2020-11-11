#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: get_access_token.py
# @time: 2020-11-11 8:26
# @desc:
import unittest
from utils.common_api import API_INFO


class APITest(unittest.TestCase):
    def setUp(self) -> None:
        self.api_info = API_INFO()

    def tearDown(self) -> None:
        pass

    def test_success_get_asscess_token(self):
        response_object = self.api_info.get_default_access_token_api()
        self.assertTrue(response_object.json()['access_token'], 'test_success_get_asscess_token执行失败')

    def test_fail_get_asscess_token(self):
        response_object = self.api_info.get_access_token_api(grant_type='ient_credential', appid='wx36e864adacdd988b',
                                                             secret='aad08333a84cadcabea20b')
        print(response_object.json())
        self.assertEqual(response_object.json()['errcode'], 40002, 'test_fail_get_asscess_token执行失败')


if __name__ == '__main__':
    unittest.main()
