# Copyright: (c) 2016, Chamchenko
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)
# This file is part of plugin.video.cbs
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
    log(" Fetching url: " + LIVE_TV_URL)
    items = json.loads(urlquick.get(LIVE_TV_URL, params=PARAMS_LIVE_TV, headers=headers).text)
    for channel in items['channels']:
        title = channel['channelName']
        live_url = channel['currentListing'][0]['contentCANVideo']['liveStreamingUrl']
        thumb = IMAGES_BASE_URL % channel['filePathLogo'] or ICON
        fanart = (IMAGES_BASE_URL % channel['currentListing'][0]['filePathThumb'] or
                 channel['currentListing'][0]['contentCANVideo']['thumbnail'] or
                 FANART)
        infoLabels = {"title":title}
        infoArt = {
                    "thumb": thumb,
                    "poster": thumb,
                    "fanart": fanart,
                    "icon": thumb,
                    "logo": thumb
                }
        addLink(title, live_url, 8, infoLabels, infoArt, len(items))
