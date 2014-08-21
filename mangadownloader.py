#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib
import os
import argparse


def get_page(url=''):
    page = requests.get(url)
    soup = BeautifulSoup(page.text)

    if not soup.title:
        return (False, 0)

    return (True, soup.find_all('img')[0].get('src'))


def get_chapter(manga='', chapter=0, dest=''):
    url = 'http://www.mangapanda.com/%s/%s/' % (manga, str(chapter))
    page_no = 1

    if not get_page(url):
        return (False, 'no chapter')

    while True:
        page = get_page(url + str(page_no))
        if not page[0]:
            return (False, 'no page')
        print page[1]
        urllib.urlretrieve(page[1], '%s/%s/%s_%s.jpg' % (dest, manga,
                           str(chapter), str(page_no)))
        page_no = page_no + 1


def get_manga(manga='', **kwargs):
    chapterFrom = kwargs.get('chapterFrom', 1)
    chapterTo = kwargs.get('chapterTo', chapterFrom)
    dest = kwargs.get('dest', '')

    directory = '%s/%s' % (dest, manga)

    if not os.path.exists(directory):
        os.makedirs(directory)

    while True:
        get_chapter(manga, chapterFrom, dest)
        chapterFrom = chapterFrom + 1

        if chapterFrom > chapterTo:
            print 'Done'
            return


if __name__ == '__main__':
    parser = \
        argparse.ArgumentParser(description='Download from mangapanda.com'
                                )
    parser.add_argument('manga', metavar='manga', help='The manga name')
    parser.add_argument('chapterFrom', metavar='from', type=int,
                        help='Download from chapter')
    parser.add_argument('chapterTo', metavar='to', type=int, nargs='?',
                        help='Download to chapter. Leave this blank to \
                                download one chapter')
    parser.add_argument('--dest', dest='dest', default='~/manga/',
                        help='Download to directory (default: ~/manga/)'
                        )

    args = parser.parse_args()

    get_manga(args.manga, dest=os.path.expanduser(args.dest),
              chapterFrom=args.chapterFrom, chapterTo=args.chapterTo)
