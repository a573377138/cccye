#-*- coding: utf8 -*-
# import random
# from pymongo import MongoClient
# import requests
# import time
# collection=MongoClient('localhost',27017)
# collection=collection['weibo']['weibo']
# user=['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
#      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
# headers={
# 'Host': 'api.weibo.cn',
# 'User-Agent':random.choice(user),
# 'Cookie':'ALF=1544929289; _T_WM=39e20928a39c3b92a9cdd8d71f3e2550; WEIBOCN_FROM=1110006030',
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Connection': 'keep-alive',
# 'Upgrade-Insecure-Requests': '1'}
#
# def get_inf(url):
#    html = requests.get(url, headers=headers).json()
#    max_id = html['max_id']
#    print(max_id)
#    n=0
#    print( html['root_comments'])
#    for i in html['root_comments']:
#        inf = {}
#        inf['text'] = i['text']
#        inf['time'] = i['created_at']
#        inf['disable_reply'] = i['disable_reply']
#        inf['liked']=i['like_counts']
#        inf['nick'] = i['user']['name']
#        #inf['class'] = i['user']['class']
#        inf['sex'] = i['user']['gender']
#        inf['city'] = i['user']['city']
#        inf['pro'] = i['user']['province']
#        inf['location'] = i['user']['location']
#        inf['关注'] = i['user']['friends_count']
#        inf['fans'] = i['user']['followers_count']
#        n=n+1
#        collection.insert_one(inf)
#        #print(inf)
#    return max_id,n
#
# total=0
# max_id='0'
# zero=15
# while zero:
#    url ='https://api.weibo.cn/2/comments/build_comments?flow=1&gsid=_2A2528V-DDeRxGeRM7loV9ifJyDuIHXVTp9RLrDV6PUJbkdAKLVf5kWpNU807bwxYkTUD9lwoQyaK4ajn_4FoWbka&wm=3333_2001&i=2a48abc&b=0&from=108B193010&c=iphone&networktype=wifi&v_p=69&skin=default&v_f=1&s=b1c8ec8f&lang=zh_CN&sflag=1&ua=iPhone9,1__weibo__8.11.1__iphone__os11.2.5&ft=11&aid=01AkR6c52cGZnAKXiIy1qC93kKA4LStXUv_uVymvDYrbPVZaw.&is_append_blogs=1&mid=4308928831894875&fid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D1&uicode=10000002&count=20&trim_level=1&moduleID=feed&max_id={}&is_show_bulletin=2&fetch_level=0&_status_id=4308928831894875&max_id_type=0&id=4308928831894875&luicode=10000003&featurecode=10000085&is_mix=1&page=0&lfid=100103type%3D1%26q%3D%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%26t%3D1&lcardid=seqid%3A870460522%7Ctype%3A1%7Ct%3A1%7Cpos%3A1-2-0%7Cq%3A%23%E5%A6%82%E6%9E%9C%E7%81%AB%E9%94%85%E5%8F%AA%E8%83%BD%E5%90%83%E4%B8%89%E6%A0%B7%E8%8F%9C%23%7Cext%3A%26cate%3D306%26mid%3D4308928831894875%26qtime%3D1542865414%26&rid=0_0_0_2669675512959047934_0_0&cum=6DD80FF3'.format(max_id)
#    max = max_id
#    try:
#        max_id,num=get_inf(url)
#    except Exception as e:
#        print(e)
#        time.sleep(30)
#        max_id,num=get_inf(url)
#    if not max_id:
#        max_id=max
#        zero=zero-1
#        time.sleep(60)
#    total=total+num
#    time.sleep(random.randint(1,2))
#    print(total)

import requests
from lxml import etree
import pyquery
from bs4 import BeautifulSoup
import time
headers ={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'SINAGLOBAL=9814691201761.367.1542011414888; login_sid_t=6fd069136a172608e17f1fda8910c8df; cross_origin_proto=SSL; Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; YF-V5-G0=bcfc495b47c1efc5be5998b37da5d0e4; WBStorage=bfb29263adc46711|undefined; _s_tentry=www.baidu.com; UOR=jx3.xoyo.com,widget.weibo.com,www.baidu.com; wb_view_log=1920*10801; Apache=6848891228083.991.1543804634960; ULV=1543804634964:2:1:1:6848891228083.991.1543804634960:1542011414895; SCF=Av-JqWB-ngsv-7f5JfV3o-HeBnRdqM5wwhzieSNwnBmeUGxnIyvPe_YfXOWlZ8fd9LMTItWIwybD-J5R3YMy9gQ.; SUB=_2A25xAOcfDeRhGeRI7lcS-SfMyD-IHXVSdF_XrDV8PUNbmtBeLRitkW9NUrFFiQe5SP8j9IymGolltEcKRDV9ZFRP; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhFLWrYhYxF9lTbleIzGx2F5JpX5K2hUgL.FozcSK-01K.7e0e2dJLoIpxki--fi-2NiKLhi--ciK.RiKy8P7tt; SUHB=0WGNO32EST1-dA; ALF=1544409615; SSOLoginState=1543804751; YF-Page-G0=324e50a7d7f9947b6aaff9cb1680413f; wb_view_log_2655399033=1920*10801',
        'Host': 'weibo.com',
        'Pragma': 'no-cache',
        'Referer': 'https://weibo.com/3190764044/H3Khl7WWv?type=comment',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
}
# for i in range(1,10):
#     req = requests.get('https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4308928831894875&page={}'.format(i),headers = headers).json()
#     #req.encoding = 'utf-8'
#     html =req['data']['html']
#     #print(html)
#     text = etree.HTML(html)
#     txt = text.xpath('//div[@class="list_con"]')
#     for i in txt:
#         t =i.xpath('./div[1]/text()')
#         print(t[1].strip('： '))
#     time.sleep(8)

req = requests.get('https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4308928831894875&root_comment_max_id=266374938880776&root_comment_max_id_type=0&root_comment_ext_param=&page=2&filter=hot&sum_comment_number=7236&filter_tips_before=0&from=singleWeiBo&__rnd=1543830301424',headers = headers).json()
html =req['data']['html']
print(html)
text = etree.HTML(html)
txt = text.xpath('//div[@class="list_con"]')
for i in txt:
    t =i.xpath('./div[1]/text()')
    print(t[1].strip('： '))