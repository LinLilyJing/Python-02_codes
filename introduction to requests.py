# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:21:16 2016

@author: chen
"""


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import requests

#---------------------------------------------------------------
#Make a request

#get method
r = requests.get('http://esf.xm.fang.com/house/i32/')

#post method
'''
headers_2 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'cookie':cookie,
            'Host': 'www.landchina.com',
            'Origin': 'http://www.landchina.com',
            'Referer': 'http://www.landchina.com/default.aspx?tabid=263&wmguid=75c72564-ffd9-426a-954b-8ac2df0903b7&p=9f2c3acd-0256-4da2-a659-6949c4671a2a%3A'+str(self.start_time)+'~'+str(self.end_time),
            'Upgrade-Insecure-Requests': '1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.21 Safari/537.36',
            #'http':proxy,

        }

data = {
            'VIEWSTATE': '/wEPDwUJNjkzNzgyNTU4D2QWAmYPZBYIZg9kFgICAQ9kFgJmDxYCHgdWaXNpYmxlaGQCAQ9kFgICAQ8WAh4Fc3R5bGUFIEJBQ0tHUk9VTkQtQ09MT1I6I2YzZjVmNztDT0xPUjo7ZAICD2QWAgIBD2QWAmYPZBYCZg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHgRUZXh0ZWRkAgEPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFhwFDT0xPUjojRDNEM0QzO0JBQ0tHUk9VTkQtQ09MT1I6O0JBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bHQvVXBsb2FkL3N5c0ZyYW1lSW1nL3hfdGRzY3dfc3lfamhnZ18wMDAuZ2lmKTseBmhlaWdodAUBMxYCZg9kFgICAQ9kFgJmDw8WAh8CZWRkAgIPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPZBYEZg9kFgJmDxYEHwEFIENPTE9SOiNEM0QzRDM7QkFDS0dST1VORC1DT0xPUjo7HwBoFgJmD2QWAgIBD2QWAmYPDxYCHwJlZGQCAg9kFgJmD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCZg9kFgJmD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAICD2QWBGYPZBYCZg9kFgJmD2QWAmYPZBYCAgEPZBYCZg8WBB8BBYYBQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjtCQUNLR1JPVU5ELUlNQUdFOnVybChodHRwOi8vd3d3LmxhbmRjaGluYS5jb20vVXNlci9kZWZhdWx0L1VwbG9hZC9zeXNGcmFtZUltZy94X3Rkc2N3X3p5X2pnZ2dfMDEuZ2lmKTsfAwUCNDYWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIBD2QWAmYPZBYCZg9kFgJmD2QWAgIBD2QWAmYPFgQfAQUgQ09MT1I6I0QzRDNEMztCQUNLR1JPVU5ELUNPTE9SOjsfAGgWAmYPZBYCAgEPZBYCZg8PFgIfAmVkZAIDD2QWAgIDDxYEHglpbm5lcmh0bWwFtwY8cCBhbGlnbj0iY2VudGVyIj48c3BhbiBzdHlsZT0iZm9udC1zaXplOiB4LXNtYWxsIj4mbmJzcDs8YnIgLz4NCiZuYnNwOzxhIHRhcmdldD0iX3NlbGYiIGhyZWY9Imh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS8iPjxpbWcgYm9yZGVyPSIwIiBhbHQ9IiIgd2lkdGg9IjI2MCIgaGVpZ2h0PSI2MSIgc3JjPSIvVXNlci9kZWZhdWx0L1VwbG9hZC9mY2svaW1hZ2UvdGRzY3dfbG9nZS5wbmciIC8+PC9hPiZuYnNwOzxiciAvPg0KJm5ic3A7PHNwYW4gc3R5bGU9ImNvbG9yOiAjZmZmZmZmIj5Db3B5cmlnaHQgMjAwOC0yMDE0IERSQ25ldC4gQWxsIFJpZ2h0cyBSZXNlcnZlZCZuYnNwOyZuYnNwOyZuYnNwOyA8c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCI+DQp2YXIgX2JkaG1Qcm90b2NvbCA9ICgoImh0dHBzOiIgPT0gZG9jdW1lbnQubG9jYXRpb24ucHJvdG9jb2wpID8gIiBodHRwczovLyIgOiAiIGh0dHA6Ly8iKTsNCmRvY3VtZW50LndyaXRlKHVuZXNjYXBlKCIlM0NzY3JpcHQgc3JjPSciICsgX2JkaG1Qcm90b2NvbCArICJobS5iYWlkdS5jb20vaC5qcyUzRjgzODUzODU5YzcyNDdjNWIwM2I1Mjc4OTQ2MjJkM2ZhJyB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnJTNFJTNDL3NjcmlwdCUzRSIpKTsNCjwvc2NyaXB0PiZuYnNwOzxiciAvPg0K54mI5p2D5omA5pyJJm5ic3A7IOS4reWbveWcn+WcsOW4guWcuue9kTxiciAvPg0K5aSH5qGI5Y+3OiDkuqxJQ1DlpIcwOTA3NDk5MuWPtyDkuqzlhaznvZHlronlpIcxMTAxMDIwMDA2NjYoMikmbmJzcDs8YnIgLz4NCjwvc3Bhbj4mbmJzcDsmbmJzcDsmbmJzcDs8YnIgLz4NCiZuYnNwOzwvc3Bhbj48L3A+HwEFZEJBQ0tHUk9VTkQtSU1BR0U6dXJsKGh0dHA6Ly93d3cubGFuZGNoaW5hLmNvbS9Vc2VyL2RlZmF1bHQvVXBsb2FkL3N5c0ZyYW1lSW1nL3hfdGRzY3cyMDEzX3l3XzEuanBnKTtkZFgrT4ZXzyk2fvKb+ZQdNgDE7amPUgf1dsAbA0tQEzbS',
            '__EVENTVALIDATION': '/wEWAgKNgPHpAgLN3cj/BMeqdKR8EqyZqeFW25/wiD3Dqo+sG7dks/liloBmr6j/',
            'hidComName': 'default',
            'TAB_QueryConditionItem': '9f2c3acd-0256-4da2-a659-6949c4671a2a',
            'TAB_QuerySortItemList': '282:False',
            'TAB_QuerySubmitConditionData': '9f2c3acd-0256-4da2-a659-6949c4671a2a:'+str(self.start_time)+'~'+str(self.end_time),
            'TAB_RowButtonActionControl': '',
            'TAB_QuerySubmitPagerData': str(self.page),
            'TAB_QuerySubmitSortData': ''
        }
requests.post(self.url, data, headers=headers_2,cookies=self.cookie)
'''

#---------------------------------------------------------------
#Response Content
print len(r.content)
print len(r.text)
print r.encoding



#-----------------------------------------------------------------
#Passing Parameters In URLs
parameters= {'keyword': 'T-shirt', 'enc': 'utf-8',"cid3":"1349"}
p = requests.get("http://search.jd.com/search", params=parameters)
print (p.url)



#-----------------------------------------------------------------
#parsing JSON
location = '厦门大学经济学院'
url_1 = 'http://apis.map.qq.com/ws/geocoder/v1/?address='
url_2 = urllib.unquote(location)
url_3 = '&key='
url_4 = ''
url = ''.join([url_1,url_2,url_3,url_4])
print requests.get(url).content
print requests.get(url).json()
print type(requests.get(url).json())
print requests.get(url).json()['result']['title']
l = eval(requests.get(url).content)
print type(l)
print l['result']['title']
#-----------------------------------------------------------------
#Headers,Proxies,timeout
headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'cookie':cookie,
            #'Host': '',
            #'Origin': '',
            #'Referer': ',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.21 Safari/537.36',


        }
#q = requests.get('http://esf.xm.fang.com/house/i32/',headers=headers,timeout=10)
#q = requests.get('http://esf.xm.fang.com/house/i32/',headers=headers,timeout=10,proxies={})


#-----------------------------------------------------------------
#Session
#s = requests.session()
#login_data={"account":"","password":""}
#res=s.post("http://mail.163.com/",login_data)
#print res.status_code
#print res.content
#print res.headers
#print res.cookies
#print res.json()


