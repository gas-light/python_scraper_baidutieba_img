#爬取表情包
import requests
import re
urls=['https://tieba.baidu.com/p/4180627025?see_lz=1&pn={}'.format(m) for m in range(1,2)]
#urls=['https://tieba.baidu.com/p/4560066715?see_lz=1']
#response=requests.get(url)
header={
"User-Agent": "Mozilla/5.0 "
              "(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}
#print(response)
#response403,没有权限，因此要模拟浏览器客户端
def get_img(url,n):
 response = requests.get(url, headers=header).text

 #print(response)
 #要筛选数据，并提取下载-re

 image_info = re.findall("[a-zA-z]+://[^\s]*.jpg",response)
 #print(image_info)

 for i in range(0,len(image_info)):
   print(image_info[i],n)
   image_content=requests.get(image_info[i], headers=header).content
   if n<=9:
        with open('image_3/'+'00'+str(n)+'.jpg',"wb") as f:
         f.write(image_content)

   elif n>9 and n<99:
        with open('image_3/'+'0'+str(n)+'.jpg',"wb") as f:
         f.write(image_content)
   else:
        with open('image_3/' + str(n) + '.jpg', "wb") as f:
         f.write(image_content)
   n=n+1
 return n

if __name__=='__main__':
    n=1
    for m in range(0,len(urls)):
        n=get_img(urls[m],n)
        print('第'+str(m+1)+'页已打印')





