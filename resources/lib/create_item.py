# Copyright: (c) 2016, Chamchenko
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)
# This file is part of plugin.video.cbs
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import xbmcgui
import xbmcplugin

from .vars import *
from .tools import *


def addLink(name, u, mode, infoList=False, infoArt=False, total=0, favID=None, infoCast=None):
    name = name.encode('ascii', 'replace')
    log('addLink, name = %s' % name)
    liz=xbmcgui.ListItem(name)
    liz.setProperty('IsPlayable', 'true')
    if infoList == False:
        liz.setInfo(
                type = "Video",
                infoLabels = {
                    "mediatype": "video",
                    "label": name,
                    "title": name
                    }
                )
    else:
        liz.setInfo(type="Video", infoLabels=infoList)

    if infoArt == False:
        liz.setArt({'thumb':ICON,'fanart':FANART})
    else:
        liz.setArt(infoArt)

    if infoCast:
        liz.setCast(infoCast)
    u = sys.argv[0]+"?url="+quote_plus(u)+"&mode="+str(mode)+"&name="+quote_plus(name)
    xbmcplugin.addDirectoryItem(
        handle=int(sys.argv[1]), url=u, listitem=liz, totalItems=total)



def addDir(name, u, mode=None, infoArt=False, infoList=False, total=0, favID=None, infoCast=False):

    name = name.encode('ascii', 'replace')
    log('addDir, name = %s' % name)
    liz = xbmcgui.ListItem(name)
    liz.setProperty('IsPlayable', 'false')
    if infoList == False:
        liz.setInfo(
                type = "Video",
                infoLabels = {
                    "mediatype": "video",
                    "label": name,
                    "title": name
                    }
                )
    else:
        liz.setInfo(type = "Video",
                infoLabels = infoList)

    if infoArt == False:
        liz.setArt({'thumb':ICON, 'fanart':FANART})
    else:
        liz.setArt(infoArt)

    if infoCast != False:
        liz.setCast(infoCast)

    u = sys.argv[0]+"?url="+quote_plus(u)+"&mode="+str(mode)+"&name="+quote_plus(name)
    xbmcplugin.addDirectoryItem(
        handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True, totalItems=total)
