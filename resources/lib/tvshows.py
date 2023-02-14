# Copyright: (c) 2016, Chamchenko
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)
# This file is part of plugin.video.cbsnetwork
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
import xbmcplugin
import sys
import urlquick

from .vars import *
from .tools import log
from .create_item import addDir
from .create_item import addLink


def browseCategories():
    log(" Fetching url: " + CATEGORIES_URL)
    log(" Fetching params: %s" % CATEGORY_PARAMS)
    categories = json.loads(urlquick.get(
                                    CATEGORIES_URL,
                                    params=CATEGORY_PARAMS,
                                    headers=headers).text)
    for category in categories['showGroups']:
        category_id = category['id']
        category_name = category['title']
        addDir(category_name, str(category_id), 3)

def getTvShows(category_id):
    log('getTvShows')
    xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
    log(" Fetching url: " + SHOWS_URL % category_id)
    log(" Fetching params: %s" % MULT_SHOWS_PARAMS)
    apijson = json.loads(
                urlquick.get(SHOWS_URL % category_id,
                    headers=headers,
                    params=MULT_SHOWS_PARAMS).text)
    for item in apijson['group']['showGroupItems']:
        title = item['title']
        showId = item['showId']
        log("Fetching url: " + SEASON_LIST % showId)
        log(" Fetching params: %s" % MULT_SHOWS_PARAMS)
        sjson = json.loads(
                    urlquick.get(SEASON_LIST % showId,
                        headers=headers,
                        params=MULT_SHOWS_PARAMS).text)
        seasons = []
        for season in sjson['video_available_season']['itemList']:
            if season['totalCount'] == season['premiumCount']:
                continue
            else:
                seasons.append(season['seasonNum'])
        if seasons == []:
            continue
        show_slug = item['showPath'].split('/')[1]
        thumb = IMAGES_BASE_URL % item['showAssets']['filepath_show_browse_poster']
        fanart = IMAGES_BASE_URL % item['showAssets']['filepath_video_endcard_show_image']
        infoList = {
                    "mediatype": "episode",
                    "title": title,
                    "TVShowTitle": title}
        infoArt = {
                    "thumb": thumb,
                    "poster": thumb,
                    "fanart": fanart,
                    "icon": ICON,
                    "logo": ICON}
        infos = json.dumps({
                            'showId': showId,
                            'show_slug': show_slug,
                            'thumb': thumb,
                            'seasons': seasons
                        })
        addDir(title, infos, 4, infoArt, infoList,0,showId)

def getSeasons(infos):
    log('getSeasons')
    xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
    infos = json.loads(infos)
    thumb = infos['thumb']
    showId = infos['showId']
    show_slug = infos['show_slug']
    seasons = infos['seasons']
    for season_number in seasons:
        seasonURL   = SEASON_API%(show_slug, season_number)
        infos = json.dumps({"seasonURL": seasonURL,
                            "episodes_count": 30,
                            "season_number":season_number})
        title = 'Season %s' % season_number
        infoList = {
                    "mediatype": "tvshow",
                    "title": title,
                    "TVShowTitle": title}
        infoArt = {
                    "thumb": thumb,
                    "poster": thumb,
                    "fanart": FANART,
                    "icon": ICON,
                    "logo": ICON}
        addDir(title, infos, 5, infoArt, infoList)



def getEpisodes(infos):
    log('getEpisodes')
    xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
    infos = json.loads(infos)
    url = infos['seasonURL']
    season_number = infos['season_number']
    headers = {
                'User-Agent': USER_AGENT,
                'authority' :'www.cbs.com',
                'referer' :'https://www.cbs.com/shows/',
                'x-requested-with' :'XMLHttpRequest'
            }
    log(" Fetching url: " + url)
    items = json.loads(urlquick.get(url,
                    headers=headers).text)

    for item in items['result']['data']:
        status = item['status']
        if status != 'AVAILABLE':
            continue
        streamID = item['content_id']
        pid = item['metaData']['pid']
        ep_url = BASE_URL + item['url']
        streaminfo = json.dumps({'streamID': streamID, 'pid': pid, 'ep_url': ep_url})
        title = item['title']
        vidType = item['type']
        thumb = item['thumb']['small']
        aired = str(item['airdate_iso']).split('T')[0]
        showTitle = item['series_title']
        duration = item['duration_raw']
        episodeNumber = item['episode_number'].split(',')[0]
        plot = '%s:\n%s' % (title, item['description'])
        seinfo = ('S' + ('0' if int(season_number) < 10 else '') + \
                            str(season_number) + 'E' + \
                            ('0' if int(episodeNumber) < 10 else '') + \
                            str(episodeNumber))
        infoLabels = {
                        "mediatype":"episode",
                        "title":showTitle+' '+seinfo,
                        "plot":plot,
                        "aired":aired,
                        "duration":duration,
                        "TVShowTitle":title
                    }
        infoArt = {
                    "thumb":thumb,
                    "poster":thumb,
                    "fanart":thumb,
                    "icon":ICON,
                    "logo":ICON
                }
        addLink(title, streaminfo, 9, infoLabels, infoArt, len(items))
