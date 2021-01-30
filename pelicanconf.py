#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime

AUTHOR = 'Liu'
SITENAME = "Liu's Portfolio"
SITEURL = "http://localhost:8000"

############################################
# Path settings
############################################

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 
                'ViewerJS',
              'extra/robots.txt',
              ]
EXTRA_PATH_METADATA = {'images/GitHub-logo.ico':{'path':'favicon.ico'}}

############################################
# Basic settings
############################################
TIMEZONE = 'US/Eastern'
DEFAULT_LANG = 'en-US'
THEME = "pelican-themes/elegant"
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
#RELATIVE_URLS = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

############################################
# Plugin settings
############################################
PLUGIN_PATHS = ['plugins']
PLUGINS = []

############################################
# Landing page configuration
############################################
LANDING_PAGE_TITLE = "Hello! Welcome to Liu's Portfolio!"
# PROJECTS = [
#     {
#         'name': 'Creating and Maintaining This Website',
#         'url': 'https://jackdewinter.github.io/categories#website-ref',
#         'description': 'Notes and articles about the creation and maintenance of this website.'
#     },
# ]

############################################
# Content page configuration
############################################
SOCIAL = (
    ('Email', 'liu2z2@mail.uc.edu'),
    ("linkedin", "https://www.linkedin.com/in/liu-uc/"),
    ("github", "https://github.com/liu2z2"),
    )
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
DEFAULT_PAGINATION = 10
PYGMENTS_STYLE = "monokai"
