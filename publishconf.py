#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR = 'Pmin'
SITENAME = 'Pmin'
SITEURL = '//28sui.github.io'
SITESUBTITLE = '人生苦短,我TMD又懒'
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
        'zh_CN': '%Y-%m-%d %H:%M:%S',
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = 'zh-CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll


# Social widget
SOCIAL = (('github', '#'),
          ('twitter', '#'),
          ('facebook', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "./theme/Pmin"

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'


STATIC_PATHS = [
    'images',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

MAIN_MENU = False
MENUITEMS = (('分 类', '/categories.html'),
    ('存  档', '/archives.html'),
            ('关  于', '/about.html'),)

DUOSHUO = '28sui'
PYGMENTS_STYLE = 'default'
