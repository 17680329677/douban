# -*- coding:utf-8 -*-
"""
    ���ݵ�Ӱid��ȡ��Ӱ����ϸ��Ϣ
"""

import urllib
from urllib import request
from urllib.parse import quote
import json
import time
import random
from bs4 import BeautifulSoup

 
inputFile = 'E://python//douban_movies.txt'    # ��ȡ�ղ��ļ�����Ϣ
fr = open(inputFile, 'r')
outputFile = 'E://python//douban_movies_detail.txt'  # ����ȡ����ϸ��Ϣд���txt�ļ�
fw = open(outputFile, 'w')
fw.write('id^title^url^cover^rate^director^composer^actor^category^district^language^showtime^length^othername^description\n')


# ��������ͷ������
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

firstLine = True   # �����ı��ĵ�һ�У������ĵ�һ�п�ʼ���ı��ڶ��У�

count = 1    # ����
errorCount = 0   # ������

result = {}   # �����

for line in fr:
    if firstLine:
        firstLine = False
        continue
    
    line = line.split(';')
    movieId = line[0]
    title = line[1]
    url = line[2]
    cover = line[3]
    rate = line[4].rstrip('\n') # �ú���ɾ���ַ���ĩβָ�����ַ���
    
    if movieId in result:
        continue
    else:
        result[str(movieId)] = 1
    try:
        page = request.Request(url=url, headers=headers)
        pageinfo = request.urlopen(page, timeout=20)
        page_html = pageinfo.read().decode('utf-8')
        page_html = BeautifulSoup(page_html, 'html.parser')
        
        info = page_html.select('#info')[0]   # ����ҳ��Դ�룬 ӰƬ����ϸ��Ϣ����cssΪinfo��div��
        info = info.get_text().split('\n')    # ����Ϣ���зֿ�
        
        # ��ȡ�ֶΣ� ֻҪð�ź�����ı��ֶ�
        director = info[1].split(':')[-1].strip()  # ����
        composer = info[2].split(':')[-1].strip()  # ���
        actor = info[3].split(':')[-1].strip()     # ����
        category = info[4].split(':')[-1].strip()  # ����
        district = info[6].split(':')[-1].strip()  # ��Ƭ����
        language = info[7].split(':')[-1].strip()  # ����
        showtime = info[8].split(':')[-1].strip()  # ��ӳ����
        length = info[9].split(':')[-1].strip()    # Ƭ��
        othername = info[10].split(':')[-1].strip()# ����
        
        # ��Ӱ���
        description = page_html.find_all("span", attrs={"property": "v:summary"})[0].get_text()
        # .lstrip()����ȥ����ߵ�ָ���ַ� ��ͬ��.rstrip()ȥ���ұߵ� 
        description = description.lstrip().lstrip('\n\t').rstrip().rstrip('\n\t').replace('\n', '\t')
        
        # д������
        record = str(movieId) + '^' + title + '^' + url + '^' + cover + '^' + str(rate) + '^' + director + '^' + composer + '^' + actor + '^' + category + '^' + district + '^' + language + '^' + showtime + '^' + length + '^' + othername + '^' + description + '\n'
        fw.write(record)
        print(count, title)
        time.sleep(1)  # ���ߣ���ֹ�ٶȹ��챻��IP
    
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