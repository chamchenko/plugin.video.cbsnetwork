# Copyright: (c) 2016, Chamchenko
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)
# This file is part of plugin.video.cbsnetwork
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
import re
import xbmcplugin
import sys
import urlquick

from .vars import *
from .create_item import addLink
from .tools import log

LIVE_TV_URL = "https://cbsdigital.cbs.com/apps-api/v3.0/iphone/live/channels.json"
LIVE_TV_AT = "ABA2MDk2NTU5NDI5OTI0Mzk5S0s6LYuEpkX9lsvDyh+EYGz3/Z/GwKUR4l1SzpGFrsniQqc6pocDBZLCUhnDbsji"
PARAMS_LIVE_TV = {
                    "at": LIVE_TV_AT,
                    "locale": "en-US",
                    "_clientRegion": "US",
                    "showListing": "true"
                }
headers = {"User-Agent": USER_AGENT}

def browseLiveTV():
    # CBS
    live_tv_url = "https://v-ny.mybtv.net/live/545/1280x720.m3u8"
    response = requests.get(live_tv_url)
    if response.status_code == 200:
        live_url = response.url
        title = "CBS"
        addLink(title, live_url, 8)


    # CBS
    live_tv_url = "https://cbsn-2.cbsnstream.cbsnews.com/out/v1/a6a897e8f4f74cfc896223dfd822482f/master.m3u8"
    response = requests.get(live_tv_url)
    if response.status_code == 200:
        live_url = response.url
        title = "CBS Switcher 1"
        addLink(title, live_url, 8)

    # CBS
    live_tv_url = "https://cbsn-3-fastly.cbsnstream.cbsnews.com/out/v1/f081461c65494eeaa9ec596d0fe96a14/master.m3u8"
    response = requests.get(live_tv_url)
    if response.status_code == 200:
        live_url = response.url
        title = "CBS Switcher 2"
        addLink(title, live_url, 8)



 # CBS News
    live_tv_url = "https://dai.google.com/linear/hls/pa/event/Sid4xiTQTkCT1SLu6rjUSQ/stream/82d2999b-0c66-4c7d-83e8-1201d7d31bbe:CBF2/variant/ea524505d39e73f6a2da30bf0adce261/bandwidth/3073312.m3u8"
    response = requests.get(live_tv_url)
    if response.status_code == 200:
        live_url = response.url
        title = "CBS News"
        addLink(title, live_url, 8)

    # CBS News 2
    live_tv_url = "https://dai.google.com/ssai/event/Sid4xiTQTkCT1SLu6rjUSQ/master.m3u8"
    response = requests.get(live_tv_url)
    if response.status_code == 200:
        live_url = response.url
        title = "CBS News 2"
        addLink(title, live_url, 8)

    # CBS News Miami
    live_tv_url = "https://dai.google.com/linear/hls/event/_yODrBHESGSzPe3dqW4gGg/master.m3u8"
    response = requests.get(live_tv_url)
    if response.status_code == 200:
        live_url = response.url
        title = "CBS News Miami"
        addLink(title, live_url, 8)

    # CBS News Los Angeles
    live_tv_url = "https://dai.google.com/linear/hls/event/K_2aA7OVRTacJJli1oSi8w/master.m3u8"
    response = requests.get(live_tv_url)
    if response.status_code == 200:
        live_url = response.url
        title = "CBS News Los Angeles"
        addLink(title, live_url, 8)

    # ET AMERICANO
    live_tv_url = "https://dai.google.com/linear/hls/event/xrVrJYTmTfitfXBQfeZByQ/master.m3u8"
    response = requests.get(live_tv_url)
    if response.status_code == 200:
        live_url = response.url
        title = "ET AMERICANO"
        addLink(title, live_url, 8)




import requests
