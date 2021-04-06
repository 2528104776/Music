#!/usr/bin/python
import urllib.parse,requests,re,os;
try:
    import requests
except:
    print('please wait...')
    os.system("pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple")


msg = input("在线模式:0,下载模式:1,请输入对应数字:")


# ------------------------配置参数---------------------------------
values={}
values['key']=input("请输入歌曲名称或者歌手名字:")
values['pn']='1'
values['rn']='30'
values['httpsStatus']='1'
values['reqId']='cc337fa0-e856-11ea-8e2d-ab61b365fb50'
param=urllib.parse.urlencode(values)
url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?'+param
rids = [];name =[]
reqid = '';real_url = '';file_name = '';

headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63",
        "Cookie":"_ga=GA1.2.1083049585.1590317697; _gid=GA1.2.2053211683.1598526974; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1597491567,1598094297,1598096480,1598526974; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1598526974; kw_token=HYZQI4KPK3P",
        "Referer": "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
        "csrf": "HYZQI4KPK3P"}

def parse():
    try:
        global real_url;global name;global reqid;global file_name;
        r=requests.get(url,headers = headers)
        r.encoding = 'utf-8'
# -------------------------解析歌手名字，歌曲名字-----------------------------
        item = r.json()['data']['list']
        for index,i in enumerate(range(len(item))):
            actor = r.json()['data']['list'][i]['artist']
            music_name = r.json()['data']['list'][i]['name']
            print(index,actor,music_name)
            name.append(music_name)
            
# ------------------------提取关键参数-----------------------------------------------            
        for rid in re.findall('\d+(?=,"duration")',r.text):
            rids.append(rid)
        for i in re.findall('(?<=","reqId":")(.*)(?="})',r.text):
            reqid+=i
# ------------------------重新拼装url-------------------------------------------------
        string = input("请输入对应序号的歌曲:")
        num = int(string)
        link = 'https://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&httpsStatus=1&reqId={}'.format(rids[num],reqid)
        res = requests.get(link)
        real_url = res.json()['url']
        real_url = real_url;
        file_name = name[num]
    except:
        print("请求失败，检查歌曲名称重试。")

def online():
    os.system("mpv %s"%(real_url))


def download():
        print(real_url)
        down = requests.get(real_url)
        root = '/storage/emulated/0/%s.mp3'%(file_name)
        with open(root,'ab')as file:
            file.write(down.content)
            print("下载成功,请前往手机根目录前往查看.")
  
def main():
    parse()
    if msg=="0":
        online()
    elif msg =="1":
        download()
    else:
        print("输入错误！")


        
if __name__ =='__main__':
    main()



    

