#�ڰ���
#8.3 ����������αװ����ʵս
#(1)
import urllib.request
import http.cookiejar
url= "http://news.163.com/16/0825/09/BVA8A9U500014SEH.html"
cjar=http.cookiejar.CookieJar()
proxy= urllib.request.ProxyHandler({'http':"127.0.0.1:8888"})  
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
fhandle=open("D:/Python35/myweb/part8/1.html","wb")
fhandle.write(data)
fhandle.close()

#(2)
import urllib.request
import http.cookiejar
url= "http://news.163.com/16/0825/09/BVA8A9U500014SEH.html"
#���ֵ����ʽ����headers
headers={ "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language":" zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
                        "Connection": "keep-alive",
                        "referer":"http://www.163.com/"}
#����cookie
cjar=http.cookiejar.CookieJar()
proxy= urllib.request.ProxyHandler({'http':"127.0.0.1:8888"})  
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cjar))
#�������б�Ϊ����ָ����ʽ�洢ͷ��Ϣ
headall=[]
#ͨ��forѭ�������ֵ䣬�����ָ����ʽ��headers��Ϣ
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
#��ָ����ʽ��headers��Ϣ��Ӻ�
opener.addheaders = headall
#��opener��װΪȫ��
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
fhandle=open("D:/Python35/myweb/part8/2.html","wb")
fhandle.write(data)
fhandle.close()

#(3)
import urllib.request
import http.cookiejar
#ע�⣬���Ҫͨ��fiddler���ԣ����·���ַҪ����Ϊ"http://www.baidu.com/"
url= "http://www.baidu.com"
headers={ "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Encoding":" gb2312,utf-8",
                        "Accept-Language":" zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
                          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
                        "Connection": "keep-alive",
                        "referer":"baidu.com"}
cjar=http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
fhandle=open("D:/Python35/myweb/part8/3.html","wb")
fhandle.write(data)
fhandle.close()

