# -*- coding:utf-8 -*-
# ���ؿ�
import sys
import string
from urllib import request
from urllib.parse import quote
import urllib
import json
from bs4 import BeautifulSoup

# ��ȡ���б�ǩ
tags = []
url = 'https://movie.douban.com/j/search_tags?type=movie'  #�����ӷ���һ��json��ʽ�Ĵ������������е�Ӱ�����ǩ
page = request.Request(url=url)
result = request.urlopen(page, timeout=20).read().decode('utf-8')

# ����jsonΪ�ֵ�
result = json.loads(result)
tags = result['tags']

# ����һ���б�洢��Ӱ�Ļ�����Ϣ
movies = []
# ����ÿ��tag��ǩ�µĵ�Ӱ
for tag in tags:
    start = 0
    # ��������ֱ�����صĽ��Ϊ��
    while 1:
        # ƴ����Ҫ��������ӣ�������ǩ�Ϳ�ʼ���
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&sort=recommend&page_limit=20&page_start=' + str(start)
        print(url)
        url = quote(url, safe=string.printable)
        pagemv = request.Request(url=url)
        pageinfo = request.urlopen(pagemv, timeout=20).read().decode('utf-8')
        resultmv = json.loads(pageinfo)
        
        # ����������з�������API���۲췵��json�Ľṹ
        # Ȼ����Python��ȡ����Ҫ��ֵ
        resultmv = resultmv['subjects']
        
        # ���ؽ��Ϊ�գ�˵���Ѿ�û��������
        # ���һ����ǩ�Ĵ����˳�ѭ��
        if len(resultmv) == 0:
            break
        
        # ��ÿһ�����ݶ�����movies
        for item in resultmv:
            movies.append(item)
        # �޸�start
        start += 20
        
print(len(movies))
        