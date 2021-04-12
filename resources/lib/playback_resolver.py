# Copyright: (c) 2016, Chamchenko
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)
# This file is part of plugin.video.cbs
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import xbmcgui
import xbmcplugin
import json
import sys
import re
import urlquick
import inputstreamhelper

from .tools import log
from .vars import *

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


PID_URL = 'http://can.cbs.com/thunder/player/videoPlayerService.php'
SMIL_URL = 'https://link.theplatform.com/s/dJ5BDC/%s?mbr=true&manifest=m3u'


def playVideo(streaminfo):
    log('playVideo')
    headers = {"User-Agent": PC_UA}
    json_parser = json.loads(streaminfo)
    streamID = json_parser['streamID']
    pid = json_parser['pid']
    ep_url = json_parser['ep_url']
    pattern = 'widevine\".*\{"url"\:\"(.*?)".*Authorization\"\:\"(.*?)\"'
    resp_ep = urlquick.get(ep_url, headers=headers, max_age=-1).text
    license_url = re.findall(pattern,resp_ep)[0][0].replace('\\','').replace('https','http')
    authorization = re.findall(pattern,resp_ep)[0][1].strip()
    resp = urlquick.get(SMIL_URL % pid, max_age=-1)    
    playbackURL = resp.history[0].headers['location']
    return json.dumps({
                        'playbackURL': playbackURL,
                        'license_url': license_url,
                        'authorization': authorization
                    })
