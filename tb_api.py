#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Em on 2018/1/9

import re

_api_urls = [
    # {
    #     'product_url': 'http://pub.alimama.com/items/channel/muying.json?spm=a219t.7900221%2F1.1998910419.ddc9f73e2.2bd61157okb4Wu&channel=muying&perPageSize=50&shopTag=&t=1515858355608&_tb_token_=f5e3e1436e58f&pvid=22_49.211.77.139_4829_1515858355263',
    #     'coupon_url': 'http://pub.alimama.com/common/code/getAuctionCode.json?auctionid=547212428150&adzoneid=191266467&siteid=41858721&scenes=1&channel=tk_muying&t=1515860848947&_tb_token_=f5e3e1436e58f&pvid=22_49.211.77.139_623_1515860835278',
    #     'category': '15',
    #     'tags': '母婴'
    # }
    # ,
    # {
    #     'product_url': 'http://pub.alimama.com/items/channel/9k9.json?spm=a219t.7900221%2F1.1998910419.d5f9e8538.2bd61157okb4Wu&channel=9k9&perPageSize=50&shopTag=&t=1515858510755&_tb_token_=f5e3e1436e58f&pvid=16_49.211.77.139_167_1515858510268',
    #     'coupon_url': 'http://pub.alimama.com/common/code/getAuctionCode.json?auctionid=553668178556&adzoneid=191266467&siteid=41858721&scenes=1&channel=tk_9k9&t=1515858588302&_tb_token_=f5e3e1436e58f&pvid=16_49.211.77.139_4984_1515858509847',
    #     'category': '1000',
    #     'tags': '九块九包邮'
    # }
    # ,
    # {
    #     'product_url': 'http://pub.alimama.com/items/channel/9k9.json?spm=a219t.7900221%2F1.1998910419.d5f9e8538.1b30c7093kKHky&channel=9k9&dpyhq=1&sortType=9&catIds=8&level=1&perPageSize=50&shopTag=dpyhq&t=1516073539816&_tb_token_=753e736e3e8ea&pvid=16_59.173.203.230_4953_1516071951136',
    #     'coupon_url': 'http://pub.alimama.com/common/code/getAuctionCode.json?auctionid=19548772081&adzoneid=191266467&siteid=41858721&scenes=1&channel=tk_9k9&t=1516072008969&_tb_token_=753e736e3e8ea&pvid=16_59.173.203.230_4953_1516071951136',
    #     'category': '3',
    #     'tags': '食物,吃汇,9块9包邮'
    # }
    # ,
    {
        'product_url': 'http://pub.alimama.com/items/channel/9k9.json?spm=a219t.7900221%2F1.1998910419.d5f9e8538.94609aciLZldF&channel=9k9&toPage=4&dpyhq=1&perPageSize=50&catIds=4&level=1&shopTag=dpyhq&t=1516170525289&_tb_token_=533ee7559e61b&pvid=16_59.173.203.230_2041_1516170503914',
        'coupon_url': 'http://pub.alimama.com/common/code/getAuctionCode.json?auctionid=545018353694&adzoneid=191266467&siteid=41858721&scenes=1&channel=tk_9k9&t=1516170554149&_tb_token_=533ee7559e61b&pvid=16_59.173.203.230_5582_1516170526631',
        'category': '12',
        'tags': '珠宝,配饰,9块9包邮'
    }
]


def get_api_urls():
    return _api_urls


def get_coupon_url(url, auctionid):
    pattern = re.compile(r'auctionid={.*?}&')
    return re.sub(pattern, str(auctionid), url)


def get_product_url(url, page):
    pattern = re.compile(r'toPage={.*?}&')
    return re.sub(pattern, str(page), url)


def get_tags(tags):
    return ',' + tags


if __name__ == '__main__':
    print 'test get_coupon_url'
    print get_coupon_url(get_api_urls()[0]['coupon_url'], '547212428150')

    print 'test get_product_url'
    print get_product_url(get_api_urls()[0]['product_url'], 1)

