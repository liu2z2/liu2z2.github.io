#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime

AUTHOR = 'Liu'
SITENAME = "Liu's ePortfolio"
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
EXTRA_PATH_METADATA = {'images/GitHub-logo.ico': {'path':'favicon.ico'},
                       'extra/robots.txt': {'path':'robots.txt'}}

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
PLUGINS = ['assets', # https://github.com/getpelican/pelican-plugins/tree/master/assets
           'tipue_search',  # https://github.com/getpelican/pelican-plugins/tree/master/tipue_search
           'post_stats', # https://github.com/getpelican/pelican-plugins/tree/master/post_stats
           'neighbors', # https://github.com/getpelican/pelican-plugins/tree/master/neighbors
           'extract_toc', # https://github.com/getpelican/pelican-plugins/tree/master/extract_toc
           'render_math', # https://github.com/getpelican/pelican-plugins/tree/master/render_math
           'sitemap', # https://github.com/getpelican/pelican-plugins/tree/master/sitemap
           ]
UTTERANCES_REPO = "liu2z2/liu2z2.github.io"
UTTERANCES_LABEL = "Comments"
UTTERANCES_FILTER = False
UTTERANCES_THEME = "github-light"
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'pages': 0.4
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}
# CLAIM_GOOGLE = u'iXlxw5kesqJmrOLBmyqGUYw3nZkBW2GBcnfuIni_910'
STAT_COUNTER_PROJECT = 12472197
STAT_COUNTER_SECURITY = u'98c4a201'


############################################
# Landing page configuration
############################################
LANDING_PAGE_TITLE = "Hello! Welcome to Liu's ePortfolio!"
PROJECTS_TITLE = "Read more about ..."
PROJECTS = [
    {
        'name': 'My Projects',
        'url': REAL_SITEURL+'/tags#project-ref',
        'description': 'in electronics and programming'
    },
    {
        'name': 'GitHub page',
        'url': 'https://github.com/liu2z2',
        'description': 'including my programming projects, documented and undocumented'
    },
    {
        'name': 'Honors ePortfolio (deprecated)',
        'url': 'https://liu2z2.wixsite.com/liuportfolio',
        'description': 'a portfolio I used for the University Honors Project'
    },
]
RECENT_ARTICLES_COUNT = 3

############################################
# Footer configuration
############################################
SITE_LICENSE = """Content licensed under <a rel="license nofollow noopener noreferrer"
    href="https://www.gnu.org/licenses/agpl-3.0.en.html" target="_blank">
    GNU Affero General Public License</a>."""
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
PAGE_URL = "pages/{slug}"
PAGE_SAVE_AS = "{slug}.html"
ARTICLE_URL = 'articles/{date:%Y}{date:%m}{date:%d}-{slug}'
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
