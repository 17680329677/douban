# -*- coding:utf-8 -*-
"""
    将清洗后的数据插入数据库中保存
"""

import pymysql

# mysql链接配置，以字典形式
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'douban',
    'charset': 'utf8'
}

# 获得数据库连接
connection = pymysql.connect(**db_config)

inputFile = 'E://python//douban_movies_clean.txt'
fr = open(inputFile, 'r')

firstLine = True
count = 0

for line in fr:
    if firstLine:
        firstLine = False
        continue
    
    line = line.split('^')
    
    movieId = line[0]
    title = line[1]
    url = line[2]
    cover = line[3]
    rate = line[4]
    director = line[5]
    composer = line[6]
    actor = line[7]
    category = line[8]
    district = line[9]
    language = line[10]
    showtime = line[11]
    length = line[12]
    othername = line[13]
    description = line[14]
    
        # 获得数据库游标
    with connection.cursor() as cursor:
        sql = 'insert into movie(movieId,title,url,cover,rate,director,composer,actor,category,district,language,showtime,length,othername,description) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql,(movieId,title,url,cover,rate,director,composer,actor,category,district,language,showtime,length,othername,description))
    connection.commit()

connection.close()
