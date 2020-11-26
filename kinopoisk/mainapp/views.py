import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

tvgle1 = 'https://www.tvigle.ru//catalog/filmy/?page='
tvigle2 = ' &q=&show=block'
tvgle_list = []
pages = 100


def get_hn():
    for i in range(1, pages):
        rec = requests.get(tvgle1 + str(i) + tvigle2).text
        soup = BeautifulSoup(rec, 'lxml')
        posters = soup.find_all('a', class_='product-list__item kind__film')
        for poster in posters:
            photo = poster.find('img').get('src')
            title = poster.find('div', class_='product-list__item_name').text
            url = poster.get('href')
            year = poster.find('div', 'product-list__item_info').text
            category = poster.find('div', class_='meta-labels').find_next('span').text
            year = year.strip()
            url = 'https://www.tvigle.ru' + url
            data = {'photo': photo,
                    'title': title,
                    'year': year,
                    'category': category,
                    'url': url
                    }
            tvgle_list.append(data)


get_hn()


def home(requests):
    context = {'tvgle_list': tvgle_list}
    return render(requests, 'mainapp/index.html', context)
