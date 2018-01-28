#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Maxine Hartnett'
SITENAME = 'Just a Programmer Trying Her Best.'
SITESUBTITLE='Computer Science Student'
SITEDESCRIPTION='Junior in CS'
SITELOGO='logo.png'
SITEURL = 'ceilingcranes.github.io'

THEME = 'Flex'
PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('LinkedIn', 'https://www.linkedin.com/in/maxinehartnett/'),
         ('Github', 'https://github.com/ceilingcranes'),
         ('Study Blog', 'https://studyblrcs.tumblr.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Ceilingcranes'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
