# -*- coding:utf-8 -*-
"""
    根据电影id获取电影的详细信息
"""

import urllib
from urllib import request
from urllib.parse import quote
import json
import time
import random
from bs4 import BeautifulSoup

 
inputFile = 'E://python//douban_movies.txt'    # 读取刚才文件的信息
fr = open(inputFile, 'r')
outputFile = 'E://python//douban_movies_detail.txt'  # 将爬取的详细信息写入该txt文件
fw = open(outputFile, 'w')
fw.write('id^title^url^cover^rate^director^composer^actor^category^district^language^showtime^length^othername^description\n')


# 设置请求头的内容
headers = {}
# headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
# headers["Accept-Encoding"] = "gzip, deflate, sdch"
# headers["Accept-Language"] = "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2"
# headers["Cache-Control"] = "max-age=0"
# headers["Connection"] = "keep-alive"
headers["Cookie"] = 'asdasd13323efafasfa'
# headers["Host"] = "movie.douban.com"
# headers["Referer"] = "http://movie.douban.com/"
# headers["Upgrade-Insecure-Requests"] = 1
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

firstLine = True   # 跳过文本的第一行，从正文第一行开始（文本第二行）

count = 1    # 总数
errorCount = 0   # 错误数

result = {}   # 结果集

for line in fr:
    if firstLine:
        firstLine = False
        continue
    
    line = line.split(';')
    movieId = line[0]
    title = line[1]
    url = line[2]
    cover = line[3]
    rate = line[4].rstrip('\n') # 该函数删除字符串末尾指定的字符串
    
    if movieId in result:
        continue
    else:
        result[str(movieId)] = 1
    try:
        page = request.Request(url=url, headers=headers)
        pageinfo = request.urlopen(page, timeout=20)
        page_html = pageinfo.read().decode('utf-8')
        page_html = BeautifulSoup(page_html, 'html.parser')
        
        info = page_html.select('#info')[0]   # 根据页面源码， 影片的详细信息均在css为info的div中
        info = info.get_text().split('\n')    # 将信息按行分开
        
        # 提取字段， 只要冒号后面的文本字段
        director = info[1].split(':')[-1].strip()  # 导演
        composer = info[2].split(':')[-1].strip()  # 编剧
        actor = info[3].split(':')[-1].strip()     # 主演
        category = info[4].split(':')[-1].strip()  # 类型
        district = info[6].split(':')[-1].strip()  # 制片国家
        language = info[7].split(':')[-1].strip()  # 语言
        showtime = info[8].split(':')[-1].strip()  # 上映日期
        length = info[9].split(':')[-1].strip()    # 片长
        othername = info[10].split(':')[-1].strip()# 别名
        
        # 电影简介
        description = page_html.find_all("span", attrs={"property": "v:summary"})[0].get_text()
        # .lstrip()用于去掉左边的指定字符 ，同理.rstrip()去掉右边的 
        description = description.lstrip().lstrip('\n\t').rstrip().rstrip('\n\t').replace('\n', '\t')
        
        # 写入数据
        record = str(movieId) + '^' + title + '^' + url + '^' + cover + '^' + str(rate) + '^' + director + '^' + composer + '^' + actor + '^' + category + '^' + district + '^' + language + '^' + showtime + '^' + length + '^' + othername + '^' + description + '\n'
        fw.write(record)
        print(count, title)
        time.sleep(1)  # 休眠，防止速度过快被封IP
    
    except Exception as e:
        print(e)
        print(count, title, "Error")
        errorCount = errorCount + 1
    
    else:
        pass
    finally:
        pass
    
    count = count + 1

print(result)    
print(count, errorCount)
fr.close()
fw.close()