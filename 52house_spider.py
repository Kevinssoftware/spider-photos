from lxml import etree
import requests
import os

def onepage_spider (a):
    if (a==0):
        url = 'http://pic.netbian.com/4kmeinv/'
    else:
        url = f'https://pic.netbian.com/4kmeinv/index_{a}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47'
    }
    yemian = requests.get(url = url,headers = headers)
    yemian.encoding = 'gbk'
    tree = etree.HTML(yemian.text)
    lists = tree.xpath('//*[@id="main"]/div[3]/ul/li')
    if not os.path.exists('./photo'):
        os.mkdir('./photo')

    for list in lists:
        url = list.xpath('./a/img/@src')[0]
        name = list.xpath('./a/b/text()')[0]
        img_url = "http://pic.netbian.com"+str(url)
        # print(name)
        # print(img_url)
        img_data = requests.get(url=img_url,headers=headers).content
        img_path = 'photo/'+name+'.jpg'
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(name+"successful")

if __name__ == '__main__':
    for a in range(0,70):
        onepage_spider(a)
    print("彻底结束")