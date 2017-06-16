#!/usr/bin/env python
# coding=utf-8
###获取cdn上的文件夹列表##

from pub_conf import *
import os
import random
import string
import oss2
import sys

def list_dir(bucket, _dir):
    #print('\n'.join(info.name for info in oss2.BucketIterator(service)))
    for obj in oss2.ObjectIterator(bucket):
        if _dir:
            if obj.key.find('.') != -1:
                continue
        print obj.key

def run(argv):
    if len(argv) < 2:
        print 'usage: python show_cdn_dir.py bucket'
        print 'bucket: qmzbw, bzwcdn, zgws'
        return
    _bucket = argv[1]
    _dir = False
    if len(argv) == 3:
        _dir = True
    if _bucket not in BUCKETS:
        print _bucket, 'not exist, valid bucket [qmzbw, bzwcdn, zgws]'
        return

    bucket = oss2.Bucket(oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET), ENDPOINT, _bucket)
    list_dir(bucket, _dir)
 
if __name__ == '__main__':
    run(['python',  'qmzbw'])
