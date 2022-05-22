from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

baseUrl = 'https://www.instagram.com/explore/tags/'
plusUrl = input('검색할 태그')
url = baseUrl + quote_plus((plusUrl))
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html)

# select는 페이지에 있는 정보를 다 가져 온다.
# 클래스가 여러 개면 기존 클래스의 공백을 없애고 .으로 연결시켜 주어야 한다.

insta = soup.select('.v1Nh3.kIKUG._bz0w')
n=1

#여러개의 이미지를 가져올 것
for i in insta:
    print('https://www.instagram.com' + i.a['href'])
    imgUrl = i.select_one('.KL4Bh').img['src']
    with urlopen(imgUrl) as f:

        with open('./img/' + plusUrl + str(n) + '.jpg', "wb") as h:
            img = f.read()
            h.write(img)

    n += 1
    print(imgUrl)
    print()

driver.close()