#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib
import os


def get_page(url=''):
    page = requests.get(url)
    soup = BeautifulSoup(page.text)

    if not soup.title:
        return (False, 0)

    return (True, soup.find_all('img')[0].get('src'))


def get_chapter(comic='', chapter=0):
    url = 'http://www.mangapanda.com/%s/%s/' % (comic, str(chapter))
    page_no = 1

    if not get_page(url):
        return (False, 'no chapter')

    while True:
        page = get_page(url + str(page_no))
        if not page[0]:
            return (False, 'no page')
        print page[1]
        urllib.urlretrieve(page[1], 'manga/%s/%s_%s.jpg' % (comic, str(chapter), str(page_no)))
        page_no = page_no + 1


def get_comic(comic='', **kwargs):
    chapterFrom = kwargs.get('chapterFrom', 1)
    chapterTo = kwargs.get('chapterTo', 1)

    directory = "manga/%s" % comic

    if not os.path.exists(directory):
        os.makedirs(directory)

    while True:
        if chapterFrom == chapterTo:
            print "Done"

        get_chapter(comic, chapterFrom)
        chapterFrom = chapterFrom + 1



