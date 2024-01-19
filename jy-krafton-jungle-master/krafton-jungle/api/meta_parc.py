import requests
from bs4 import BeautifulSoup

url = 'https://shinsegaemall.ssg.com/best/bestShop.ssg?dispCtgId=6000039159'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

soup = BeautifulSoup(data.text, 'html.parser')

og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')

db.items.insert_one(data)

return jsonify({'result': 'success'})

print(og_image)
print(og_title)
print(og_description)

