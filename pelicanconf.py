#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Liu'
SITENAME = 'Liu (Zuguang Liu)'
SITEURL = ''
SITELOGO = 'https://github.com/liu2z2/liu2z2.github.io/blob/pelican-src/content/images/wiggler-hello.png'


# Path settings
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']



TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Link to old Portfolio', 'https://liu2z2.wixsite.com/liuportfolio'),
        #  ('You can modify those links in your config file', 'https://get.stick.bugged/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Used Theme
THEME = "pelican-themes/Flex"
