#! python3
#! imgurDL.py - Downloads the first 20 images from search on imgur

import requests, os, bs4
search = str(input('Request an image: '))
url = 'https://imgur.com/search/score?q=' + search
os.makedirs('imgur', exist_ok=True)

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
imgLink = soup.select('a img')

n=20
breakFlag = 0

if len(imgLink) == 0:
        print('imgur found 0 results, try another search term.')
        breakFlag = 1
if len(imgLink) < 20:
    n = len(imgLink)

if breakFlag == 0:    
    for imageNo in range(n):
        print('Downloading image no.'+str(imageNo+1)+'...')
        
        imgUrl = 'http:'+imgLink[imageNo].get('src') 
        imgRes = requests.get(imgUrl)
        imgFile = open(os.path.join('imgur', os.path.basename(imgUrl)), 'wb')
        for chunk in imgRes.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()

print('Done!')
    
    
    
