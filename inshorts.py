# Coded by Sumanjay on 29th Feb 2020

import uuid
import requests
from bs4 import BeautifulSoup


def extract_content_from_item_prop(soup, item_prop):
    if item_prop == 'author':
        element = soup.find('span', class_=item_prop)
        text = element.get_text(strip=True)
    elif item_prop == 'date':
        element = soup.find(attrs={'clas': item_prop}) #Probably a typo from Inshorts Team
        text = element.get_text(strip=True)
    elif item_prop == 'image':
        span_element = soup.find('span', itemprop=item_prop)
        meta_element = span_element.find('meta', itemprop='url')
        return meta_element['content']
    elif item_prop == 'mainEntityOfPage':
        span_element = soup.find('span', itemprop=item_prop)
        return span_element.get('itemid')
    else:
        element = soup.find(attrs={'itemprop': item_prop})
        text = element.get_text(strip=True)
    return text


def getNews(category):
    newsDictionary = {
        'success': True,
        'category': category,
        'data': []
    }

    try:
        if category != 'all':
            htmlBody = requests.get(
                'https://www.inshorts.com/en/read/' + category)
        else:
            htmlBody = requests.get('https://www.inshorts.com/en/read/')

    except requests.exceptions.RequestException as e:
        newsDictionary['success'] = False
        newsDictionary['error'] = str(e.message)
        return newsDictionary

    soup = BeautifulSoup(htmlBody.text, 'lxml')
    newsCards = soup.find_all(
        attrs={'itemtype': 'http://schema.org/NewsArticle'})

    if not newsCards:
        newsDictionary['success'] = False
        newsDictionary['error'] = 'Invalid Category'
        return newsDictionary

    for card in newsCards:

        try:
            title = extract_content_from_item_prop(card, 'headline')
        except Exception:
            title = None
        try:
            imageUrl = extract_content_from_item_prop(card, 'image')
        except Exception:
            imageUrl = None

        try:
            url = extract_content_from_item_prop(card, 'mainEntityOfPage')
        except Exception:
            url = None

        try:
            content = extract_content_from_item_prop(card, 'articleBody')
        except Exception:
            content = None

        try:
            author = extract_content_from_item_prop(card, 'author')
        except Exception:
            author = None

        try:
            date = extract_content_from_item_prop(card, 'date')
        except Exception:
            date = None

        try:
            time = extract_content_from_item_prop(card, 'datePublished')
        except Exception:
            time = None

        try:
            readMoreUrl = card.find_all('div')[-1].find('a')['href']
        except Exception:
            readMoreUrl = url

        newsObject = {
            'id': uuid.uuid4().hex,
            'title': title,
            'imageUrl': imageUrl,
            'url': url,
            'content': content,
            'author': author,
            'date': date,
            'time': time,
            'readMoreUrl': readMoreUrl
        }
        newsDictionary['data'].append(newsObject)
    return newsDictionary
