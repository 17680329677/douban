# -*- coding:utf-8 -*-
"""
    ����ȡ�ĵ�Ӱ��Ϣ���ݽ�����ϴ
"""

import json
import time
import random

inputFile = 'E://python//douban_movies_detail.txt'
fr = open(inputFile, 'r')
outputFile = 'E://python//douban_movies_clean.txt'
fw = open(outputFile, 'w')
fw.write('id^title^url^cover^rate^director^composer^actor^category^district^language^showtime^length^othername^description\n')

firstLine = True
count = 1

nameMap = {}
nameMap['������'] = 'Afghanistan'
nameMap['������'] = 'Angola'
nameMap['����������'] = 'Albania'
nameMap['������'] = 'United Arab Emirates'
nameMap['����͢'] = 'Argentina'
nameMap['��������'] = 'Armenia'
nameMap['�����ϰ�����ϼ����'] = 'French Southern and Antarctic Lands'
nameMap['�Ĵ�����'] = 'Australia'
nameMap['�Ĵ����� Australia'] = 'Australia'
nameMap['�µ���'] = 'Austria'
nameMap['�����ݽ�'] = 'Azerbaijan'
nameMap['��¡��'] = 'Burundi'
nameMap['����ʱ'] = 'Belgium'
nameMap['����'] = 'Benin'
nameMap['�����ɷ���'] = 'Burkina Faso'
nameMap['�ϼ�����'] = 'Bangladesh'
nameMap['��������'] = 'Bulgaria'
nameMap['�͹���'] = 'The Bahamas'
nameMap['�͹��� Bahamas'] = 'The Bahamas'
nameMap['��˹���Ǻͺ�����ά��'] = 'Bosnia and Herzegovina'
nameMap['�׶���˹'] = 'Belarus'
nameMap['������'] = 'Belize'
nameMap['��Ľ��'] = 'Bermuda'
nameMap['����ά��'] = 'Bolivia'
nameMap['����'] = 'Brazil'
nameMap['����'] = 'Brunei'
nameMap['����'] = 'Bhutan'
nameMap['��������'] = 'Botswana'
nameMap['�зǹ��͹�'] = 'Central African Republic'
nameMap['���ô�'] = 'Canada'
nameMap['Canada'] = 'Canada'
nameMap['���ô� Canada'] = 'Canada'
nameMap['��ʿ'] = 'Switzerland'
nameMap['����'] = 'Chile'
nameMap['�й�'] = 'China'
nameMap['���'] = 'China'
nameMap['̨��'] = 'China'
nameMap['�й���½'] = 'China'
nameMap['��������'] = 'Ivory Coast'
nameMap['����¡'] = 'Cameroon'
nameMap['�չ��������͹�'] = 'Democratic Republic of the Congo'
nameMap['�չ����͹�'] = 'Republic of the Congo'
nameMap['���ױ���'] = 'Colombia'
nameMap['��˹�����'] = 'Costa Rica'
nameMap['�Ű�'] = 'Cuba'
nameMap['������·˹'] = 'Northern Cyprus'
nameMap['����·˹'] = 'Cyprus'
nameMap['�ݿ˹��͹�'] = 'Czech Republic'
nameMap['�ݿ� Czech Republic'] = 'Czech Republic'
nameMap['�ݿ�'] = 'Czech Republic'
nameMap['�¹�'] = 'Germany'
nameMap['����'] = 'Germany'
nameMap['ԭ����'] = 'Germany'
nameMap['������'] = 'Djibouti'
nameMap['����'] = 'Denmark'
nameMap['���� Denmark'] = 'Denmark'
nameMap['������ӹ��͹�'] = 'Dominican Republic'
nameMap['����������'] = 'Algeria'
nameMap['����������'] = 'Algeria'
nameMap['��϶��'] = 'Ecuador'
nameMap['����'] = 'Egypt'
nameMap['����������'] = 'Eritrea'
nameMap['������'] = 'Spain'
nameMap['��ɳ����'] = 'Estonia'
nameMap['���������'] = 'Ethiopia'
nameMap['����'] = 'Finland'
nameMap['쳼�'] = 'Fiji'
nameMap['������Ⱥ��'] = 'Falkland Islands'
nameMap['����'] = 'France'
nameMap['����'] = 'Gabon'
nameMap['Ӣ��'] = 'United Kingdom'
nameMap['UK'] = 'United Kingdom'
nameMap['��³����'] = 'Georgia'
nameMap['����'] = 'Ghana'
nameMap['������'] = 'Guinea'
nameMap['�Ա���'] = 'Gambia'
nameMap['�����Ǳ���'] = 'Guinea Bissau'
nameMap['���������'] = 'Equatorial Guinea'
nameMap['ϣ��'] = 'Greece'
nameMap['������'] = 'Greenland'
nameMap['Σ������'] = 'Guatemala'
nameMap['����������'] = 'French Guiana'
nameMap['������'] = 'Guyana'
nameMap['�鶼��˹'] = 'Honduras'
nameMap['���޵���'] = 'Croatia'
nameMap['����'] = 'Haiti'
nameMap['������'] = 'Hungary'
nameMap['ӡ��'] = 'Indonesia'
nameMap['ӡ��������'] = 'Indonesia'
nameMap['ӡ��'] = 'India'
nameMap['������'] = 'Ireland'
nameMap['����'] = 'Iran'
nameMap['������'] = 'Iraq'
nameMap['����'] = 'Iceland'
nameMap['���u Iceland'] = 'Iceland'
nameMap['��ɫ��'] = 'Israel'
nameMap['�����'] = 'Italy'
nameMap['�����'] = 'Jamaica'
nameMap['Լ��'] = 'Jordan'
nameMap['�ձ�'] = 'Japan'
nameMap['������˹̹'] = 'Kazakhstan'
nameMap['������'] = 'Kenya'
nameMap['������˹˹̹'] = 'Kyrgyzstan'
nameMap['����կ'] = 'Cambodia'
nameMap['����'] = 'South Korea'
nameMap['������'] = 'Kosovo'
nameMap['������'] = 'Kuwait'
nameMap['����'] = 'Laos'
nameMap['�����'] = 'Lebanon'
nameMap['��������'] = 'Liberia'
nameMap['������'] = 'Libya'
nameMap['˹������'] = 'Sri Lanka'
nameMap['������'] = 'Lesotho'
nameMap['������'] = 'Lithuania'
nameMap['¬ɭ��'] = 'Luxembourg'
nameMap['����ά��'] = 'Latvia'
nameMap['Ħ���'] = 'Morocco'
nameMap['Ħ������'] = 'Moldova'
nameMap['����˹��'] = 'Madagascar'
nameMap['ī����'] = 'Mexico'
nameMap['�����'] = 'Macedonia'
nameMap['����'] = 'Mali'
nameMap['���'] = 'Myanmar'
nameMap['��ɽ'] = 'Montenegro'
nameMap['�ɹ�'] = 'Mongolia'
nameMap['Īɣ�ȿ�'] = 'Mozambique'
nameMap['ë��������'] = 'Mauritania'
nameMap['����ά'] = 'Malawi'
nameMap['��������'] = 'Malaysia'
nameMap['���ױ���'] = 'Namibia'
nameMap['�¿��������'] = 'New Caledonia'
nameMap['���ն�'] = 'Niger'
nameMap['��������'] = 'Nigeria'
nameMap['�������'] = 'Nicaragua'
nameMap['����'] = 'Netherlands'
nameMap['Ų��'] = 'Norway'
nameMap['�Ჴ��'] = 'Nepal'
nameMap['������'] = 'New Zealand'
nameMap['����'] = 'Oman'
nameMap['�ͻ�˹̹'] = 'Pakistan'
nameMap['������'] = 'Panama'
nameMap['��³'] = 'Peru'
nameMap['���ɱ�'] = 'Philippines'
nameMap['�Ͳ����¼�����'] = 'Papua New Guinea'
nameMap['����'] = 'Poland'
nameMap['�������'] = 'Puerto Rico'
nameMap['������'] = 'North Korea'
nameMap['������'] = 'Portugal'
nameMap['������'] = 'Paraguay'
nameMap['������'] = 'Qatar'
nameMap['��������'] = 'Romania'
nameMap['����˹'] = 'Russia'
nameMap['����'] = 'Russia'
nameMap['¬����'] = 'Rwanda'
nameMap['��������'] = 'Western Sahara'
nameMap['ɳ�ذ�����'] = 'Saudi Arabia'
nameMap['�յ�'] = 'Sudan'
nameMap['���յ�'] = 'South Sudan'
nameMap['���ڼӶ�'] = 'Senegal'
nameMap['������Ⱥ��'] = 'Solomon Islands'
nameMap['��������'] = 'Sierra Leone'
nameMap['�����߶�'] = 'El Salvador'
nameMap['��������'] = 'Somaliland'
nameMap['������'] = 'Somalia'
nameMap['����ά�ǹ��͹�'] = 'Republic of Serbia'
nameMap['������'] = 'Suriname'
nameMap['˹�工��'] = 'Slovakia'
nameMap['�ݿ�˹�工��'] = 'Slovakia'
nameMap['�ݿ�˹�工�� Czechoslovakia'] = 'Slovakia'
nameMap['˹��������'] = 'Slovenia'
nameMap['���'] = 'Sweden'
nameMap['˹��ʿ��'] = 'Swaziland'
nameMap['������'] = 'Syria'
nameMap['է��'] = 'Chad'
nameMap['���'] = 'Togo'
nameMap['̩��'] = 'Thailand'
nameMap['������˹̹'] = 'Tajikistan'
nameMap['������˹̹'] = 'Turkmenistan'
nameMap['������'] = 'East Timor'
nameMap['�������Ͷ�͸�'] = 'Trinidad and Tobago'
nameMap['ͻ��˹'] = 'Tunisia'
nameMap['������'] = 'Turkey'
nameMap['̹ɣ�������Ϲ��͹�'] = 'United Republic of Tanzania'
nameMap['�ڸɴ�'] = 'Uganda'
nameMap['�ڿ���'] = 'Ukraine'
nameMap['������'] = 'Uruguay'
nameMap['����'] = 'United States of America'
nameMap['USA'] = 'United States of America'
nameMap['���ȱ��˹̹'] = 'Uzbekistan'
nameMap['ί������'] = 'Venezuela'
nameMap['Խ��'] = 'Vietnam'
nameMap['��Ŭ��ͼ'] = 'Vanuatu'
nameMap['����'] = 'West Bank'
nameMap['Ҳ��'] = 'Yemen'
nameMap['�Ϸ�'] = 'South Africa'
nameMap['�ޱ���'] = 'Zambia'
nameMap['��Ͳ�Τ'] = 'Zimbabwe'

