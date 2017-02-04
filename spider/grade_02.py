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
reload(sys)
sys.setdefaultencoding("utf-8")
cookie = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

CaptchaUrl = "http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS"
PostUrl = "http://jw.hrbeu.edu.cn/ACTIONLOGON.APPPROCESS"
GradeUrl = 'http://jw.hrbeu.edu.cn/ACTIONQUERYSTUDENTSCORE.APPPROCESS'
weights = []
points = []

#用openr的访问验证码地址，获取cookie
picture = opener.open(CaptchaUrl).read()
#保存验证码到本地
local = open('/root/Spider/qsbk/SC/image.jpg','wb')
local.write(picture)
local.close()
#打开保存的验证码图片输入
SecretCode = raw_input('Please input the SecretCode:')

#需要POST的数据#
postdata=urllib.urlencode({  
    'WebUserNO':'2013061106',  
    'Password':'6866223'  ,
	'Agnomen': SecretCode,
	'submit.x':'24',
	'submit.y':'2',
	'applicant':'ACTIONQUERYSTUDENTSCORE'
})
#自定义一个请求#
req = urllib2.Request(  
    url = PostUrl,  
    data = postdata
)
#访问该链接#
result = opener.open(req)
result = opener.open(GradeUrl)
#打印返回的内容
#print result.read().decode('gb2312')
m = re.findall('<tr.*?class="color-row"><td.*?<td.*?\d+</td></tr>',result.read())
print m

   