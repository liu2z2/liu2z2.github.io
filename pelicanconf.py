#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime

AUTHOR = 'Liu'
SITENAME = "Liu's Portfolio"
SITEURL = "http://localhost:8000"
REAL_SITEURL = "https://liu2z2.github.io"

############################################
# Path settings
############################################

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 
                'ViewerJS',
                'extra',
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
PLUGINS = ['assets','tipue_search']

############################################
# Landing page configuration
############################################
LANDING_PAGE_TITLE = "Hello! Welcome to Liu's Portfolio!"
PROJECTS_TITLE = "Read more about ..."
PROJECTS = [
    {
        'name': 'My Projects',
        'url': REAL_SITEURL+'/tags#projects-ref',
        'description': 'electronics and programming projects'
    },
    {
        'name': 'GitHub page',
        'url': 'https://github.com/liu2z2',
        'description': 'includes my programming projects, documented and undocumented'
    },
    {
        'name': 'Honors ePortfolio (deprecated)',
        'url': 'https://liu2z2.wixsite.com/liuportfolio',
        'description': 'a portfolio I used for the University Honors Project'
    },
]

############################################
# Footer configuration
############################################
SITE_LICENSE = """Content licensed under <a rel="license nofollow noopener noreferrer"
    href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
    Creative Commons Attribution 4.0 International License</a>."""
HOSTED_ON = {
    "name": "GitHub",
    "url": "https://github.com/liu2z2/liu2z2.github.io"
    }

############################################
# Content page configuration
############################################
SOCIAL = (
    ('Email', 'liu2z2@mail.uc.edu'),
    ("linkedin", "https://www.linkedin.com/in/liu-uc/"),
    ("github", "https://github.com/liu2z2"),
    )
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
ARTICLE_URL = 'articles/{date:%Y}{date:%m}{date:%d}-{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}{date:%m}{date:%d}-{slug}/index.html'
DEFAULT_PAGINATION = 10
DEFAULT_METADATA = {
    'status': 'draft',
    'author': 'Liu',
}

############################################
# Markdown configuration
############################################
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.meta': {},
        'smarty' : {
            'smart_angled_quotes' : 'true'
        },
        'markdown.extensions.toc': {
            'permalink': 'true',
        },
    }
}
