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
    live_tv_url = "https://www.cbs.com/live-tv/stream/cbs-news/"
    response = requests.get(live_tv_url)
    if response.status_code != 200:
        print("Error fetching url: " + live_tv_url)
        return
    live_url = response.url
    title = "CBS News"
    addLink(title, live_url, 8)
    
    
   
        
        
import requests


        
