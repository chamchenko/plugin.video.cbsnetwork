# Copyright: (c) 2016, Chamchenko
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)
# This file is part of plugin.video.cbsnetwork
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import xbmcaddon
from xbmc import getInfoLabel
ADDON_ID = 'plugin.video.cbsnetwork'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME = REAL_SETTINGS.getAddonInfo('name')
SETTINGS_LOC = REAL_SETTINGS.getAddonInfo('profile')
QUALITY = REAL_SETTINGS.getSetting('Quality').replace('p','')
ADDON_PATH = REAL_SETTINGS.getAddonInfo('path')
ADDON_VERSION = REAL_SETTINGS.getAddonInfo('version')
ICON = REAL_SETTINGS.getAddonInfo('icon')
FANART = REAL_SETTINGS.getAddonInfo('fanart')
LANGUAGE = REAL_SETTINGS.getLocalizedString
DEBUG = REAL_SETTINGS.getSetting('Debugging') == 'true'
XBMC_VERSION = int(getInfoLabel("System.BuildVersion").split('-')[0].split('.')[0])
INPUTSTREAM_PROP = 'inputstream' if XBMC_VERSION >= 19 else 'inputstreamaddon'

PC_UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
LICENCE_KEY_TEMP = '%s|User-Agent=%s&Referer=%s&Authorization=%s&authority=%s&Content-Type=%s|R{SSM}|'
USER_AGENT = "CBSTVE/3519 CFNetwork/1220.1 Darwin/20.3.0"
headers = {"User-Agent": USER_AGENT}
BASE_URL = 'https://www.cbs.com'
SHOWS_API = BASE_URL + '/shows_xhr/%s'
SEASON_API = BASE_URL + '/shows/%s/xhr/episodes/page/0/size/30/xs/0/season/%s/'
IMAGES_BASE_URL = "http://wwwimage.cbsstatic.com/base/%s"
API_BASE_URL = "https://cbsdigital.cbs.com/apps-api/"
SINGLE_EPISODE_INFO_URL = API_BASE_URL + 'v3.1/iphone/dynamicplay/show/%s.json'
SINGLE_SHOW_AT = "ABA1NDAwNzc5OTE2NDAzMzYyFmztWf+1XMRsrbF7WpFhWti+4emxV0SENusnMwEEkoPgW2beW0jFPmKXgQBfTDT9"
SINGLE_SHOW_PARAMS = {"at": SINGLE_SHOW_AT, "locale": "en-US"}
SHOWS_BASE_URL = API_BASE_URL + "v2.0/iphone/shows/"
CATEGORIES_URL = SHOWS_BASE_URL + "groups.json"
SHOWS_URL = SHOWS_BASE_URL + "group/%s.json"
SINGLE_SHOW_INFO_URL = API_BASE_URL + "%s.json"
SINGLE_SHOW_LANDING_URL = SHOWS_BASE_URL + "%s/videos/config/SHOW_LANDING_EPISODES.json"
SEASON_LIST = SHOWS_BASE_URL + "%s/video/season/availability.json"
SINGLE_SEASON_EP_LIST = API_BASE_URL + "v2.0/iphone/videos/section/%s.json"
CATEGORY_AT = "ABA2MDk2NTU5NDI5OTI0Mzk5S0s6LYuEpkX9lsvDyh+EYGz3/Z/GwKUR4l1SzpGFrsniQqc6pocDBZLCUhnDbsji"
MULT_SHOWS_AT = "ABA4OTU3NjAwNTc4Njg3NjE2qlOcFciGGVo8EoUSR5C39f1+lEMBvlu499fO38sPLKIGL2xHNK+IzWxZncWGSflM"
SINGLE_SEASON_AT = "ABA3NTc3NjMyMjcyOTEwNjMz7A45BjQavk2ZsZoBZLjvcOtwP6AlA3Tc/46fB7w0i2T1SneX+/nCSCwBukA4M3Kp"
CATEGORY_PARAMS = {"at": CATEGORY_AT, "locale": "en-US"}
MULT_SHOWS_PARAMS = {"at": MULT_SHOWS_AT, "locale": "en-US"}

MAIN_MENU = [('LIVE TV', "", 1),
             ('TVSHOWS', "", 2)]
