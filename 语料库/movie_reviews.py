#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import bs4

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
os.environ['NLS_LANG'] = 'Simplified Chinese_CHINA.ZHS16GBK'
#以上用来确保读写文件时编码正确

f = open('疯狂的外星人'.encode('GBK', 'ignore') + '1-5.txt', 'a')
final_page = 5
start_page = 0

proxies = {'https':'https://106.75.71.140:16817'}
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}

try:
	for j in range(start_page, final_page):
		print "in pages" + str(j)
		url = 'https://movie.douban.com/subject/25986662/reviews?start=' + str(j * 20)
		try:	
			r = requests.get(url, headers = header, proxies=proxies, timeout = 5)
		except:
			print 'time out, retry...'
			try:
				r = requests.get(url, headers = header, proxies=proxies, timeout = 5)
			except:
				print 'time out twice, the ip is going to be forbidden'
				try:
					r = requests.get(url, headers = header, proxies=proxies, timeout = 5)
				except:
					r = requests.get(url, headers = header, proxies=proxies, timeout = 5)
					print 'time out three times, the ip is going to be forbidden!'
		r.encoding = r.apparent_encoding
		soup = BeautifulSoup(r.text, 'lxml')
		
		
		for i in range(0,20):
			url1 = soup.find_all('h2')[i].a.attrs['href']
			try:
				r_in = requests.get(url1, headers = header, proxies=proxies, timeout = 5)
			except:
				print 'inner time out, retry...'
				try:
					r_in = requests.get(url1, headers = header, proxies=proxies, timeout = 5)
				except:
					print 'inner time out twice, the ip is going to be forbidden'
					try:
						r = requests.get(url, headers = header, proxies=proxies, timeout = 5)
					except:
						r = requests.get(url, headers = header, proxies=proxies, timeout = 5)
						print 'time out three times, the ip is going to be forbidden!'
			soup1 = BeautifulSoup(r_in.text, 'lxml')
			review = soup1.find_all(class_ = "review-content clearfix")[0]
		
			for child in review.children:
				if(child.name == 'p'):
					try:
						f.write(child.string.decode('utf-8').encode('GBK', 'ignore'))
					except:
						print '',
				if(isinstance(child, bs4.element.Tag)):
					f.write('')
				else:
					f.write(child.decode('utf-8').encode('GBK', 'ignore'))
			f.write('=========================================================================')
			print 'page' + str(i+1) + 'over' + 'url =' + url1
except:		
	f.close()


