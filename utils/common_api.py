#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: common_api.py
# @time: 2020-11-10 16:14
# @desc:
import requests
import re
import requests
from utils.read_conf import ReadConf


class API_INFO:
    def __init__(self):
        self.session_req = requests.session()
        self.read_conf = ReadConf()

    def get_access_token_api(self, grant_type, appid, secret):
        get_access_token_url = '/cgi-bin/token'
        get_params = {'grant_type': grant_type, 'appid': appid, 'secret': secret}
        response_obj = self.session_req.get(url=self.read_conf.get_conf_Host_url + get_access_token_url,
                                            params=get_params)
        return response_obj

    def get_default_access_token_api(self):
        get_access_token_url = '/cgi-bin/token'
        get_params = {'grant_type': self.read_conf.get_conf_grant_type, 'appid': self.read_conf.get_conf_appid,
                      'secret': self.read_conf.get_conf_secret}
        response_obj = self.session_req.get(url=self.read_conf.get_conf_Host_url + get_access_token_url,
                                            params=get_params)
        return response_obj

    @property
    def get_default_access_token_value(self):
        response_obj = self.get_default_access_token_api()
        access_token = response_obj.json()['access_token']
        return access_token

    def create_tag_api(self, name):
        get_create_tag_url = '/cgi-bin/tags/create'
        access_token = self.get_default_access_token_value
        get_params = {'access_token': access_token}
        post_data = {"tag": {"name": name}}
        response_obj = self.session_req.post(url=self.read_conf.get_conf_Host_url + get_create_tag_url,
                                             params=get_params,
                                             json=post_data)
        return response_obj

    def get_created_tag(self):
        created_tag_url = '/cgi-bin/tags/get'
        access_token = self.get_default_access_token_value
        get_params = {'access_token': access_token}
        response_obj = self.session_req.get(url=self.read_conf.get_conf_Host_url + created_tag_url, params=get_params)
        return response_obj

    def del_tag(self, id):
        del_tag_url = '/cgi-bin/tags/delete'
        access_token = self.get_default_access_token_value
        get_params = {'access_token': access_token}
        post_data = {"tag": {"id": id}}
        response_obj = self.session_req.post(url=self.read_conf.get_conf_Host_url + del_tag_url, params=get_params,
                                             json=post_data)
        return response_obj


if __name__ == '__main__':
    api_info = API_INFO()
    value = api_info.get_created_tag()
    print(value.json())
