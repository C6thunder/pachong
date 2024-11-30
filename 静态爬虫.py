import requests
from bs4 import BeautifulSoup
import time
import os
from urllib.request import urlretrieve
from PIL import Image
from io import BytesIO



headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

res = requests.get('http://www.acgzyj.com/meitu/2158.html', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')


if not os.path.exists('./testp1'):  #如果没有 储存文件 则创建一个
    os.mkdir('./testp1')


items = soup.find_all("a",rel="nofollow") 

# print(items)

n = 0
for i in items:
    # print(i)
    n += 1
    if(n<=10):
        continue
    href = i["href"]
    if(n==20):
        break

    
    # print(href)
    print('http://www.acgzyj.com'+ href)

    out_url = 'http://www.acgzyj.com'+ href   


    res = requests.get(out_url, headers=headers)
    soupm = BeautifulSoup(res.text, 'html.parser')

    item = soupm.select(".art-content img")


    p = 1
    for l in item:
        print(l)
        src = l["src"]

        alt = l["alt"]
        
        # print(src)

        print('http://www.acgzyj.com'+ src)

        website_url = 'http://www.acgzyj.com'+ src  


        #筛选.jpg
        if website_url.lower().endswith('.jpg'):

            image_url = website_url 
        else:
            continue            


        #如果没有alt则创建一个  为了分类储存
        if not os.path.exists('./testp1/' + alt):
            os.mkdir('./testp1/' + alt)

        # 本地保存的路径和文件名
        save_path = './testp1/' + alt +"/" + alt + str(p) + '.jpg'
        p += 1

        # 加延迟
        time.sleep(0.2)

        try:
            response = requests.get(image_url,headers=headers)
            response.raise_for_status()
            image_data = BytesIO(response.content)
            image = Image.open(image_data)
            
            #图像保存路径
            image.save(save_path)
            print(f"图片已成功保存到"+ save_path)
        except requests.RequestException as e:
            print(f"下载图片时出错: {e}")



