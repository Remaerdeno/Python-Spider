import requests
import re
from bs4 import BeautifulSoup
import os
url='http://lol.qq.com/biz/hero/champion.js'
def get_hero_name(url):
    head={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36'}
    html=requests.get(url,headers=head)
    html_json=html.json()
    hero_name=html_json['data'].keys()
    list_of_nameMax=list(hero_name)
    list_of_nameMin=[]
    for ii in list_of_nameMax:
        name=ii.lower()
        list_of_nameMin.append(name)
        return list_of_nameMin
def get_onehero_img(name):
    url2='http://lol.qq.com/web201310/info-defail.shtml?id'+name+'/'
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    html=requests.get(url,headers=head)
    contents=html.text
    soup=BeautifulSoup(contents)
    hero_img=soup.findAll('img')
    reg=re.compile(r'"http://ossweb-img.qq.com/images/lol/web201310/skin/.*?.jpg"',re.S)
    hero_img_links=re.findall(reg,str(hero_img))
    return hero_img_links
def main():
    list_name=list_of_name
    for i in list_name:
        os.makedirs('F:/爬虫/英雄联盟图片/'+i)
        os.chdir('F:/爬虫/英雄联盟图片/'+i)
        ashe=get_onehero_img(i)
        for j in ashe:
            im=re.sub('"','',j)
            ir=requests.get(im)
            if ir.status_code==200:
                ip=re.sub('"','',j)
                iu=re.split('/',im)
                open(iu[-1],'wb').write(ir.content)
if __name__ == '__main__':

    list_of_name=get_hero_name(url)
    main()
