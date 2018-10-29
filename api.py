#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2018/1/9

import requests
from config import *

SERVER_HOST = 'http://xxxxx'
LOCAL_HOST = 'http://xxxxx'


# 爬取地址
API_CRAWLER_ADDRESS = '/api/import/xxxxx'
# 分类
API_CATEGORY = '/api/import/xxxxx'
# 店铺
API_STORE = '/api/import/xxxxx'
# 商品
API_PRODUCT = '/api/import/xxxxx'
# 商品描述
API_PRODUCT_DESC = '/api/import/xxxxx'
# 链接/淘口令
API_LINK = '/api/import/xxxxx'


def get_host():
    if get_debug():
        return LOCAL_HOST
    else:
        return SERVER_HOST

# def get_host():
#     return LOCAL_HOST


# 爬取地址
def get_crawler_address():
    return requests.get(LOCAL_HOST + API_CRAWLER_ADDRESS).json()


# 获取所有的分类
def get_all_category():
    return requests.get(get_host() + API_CATEGORY).json()


# 获取所有的店铺
def get_all_store():
    return requests.get(get_host() + API_STORE).json()


def create_store(params):
    r = requests.post(get_host() + API_STORE, params)
    print u'创建店铺成功 ==> ' + params['name']
    return r.json()


def create_product(params):
    r = requests.post(get_host() + API_PRODUCT, params)
    print u'======================= 创建商品 ======================= '
    print u'Name ==> ' + str(params['name'])
    print u'tpid ==> ' + str(params['tpid'])
    print u'tags ==> ' + str(params['tags'])
    print '          ---------------- Json ----------------         '
    print r.text
    print u'======================= 创建商品成功 ======================= '
    return r.json()


if __name__ == '__main__':
    print get_crawler_address()
