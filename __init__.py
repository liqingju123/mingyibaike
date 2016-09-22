# encoding:utf-8
from urllib import urlopen
import urllib2
import time
import sys 
import re
from bs4 import  BeautifulSoup






def zhengli():
    keshi_jibing_xiangqing = open('/Users/imac/Downloads/名医百科/科室_疾病_详情.txt', 'r')
    keshi_jibing_xiangqing_xiugai = open('/Users/imac/Downloads/名医百科/科室_疾病_详情_修改.txt', 'w')
    keshi_jibing_xiangqing_quandui = open('/Users/imac/Downloads/名医百科/科室_疾病_详情_全对.txt', 'w')
    keshi_jibing_xiangqing_list = keshi_jibing_xiangqing.readlines()
    for keshi_jibing_xiangqing_one in keshi_jibing_xiangqing_list:
        keshi_jibing_xiangqing_list_one = keshi_jibing_xiangqing_one.split('__')
        if len(keshi_jibing_xiangqing_list_one) == 5:
            keshi_jibing_xiangqing_xiugai.write(keshi_jibing_xiangqing_one)
        else:
            keshi_jibing_xiangqing_quandui.write(keshi_jibing_xiangqing_one)
    
    keshi_jibing_xiangqing_xiugai.close()
    keshi_jibing_xiangqing_quandui.close()
    print '完毕'

def keshi_jienjie():
    keshi_jibing = open('/Users/imac/Downloads/名医百科/科室_疾病.txt', 'r')
    keshi_jibing_xiangqing = open('/Users/imac/Downloads/名医百科/科室_疾病_详情.txt', 'r')
    list_all_keshi = keshi_jibing.readlines()[6300:]
    for one_url in list_all_keshi:
        text_list = one_url.split('__')
        url_keshi_jibing_xiangqiang = text_list[2].replace('view', 'detail') + '/1'
        page_text = get_html(url_keshi_jibing_xiangqiang)
        page_beaut = BeautifulSoup(page_text)
        jiejian_list = page_beaut.find_all('div', {'class':'lemma-main-content'})
        page_text_one = ''
        for one_jiejian in jiejian_list:
            page_text_one = page_text_one + '__' + rm_all_pasce(str(one_jiejian.get_text().encode('utf-8')))
        
        page_text_one = rm_all_pasce(one_url) + page_text_one + '__' + url_keshi_jibing_xiangqiang + '\n'
        print page_text_one
        keshi_jibing_xiangqing.write(page_text_one)
    
    keshi_jibing_xiangqing.close()

def keshi_jibing(page_num):
    keshi_jibing = open('/Users/imac/Downloads/名医百科/科室_疾病.txt', 'w')
    mingyi = open('/Users/imac/Downloads/名医百科/科室.txt', 'r')
    lines_keshi = mingyi.readlines()
    for one_keshi in lines_keshi:
        url_name = one_keshi.split('__')
        for index in range(1, 9):
            page = get_html(url_name[0] + page_num % index)
            page_add(rm_all_pasce(one_keshi), page, keshi_jibing)
    
    keshi_jibing.close()
    mingyi.close()
    print '抓取完成'

def get_all_keshi(host):
    mingyi =open('/Users/imac/Downloads/名医百科/科室.txt','r')
    content_mingyi = get_html('http://www.baikemy.com/disease/list/0/0')
    list_all_keshi = re.findall('<li title="" class="yiyao_w70"><a[\s\S]*?href="(.*?)">(.*?)</a></li>', content_mingyi)
    for one_yiyang in list_all_keshi:
        mingyi.write('%s%s__%s\n' % (host, one_yiyang[0], one_yiyang[1]))
    
    mingyi.close()

host ='http://www.baikemy.com'
page_num ='?pageIndex=%d&pageCount=10'

def rm_all_pasce(text):
    return text.replace("\n", "").replace("\t", "").replace(' ', '').replace('\r', '').replace('<<收起', '')

def get_html(site):
    print site
    hdr = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(site, headers=hdr)
    try:
        data = urllib2.urlopen(req, timeout=4)
        page = data.read()
        print '===请求到了==='
    except:
        return '1错误'
    try:
#         page1 = page.decode('gbk')
        return page
    except:
        return page

def page_add(keshi,page,keshi_jibing):
    list_jibing = re.findall('<li><a  target="_blank" href="(.*?)">(.*?)</a></li>', page)
    print len(list_jibing)
    for one_jibing in list_jibing:
#         print keshi+'__'+host+one_jibing[0]+'__'+one_jibing[1]+'\n'
        keshi_jibing.write(keshi+'__'+host+one_jibing[0]+'__'+one_jibing[1]+'\n')
    


# keshi_jibing = open('/Users/imac/Downloads/名医百科/科室_疾病_详情_修改.txt', 'r')
# keshi_jibing_xiangqing = open('/Users/imac/Downloads/名医百科/科室_疾病_详情.txt', 'w')
# list_all_keshi = keshi_jibing.readlines()
# for one_url in list_all_keshi:
#         text_list = one_url.split('__')
#         url_keshi_jibing_xiangqiang = text_list[2].replace('view', 'detail') + '/1'
#         page_text = get_html(url_keshi_jibing_xiangqiang)
#         page_beaut = BeautifulSoup(page_text)
#         jiejian_list = page_beaut.find_all('div', {'class':'lemma-main-content'})
#         page_text_one = ''
#         for one_jiejian in jiejian_list:
#             page_text_one = page_text_one + '__' + rm_all_pasce(str(one_jiejian.get_text().encode('utf-8')))
#         one_url =text_list[0]+'__'+text_list[1]+'__'+text_list[2]+'__'+text_list[3]+'__'
#         page_text_one = rm_all_pasce(one_url) + page_text_one + '__' + url_keshi_jibing_xiangqiang + '\n'
#         print page_text_one
#         keshi_jibing_xiangqing.write(page_text_one)
#     
# keshi_jibing_xiangqing.close()






