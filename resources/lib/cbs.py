# Copyright: (c) 2016, Chamchenko
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)
# This file is part of plugin.video.cbsnetwork
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import json
import xbmcgui
import xbmcplugin
import inputstreamhelper

from .tools import *
from .livetv import browseLiveTV
from .tvshows import browseCategories
from .tvshows import getTvShows
from .tvshows import getSeasons
from .tvshows import getEpisodes
from .create_item import addDir
from .vars import *
from .playback_resolver import playVideo

class CBS(object):
    def __init__(self):
        log('__init__')
    def buildMenu(self):
        for item in MAIN_MENU: addDir(*item)
    def browseLive(self):
        browseLiveTV()
    def browseShowsMenu(self):
        browseCategories()
    def browseShows(self, category_id):
        getTvShows(category_id)
    def browseSeasons(self, infos):
        getSeasons(infos)
    def browseEpisodes(self, infos):
        getEpisodes(infos)
    def playLive(self, name, playbackURL):
        liz = xbmcgui.ListItem(name, path=playbackURL)
        liz.setProperty(INPUTSTREAM_PROP,'inputstream.adaptive')
        liz.setProperty('inputstream.adaptive.manifest_type', 'hls')
        liz.setProperty('inputstream.adaptive.stream_headers', 'User-Agent=%s' % PC_UA)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem=liz)
    def playVideo(self, name, streaminfo, liz=None):
        is_helper = inputstreamhelper.Helper('mpd', drm='com.widevine.alpha')
        if is_helper.check_inputstream():
            playbackinfo = json.loads(playVideo(streaminfo))
            playbackURL = playbackinfo['playbackURL']
            license_url = playbackinfo['license_url']
            authorization = playbackinfo['authorization']
            liz = xbmcgui.ListItem(name, path=playbackURL)
            URL_LICENCE_KEY = LICENCE_KEY_TEMP % (license_url, PC_UA, BASE_URL, authorization, 'cbsi.live.ott.irdeto.com')
            liz.setProperty(INPUTSTREAM_PROP,'inputstream.adaptive')
            liz.setProperty('inputstream.adaptive.manifest_type', 'mpd')
            liz.setProperty('inputstream.adaptive.license_type', 'com.widevine.alpha')
            liz.setProperty('inputstream.adaptive.license_key', URL_LICENCE_KEY)
            liz.setProperty('inputstream.adaptive.stream_headers', 'User-Agent=%s' % PC_UA)
            xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem=liz)
        else:
            return
        
params=getParams()
try: url=unquote_plus(params["url"])
except: url=None
try: name=unquote_plus(params["name"])
except: name=None
try: mode=int(params["mode"])
except: mode=None
log("Mode: "+str(mode))
log("URL : "+str(url))
log("Name: "+str(name))

if  mode==None: CBS().buildMenu()
elif mode == 1: CBS().browseLive()
elif mode == 2: CBS().browseShowsMenu()
elif mode == 3: CBS().browseShows(url)
elif mode == 4: CBS().browseSeasons(url)
elif mode == 5: CBS().browseEpisodes(url)
elif mode == 8: CBS().playLive(name, url)
elif mode == 9: CBS().playVideo(name, url)


xbmcplugin.addSortMethod(int(sys.argv[1]) , xbmcplugin.SORT_METHOD_LABEL)
xbmcplugin.addSortMethod(int(sys.argv[1]) , xbmcplugin.SORT_METHOD_TITLE)
xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
