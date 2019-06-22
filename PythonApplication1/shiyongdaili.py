import requests
import re

def get_html(url):
    proxy = {
        'http': '120.25.253.234:812',
        'https' '163.125.222.244:8123'
    }
    heads = {}
    heads['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    req = requests.get(url, headers=heads,proxies=proxy)
    html = req.text
    return html

def get_ipport(html):
    regex = r'<td data-title="IP">(.+)</td>'
    iplist = re.findall(regex, html)
    regex2 = '<td data-title="PORT">(.+)</td>'
    portlist = re.findall(regex2, html)
    regex3 = r'<td data-title="类型">(.+)</td>'
    typelist = re.findall(regex3, html)
    sumray = []
    for i in iplist:
        for p in portlist:
            for t in typelist:
                pass
            pass
        a = t+','+i + ':' + p
        sumray.append(a)
    print('高匿代理')
    print(sumray)


if __name__ == '__main__':
    url = 'http://www.kuaidaili.com/free/'
    get_ipport(get_html(url))
