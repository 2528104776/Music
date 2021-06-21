#!/usr/bin/python
import urllib.parse,requests,re
def parse(music_name):
    values = {}
    values['key'] = music_name
    values['pn'] = '1'
    values['rn'] = '30'
    values['httpsStatus'] = '1'
    values['reqId'] = 'cc337fa0-e856-11ea-8e2d-ab61b365fb50'
    param = urllib.parse.urlencode(values)
    url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?' + param
    rids = [];
    reqid = '';
    real_url = '';
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63",
        "Cookie": "_ga=GA1.2.1083049585.1590317697; _gid=GA1.2.2053211683.1598526974; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1597491567,1598094297,1598096480,1598526974; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1598526974; kw_token=HYZQI4KPK3P",
        "Referer": "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
        "csrf": "HYZQI4KPK3P"}
    try:
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'
        for rid in re.findall('\d+(?=,"duration")', r.text):
            rids.append(rid)
        for i in re.findall('(?<=","reqId":")(.*)(?="})', r.text):
            reqid += i
        # ------------------------重新拼装url-------------------------------------------------
        link = 'https://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&httpsStatus=1&reqId={}'.format(rids[0], reqid)
        res = requests.get(link)
        real_url = res.json()['url']
        print(real_url)
        return real_url
    except:
        print("请求失败，检查歌曲名称重试。")
