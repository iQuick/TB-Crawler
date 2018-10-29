#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2018/1/9


import time
import jieba
import sys
import tb_login
import threading
from api import *
from tb_api import *
from tb_api import get_api_urls
import sys
import getopt


# def main():
#     crawler_threads = []
#     cookie = tb_login.get_cookies(False)
#     for index, api_url in enumerate(get_api_urls()):
#         t_name = 'crawler_thread_' + str(index)
#         print u'开启线程 ===> ' + t_name
#         t = threading.Thread(name=t_name, target=crawler_product, args=(cookie, api_url, ))
#         crawler_threads.append(t)
#         t.start()
#     for t in crawler_threads:
#         t.join()
#
# def main():
#     cookie = tb_login.get_cookies(False)
#     for index, api_url in enumerate(get_api_urls()):
#         # t_name = 'crawler_thread_' + str(index)
#         print u'开启抓取 ===> ' + str(index)
#         crawler_product(cookie, api_url)
#         # t = threading.Thread(name=t_name, target=crawler_product, args=(cookie, api_url, ))


def main():
    cookie = tb_login.get_cookies(False)
    while True:
        try:
            c_address = get_crawler_address()
            print u'开始抓取 =================== Start '
            crawler_product(cookie, c_address['data'])
        except Exception as e:
            print u'没有可抓取项，休眠60s ...'
            time.sleep(60)


def crawler_product(cookie, dit):
    for i in range(1 if dit['start_page']==0 else dit['start_page'], 1000 if dit['end_page']==0 else dit['end_page']):
        end = crawler_product_page(dit, i, cookie)
        if end:
            print u'======================== 结束 ========================'
            break


def crawler_product_page(dit, page, cookies):
    print u'============================= 开始抓取第 ' + str(page) + u'页 ============================='
    print u'url ==> ' + get_product_url(dit['product_url'], page)
    print '\n'

    r = requests.get(get_product_url(dit['product_url'], page), cookies=cookies)

    info = r.json()['data']
    for p in info['pageList']:

        seg_list = jieba.cut_for_search(p['title'])
        tags = ','.join(seg_list)

        mys = {}
        mys['nick'] = p['nick']
        mys['name'] = p['shopTitle']
        mys['seller_id'] = p['sellerId']
        mys['tsid'] = p['sellerId']
        store = create_store(mys)

        myp = {}
        myp['tpid'] = p['auctionId']
        myp['cid'] = dit['category']
        myp['sid'] = store['data']['id']
        myp['name'] = p['title']
        myp['tags'] = tags
        myp['cover'] = p['pictUrl']
        myp['price'] = p['zkPrice']
        myp['source_link'] = p['auctionUrl']
        myp['coupon'] = 1 if p['couponTotalCount'] > 0 else 0
        myp['coupon_info'] = p['couponInfo']
        myp['coupon_start_fee'] = p['couponStartFee']
        myp['coupon_amount'] = p['couponAmount']
        myp['biz30day'] = p['biz30day']
        myp['commission_rate'] = p['eventRate']
        myp['tk_comm_fee'] = p['tkCommFee']
        myp['tk_rate'] = p['tkRate']
        myp['description'] = p['title']
        myp['coupon_effective_start_at'] = p['couponEffectiveStartTime']
        myp['coupon_effective_end_at'] = p['couponEffectiveEndTime']
        myp['status'] = 1

        # r
        url = get_coupon_url(dit['coupon_url'], p['auctionId'])
        r = requests.get(url, cookies=cookies)
        data = r.json()['data']
        try:
            myp['tpwd'] = data['taoToken']
            myp['link_short'] = data['shortLinkUrl']
            myp['link_long'] = data['clickUrl']
            myp['qrcode'] = data['qrCodeUrl']
        except Exception as e:
            pass

        try:
            if myp['coupon']:
                myp['ctpwd'] = data['couponLinkTaoToken']
                myp['coupon_link_short'] = data['couponShortLinkUrl']
                myp['coupon_link_long'] = data['couponLink']
        except Exception as e:
            print u'没有优惠券'

        create_product(myp)
        print '\n=========================== Item End ================================== \n'
        time.sleep(2)

    if info['head']['pageNo'] == info['paginator']['pages']:
        return True
    else:
        time.sleep(60)
        return False

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # 参数
    try:
        opts, args = getopt.getopt(sys.argv[1:], "dhv", ['debug', 'help', 'version'])
        for op, value in opts:
            if op in ('-d', '--debug'):
                set_debug(True)
            elif op in ("-h", "--help"):
                print usage.__doc__
                sys.exit()
            elif op in ("-v", "--version"):
                print get_version()
                sys.exit()
            else:
                print "Using the wrong way, please view the help information."
    except getopt.GetoptError as err:
        print usage.__doc__
        sys.exit(1)

    main()
