# -*- coding:utf-8 -*-
# 加载库
import sys
import string
from urllib import request
from urllib.parse import quote
import urllib
import json
from bs4 import BeautifulSoup

# 获取所有标签
tags = []
url = 'https://movie.douban.com/j/search_tags?type=movie'  #此链接返回一个json格式的串，包含了所有电影分类标签
page = request.Request(url=url)
result = request.urlopen(page, timeout=20).read().decode('utf-8')

# 加载json为字典
result = json.loads(result)
tags = result['tags']

# 定义一个列表存储电影的基本信息
movies = []
# 处理每个tag标签下的电影
for tag in tags:
    start = 0
    # 不断请求，直到返回的结果为空
    while 1:
        # 拼接需要请求的链接，包含标签和开始编号
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&sort=recommend&page_limit=20&page_start=' + str(start)
        print(url)
        url = quote(url, safe=string.printable)
        pagemv = request.Request(url=url)
        pageinfo = request.urlopen(pagemv, timeout=20).read().decode('utf-8')
        resultmv = json.loads(pageinfo)
        
        # 先在浏览器中访问以下API，观察返回json的结构
        # 然后在Python中取出需要的值
        resultmv = resultmv['subjects']
        
        # 返回结果为空，说明已经没有数据了
        # 完成一个标签的处理，退出循环
        if len(resultmv) == 0:
            break
        
        # 将每一条数据都加入movies
        for item in resultmv:
            movies.append(item)
        # 修改start
        start += 20
        
print(len(movies))
        