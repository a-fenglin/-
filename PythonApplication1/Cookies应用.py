import requests

headers = {
    'Cookie': '_xsrf=afLj8anMnzgAdrUcHtqylVWAOHAOG0Vu; _zap=69ad56fa-0256-484f-ad33-4657c94d38ce; d_c0="ADDtQUfHng-PTsb2DCxOMB74xltgxNNaOG0=|1561133477"; tst=r; q_c1=786e4f503be7448493f63b314f874a2c|1561133528000|1561133528000; tgw_l7_route=578107ff0d4b4f191be329db6089ff48; __gads=ID=1130b606d83533e8:T=1561134851:S=ALNI_MY_i6WpTenzR_2Cq2YR243y4MBtlA; capsion_ticket="2|1:0|10:1561135471|14:capsion_ticket|44:OWUzNDE0ZjYwYjM3NDAzMWJmMjNmNmNkM2M5NmVkMTY=|88e6d2fe678309c3dba3b2a85bc358cefcc086809a6daf02b5fd1d5bab54ffd3"; z_c0="2|1:0|10:1561135499|4:z_c0|92:Mi4xSVNSWEN3QUFBQUFBTU8xQlI4ZWVEeWNBQUFDRUFsVk5pNVkwWFFCUkdLRVBBYzhfblZLbjdHb1o3X3lxYkVhd3VB|05213ba7ffd99ae1675d4143d6682f9833897ac27cced8032b5cb235f1574b07"',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)

