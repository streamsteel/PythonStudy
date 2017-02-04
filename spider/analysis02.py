# -*- coding: utf-8 -*-
#---------------------------------------
#   ���򣺹��������̴�ѧ����
#   �汾��1.0
#   ���ߣ�hzz
#   ���ڣ�2
#   ���ԣ�Python 2.7
#   ����������ѧ�ź�����
#   ���ܣ�����ɼ��ļ�Ȩƽ��ֵҲ���Ǽ���
#---------------------------------------

import urllib  
import urllib2
import cookielib
import sys
import re
import string

class HEU:

	#��ĳ�ʼ��
	def __init__(self):
		#��¼URL
		self.loginUrl = 'http://jw.hrbeu.edu.cn/ACTIONLOGON.APPPROCESS'
		#��ѧ�ڳɼ�URL
		self.gradeUrl = 'http://jw.hrbeu.edu.cn/ACTIONQUERYSTUDENTSCORE.APPPROCESS'
		#��֤��URL
		self.captchaUrl = 'http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS'
		#CookieJar����
		self.cookies = cookielib.CookieJar()
		#����opener
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
		#��openr�ķ�����֤���ַ����ȡcookie
		self.picture = self.opener.open(self.captchaUrl).read()
		#������֤�뵽����
		self.local = open('/root/Spider/qsbk/SC/image.jpg','wb')
		self.local.write(self.picture)
		self.local.close()
		#�򿪱������֤��ͼƬ����
		self.SecretCode = raw_input('Please input the SecretCode:')
		#������
		self.postdata = urllib.urlencode({
			'WebUserNO':'2013061106',  
			'Password':'6866223'  ,
			'Agnomen': self.SecretCode,
			'submit.x':'24',
			'submit.y':'2',
			'applicant':'ACTIONQUERYSTUDENTSCORE'
		})
		##����opener
		##self.opener = urllib2.Request(self.req)
		#ѧ��list
		self.credit = []
		#�ɼ�list
		self.grades = []
		
	def getPage(self):
		req = urllib2.Request(
			url = self.loginUrl,  
			data = self.postdata
		)
		result = self.opener.open(req)
		result = self.opener.open(self.gradeUrl)
		#���ر�ѧ��ҳ��
		#return result.read().decode('gbk')
		self.getGrades(result.read().decode('gbk'))
		self.getGrade();
		
	def getGrades(self,page):
		#��ñ�ѧ�ڳɼ�ҳ��
		#page = self.getPage()
		#����ƥ��
		myItems = re.findall('<tr.*?class="color-row">\n.*?<td.*?\n.*?<td.*?\n.*?<td.*?\n.*?<td.*?\n.*?<td.*?\n.*?<td.*?>(.*?)</td>\n.*?<td.*?\n.*?<td.*?\n.*?<td.*?>(\d*)</td>\n.*?</tr>',page,re.S)
		for item in myItems:
			self.credit.append(item[0].encode('gbk'))
			self.grades.append(item[1].encode('gbk'))
		
	def getGrade(self):
		#�����ܼ���
		sum = 0.0
		weight = 0.0
		for i in range(len(self.credit)):
			if(self.grades[i].isdigit()):
				sum += string.atof(self.credit[i])*string.atof(self.grades[i])
				weight += string.atof(self.credit[i])
		try:		
			print "JiDian is:",sum/weight
		except ZeroDivisionError:
			print "The weight is zero!"
	
		
heu = HEU()
heu.getPage()