import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://books.toscrape.com/'

HEADERS = {
    "User-agent": "LearningScraperBot/1.0 (educational project; contact: her600742@gmail.com)"
}

response = requests.get(URL, headers=HEADERS, timeout=10)
response.encoding = 'utf-8'

# if response.status_code == 200:
#     print('OK')

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

all_books = []

for book in books:
    link_tag = book.find('h3').find('a')
    title = link_tag.get('title')

    price = book.find('p', class_='price_color').get_text(strip=True)

    in_stock = book.find('p', class_='instock availability').get_text(strip=True)

    star_rate = book.find('p', class_='star-rating').get('class')[1]

    all_books.append({
        'Название': title,
        'Рейтинг': star_rate,
        'Цена': price,
        'Наличие': in_stock,
    })

with open('books.csv', 'w', newline='', encoding='utf-8-sig') as f:
    fieldnames = all_books[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_books)

print(f'Собрано {len(all_books)} книг') 

    # print(title)
    # print(star_rate)
    # print(price)
    # print(in_stock)