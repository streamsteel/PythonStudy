# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：哈尔滨工程大学爬虫
#   版本：1.0
#   作者：hzz
#   日期：2
#   语言：Python 2.7
#   操作：输入学号和密码
#   功能：输出成绩的加权平均值也就是绩点
#---------------------------------------

import urllib  
import urllib2
import cookielib
import sys
import re
import string

class HEU:

	#类的初始化
	def __init__(self):
		#登录URL
		self.loginUrl = 'http://jw.hrbeu.edu.cn/ACTIONLOGON.APPPROCESS'
		#本学期成绩URL
		self.gradeUrl = 'http://jw.hrbeu.edu.cn/ACTIONQUERYSTUDENTSCORE.APPPROCESS'
		#验证码URL
		self.captchaUrl = 'http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS'
		#CookieJar对象
		self.cookies = cookielib.CookieJar()
		#构建opener
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
		#用openr的访问验证码地址，获取cookie
		self.picture = self.opener.open(self.captchaUrl).read()
		#保存验证码到本地
		self.local = open('/root/Spider/qsbk/SC/image.jpg','wb')
		self.local.write(self.picture)
		self.local.close()
		#打开保存的验证码图片输入
		self.SecretCode = raw_input('Please input the SecretCode:')
		#表单数据
		self.postdata = urllib.urlencode({
			'WebUserNO':'2013061106',  
			'Password':'6866223'  ,
			'Agnomen': self.SecretCode,
			'submit.x':'24',
			'submit.y':'2',
			'applicant':'ACTIONQUERYSTUDENTSCORE'
		})
		##构建opener
		##self.opener = urllib2.Request(self.req)
		#学分list
		self.credit = []
		#成绩list
		self.grades = []
		
	def getPage(self):
		req = urllib2.Request(
			url = self.loginUrl,  
			data = self.postdata
		)
		result = self.opener.open(req)
		result = self.opener.open(self.gradeUrl)
		#返回本学期页面
		#return result.read().decode('gbk')
		self.getGrades(result.read().decode('gbk'))
		self.getGrade();
		
	def getGrades(self,page):
		#获得本学期成绩页面
		#page = self.getPage()
		#正则匹配
		myItems = re.findall('<tr.*?class="color-row">\n.*?<td.*?\n.*?<td.*?\n.*?<td.*?\n.*?<td.*?\n.*?<td.*?\n.*?<td.*?>(.*?)</td>\n.*?<td.*?\n.*?<td.*?\n.*?<td.*?>(\d*)</td>\n.*?</tr>',page,re.S)
		for item in myItems:
			self.credit.append(item[0].encode('gbk'))
			self.grades.append(item[1].encode('gbk'))
		
	def getGrade(self):
		#计算总绩点
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