#!/usr/bin/env python
# coding=utf-8
###获取cdn上的文件夹列表##

from pub_conf import *
import random
import string
import oss2
from glob import glob
import os
import os.path
import sys

def upload_dir(bucket, _src, _dst):
    _dir = _src
    if _src[-1] == '/':
        _src = _src[:-1]
    index = _src.rfind('/')
    if index > -1:
        _dir = _src[index + 1 : ]
    cdn_path = _dst + _dir
    if cdn_path[-1] != '/':
        cdn_path += '/'
    for p in glob(_src + "/*"):
        if not os.path.isdir(p):
            upload_file(bucket, p, cdn_path)
        else:
            upload_dir(bucket, p, cdn_path)

def upload_file(bucket, _src, _dst):
    print _dst
    index = _src.rfind('/')
    file_name = _src
    if index > -1:
        file_name = _src[index + 1 :]
    cdn_path = _dst + file_name
    #with open(_src, 'rb') as fileobj:
    #    bucket.put_object(cdn_path, fileobj)
    bucket.put_object_from_file(cdn_path, _src)

def run(argv):
    if len(argv) < 4:
        print 'usage: python show_cdn_dir.py bucket src dst'
        print 'bucket: qmzbw, bzwcdn, zgws'
        return
    _bucket = argv[1]
    _src = argv[2]
    _dst = argv[3]
    if _bucket not in BUCKETS:
        print _bucket, 'not exist, valid bucket [qmzbw, bzwcdn, zgws]'
        return
    if not os.path.exists(_src):
        print _src, 'not exists'
        return
    bucket = oss2.Bucket(oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET), ENDPOINT, _bucket)
    if os.path.isfile(_src):
        upload_file(bucket, _src, _dst)
    else:
        upload_dir(bucket, _src, _dst)
 
if __name__ == '__main__':
    run(['','qmzbw','./crazy_activity_board.jpg','bzw_image/'])
