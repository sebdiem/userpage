#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'S\xe9bastien Diemer'
SITENAME = u'sebdiem.github.io'
FORMATED_TITLE = u'seb<span>&#x24d3</span>iem'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

OUTPUT_PATH = 'Users/Diem/GitHub/sebdiem.github.io/'
# To keep version control data
OUTPUT_RETENTION = ('.git')

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
#FACEBOOK_LIKE = True
TWITTER_USER = 'DiemerSebastien'
TWITTER_TWEET_BUTTON = True

DEFAULT_PAGINATION = 5
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
SEARCH_BOX = True

THEME = '../my-theme'
PLUGINS = ['liquid_tags.include_code',
           'liquid_tags.notebook']
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

#SITEURL = '/Users/Diem/Github/userpage_source/output'
SITEURL = 'http://sebdiem.github.io'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MENUITEMS = [('Blog', '%s/' % SITEURL),
             ('Archives', '%s/archives.html' % SITEURL),
             ('À Propos', '%s/pages/a-propos.html' % SITEURL)]

# The static paths accessible on the output path static/
STATIC_PATHS = ['images']
