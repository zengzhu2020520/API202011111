#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: read_conf.py
# @time: 2020-11-10 15:55
# @desc:
import configparser, os

conf_path_01 = os.path.join(os.path.dirname(__file__), '../config/config.ini')


class ReadConf:
    def __init__(self, conf_path=conf_path_01):
        self.conf_path = conf_path
        self.read_conf = configparser.ConfigParser()
        self.read_conf.read(self.conf_path, encoding='utf-8')

    def __get_conf_info(self, sec, option):
        value = self.read_conf.get(sec, option)
        return value

    @property
    def get_conf_Host_url(self):
        Host_url = self.__get_conf_info('default', 'Host_url')
        return Host_url

    @property
    def get_conf_grant_type(self):
        grant_type = self.__get_conf_info('default', 'grant_type')
        return grant_type

    @property
    def get_conf_appid(self):
        appid = self.__get_conf_info('default', 'appid')
        return appid

    @property
    def get_conf_secret(self):
        secret = self.__get_conf_info('default', 'secret')
        return secret

    @property
    def get_conf_report_path(self):
        secret = self.__get_conf_info('default', 'report_path')
        return secret

    @property
    def get_conf_smtp_server(self):
        return self.__get_conf_info('default', 'smtp_server')

    @property
    def get_conf_smtp_sender(self):
        return self.__get_conf_info('default', 'smtp_sender')

    @property
    def get_conf_smtp_senderpassword(self):
        return self.__get_conf_info('default', 'smtp_senderpassword')

    @property
    def get_conf_smtp_receiver(self):
        return self.__get_conf_info('default', 'smtp_receiver')

    @property
    def get_conf_smtp_cc(self):
        return self.__get_conf_info('default', 'smtp_cc')

    @property
    def get_conf_smtp_subject(self):
        return self.__get_conf_info('default', 'smtp_subject')

    @property
    def get_conf_smtp_body(self):
        return self.__get_conf_info('default', 'smtp_body')

    @property
    def get_conf_case_path(self):
        return self.__get_conf_info('default', 'case_path')

    # @property
    # def get_conf_smtp_file_path(self):
    #     return self.__get_conf_info('default', 'smtp_file_path')


read_conf = ReadConf()
if __name__ == '__main__':
    # read_conf = ReadConf()
    print(read_conf.get_conf_smtp_subject)
