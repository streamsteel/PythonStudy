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
reload(sys)
sys.setdefaultencoding("utf-8")
cookie = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

CaptchaUrl = "http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS"
PostUrl = "http://jw.hrbeu.edu.cn/ACTIONLOGON.APPPROCESS"
GradeUrl = 'http://jw.hrbeu.edu.cn/ACTIONQUERYSTUDENTSCORE.APPPROCESS'
weights = []
points = []

#��openr�ķ�����֤���ַ����ȡcookie
picture = opener.open(CaptchaUrl).read()
#������֤�뵽����
local = open('/root/Spider/qsbk/SC/image.jpg','wb')
local.write(picture)
local.close()
#�򿪱������֤��ͼƬ����
SecretCode = raw_input('Please input the SecretCode:')

#��ҪPOST������#
postdata=urllib.urlencode({  
    'WebUserNO':'2013061106',  
    'Password':'6866223'  ,
	'Agnomen': SecretCode,
	'submit.x':'24',
	'submit.y':'2',
	'applicant':'ACTIONQUERYSTUDENTSCORE'
})
#�Զ���һ������#
req = urllib2.Request(  
    url = PostUrl,  
    data = postdata
)
#���ʸ�����#
result = opener.open(req)
result = opener.open(GradeUrl)
#��ӡ���ص�����
#print result.read().decode('gb2312')
m = re.findall('<tr.*?class="color-row"><td.*?<td.*?\d+</td></tr>',result.read())
print m

   