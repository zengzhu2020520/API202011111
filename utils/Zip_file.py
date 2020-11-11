#!/usr/bin/env python
# encoding: utf-8
# @author: zengzhu
# @file: Zip_file.py
# @time: 2020-11-11 10:12
# @desc:
import os
import zipfile

dir_path1 = os.path.join(os.path.dirname(__file__), '../reports/report_20201111_100930.html接口测试报告V1.0')
zip_path1 = dir_path1 + '.zip'


def zip_dir(dir_path, zip_path):
    zip = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
    for root, dirnames, filenames in os.walk(dir_path):
        file_path = root.replace(dir_path, '')  # 去掉跟路径，只对目标文件夹下的文件和文件夹进行压缩
        # 循环出一个文件名
        for filename in filenames:
            zip.write(os.path.join(root, filename), os.path.join(file_path, filename))
        # zip.close()


if __name__ == '__main__':
    zip_dir(dir_path1, zip_path1)
    # smtp_file_path = os.path.join(os.path.dirname(__file__), '../scream_hot/scream')
    # file_path =smtp_file_path+'.zip'
    # zip_dir(smtp_file_path, file_path)
