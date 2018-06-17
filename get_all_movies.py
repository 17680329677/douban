# -*- coding:utf-8 -*-
"""
    һ������ȡ�������е�Ӱ�ĸ�Ҫ��Ϣ
    ��Ϣ�洢��txt��
    
"""
import urllib
from urllib import request
from urllib.parse import quote
import json
import time
import string

ISOTIMEFORMAT = '%Y-%m-%d %X'    # ����һ��ʱ���ʽ

outputfile = 'E://python//douban_movies.txt'    # д�뵽��txt�ļ���
fw = open(outputfile, 'w')
fw.write('id;title;url;cover;rate\n')

# ��������ͷ�ĸ�������
headers = {}
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
headers["Accept-Encoding"] = "gzip, deflate, sdch"
headers["Accept-Language"] = "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2"
# headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
# headers["Cookie"] = 'bid="LJSWKkSUfZE"; ll="108296"; __utmt=1; regpop=1; _pk_id.100001.4cf6=32aff4d8271b3f15.1442223906.2.1442237186.1442224653.; _pk_ses.100001.4cf6=*; __utmt_douban=1; __utma=223695111.736177897.1442223906.1442223906.1442236473.2; __utmb=223695111.0.10.1442236473; __utmc=223695111; __utmz=223695111.1442223906.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=30149280.674845100.1442223906.1442236473.1442236830.3; __utmb=30149280.4.9.1442237186215; __utmc=30149280; __utmz=30149280.1442236830.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap=1'
headers["Host"] = "movie.douban.com"
headers["Referer"] = "http://movie.douban.com/"
headers["Upgrade-Insecure-Requests"] = 1
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"


# ��ȡ��ǩtag
page = request.Request(url="http://movie.douban.com/j/search_tags?type=movie")
page_tag = request.urlopen(page, timeout=20)
tags = json.loads(page_tag.read().decode('utf-8'))['tags']
print(tags)

# ��ʼ��ȡ
print("***********Start*************")
print(time.strftime(ISOTIMEFORMAT, time.localtime()))   # ������ʱ��Ԫ�飬�������Կɶ��ַ�����ʾ�ĵ���ʱ�䣬��ʽ�ɲ���format����

for tag in tags:
    print("Crawl movies with tag: " + tag)
    print(time.strftime(ISOTIMEFORMAT, time.localtime()))
    
    start = 0
    while True:
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&sort=recommend&page_limit=20&page_start=' + str(start)
        url = quote(url, safe=string.printable)
        page_movie = request.Request(url=url)
        page_info = request.urlopen(page_movie, timeout=20)
        movies = json.loads(page_info.read().decode('utf-8'))['subjects']
        if len(movies) == 0:
            break
        for item in movies:
            rate = item['rate']
            title = item['title']
            url = item['url']
            cover = item['cover']
            movieId = item['id']
            record = str(movieId) + ';' + title + ';' + url + ';' + cover + ';' + str(rate) + '\n'
            fw.write(record)
            print(tag + '\t' + title)
        start += 20
    
fw.close()