for line in fr:
    if firstLine:
        firstLine = False
        continue
    
    line = line.split('^')   # ���ļ���ÿ�е�Ӱ��Ϣ����^���ž����и�
    
    movieId = line[0]
    title = line[1]
    url = line[2]
    cover = line[3]
    rate = line[4]
    director = line[5]
    
    composer = line[6].split('/')
    temp = ''
    for item in composer:
        temp = temp + item.strip() + '/'
    composer = temp[:-1]
    
    actor = line[7].split('/')
    temp = ''
    for item in actor:
        temp = temp + item.strip() + '/'
    actor = temp[:-1]
    
    category = line[8].split('/')
    temp = ''
    for item in category:
        temp = temp + item.strip() + '/'
    category = temp[:-1]
    
    district = line[9].split('/')
    temp = ''
    for item in district:
        if item.strip() not in nameMap:
            continue
        temp = temp + nameMap[item.strip()] + '_' + item.strip() + '/'
    district = temp[:-1]
    if len(district) == 0:
        district = "δ֪����"
        
    language = line[10].split('/')
    temp = ''
    for item in language:
        temp = temp + item.strip() + '/'
    language = temp[:-1]
    
    showtime = line[11].split('/')[0][:4]
    
    length = line[12].split('/')[0]
    length = length.strip()
    for x in range(0, len(length)-1):
        if length[x].isdigit():
            continue
        else:
            length = length[:x]
            break
    
    othername = line[13].split('/')
    temp = ''
    for item in othername:
        temp = temp + item.strip() + '/'
    othername = temp[:-1]
    
    description = line[14].split('\t')
    temp = ''
    for item in description:
        item = item.strip().strip('\t')
        if not item == '':
            temp = temp + item + '/'
    description = temp[:-1]
    
    record = movieId + '^' + title + '^' + url + '^' + cover + '^' + rate + '^' + director + '^' + composer + '^' + actor + '^' + category + '^' + district + '^' + language + '^' + showtime + '^' + length + '^' + othername + '^' + description + '\n'
    fw.write(record)
    
    print(count, title)
    count = count + 1
    
fr.close()
fw.close()