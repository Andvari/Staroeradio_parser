'''
Created on Jun 16, 2014

@author: nemo
'''

import urllib2, re

i = 0x90
while i<=0xAF:
    print "\xD0" + chr(i)
    req = urllib2.urlopen("http://staroeradio.ru/collection/\xD0" + chr(i))
    page = req.read()

    f = open("\xD0" + chr(i) + ".txt", "wb")

    track_list = re.compile('<a href="/audio/(.*?)</div></a>').findall(page)

    for track in track_list:
        id = track[ 0 : track.find('"')]
        name = track [track.find('mp3name">') + 9 : ]
        f.write('"' + id + '"' + ' "' + name + '"\n')
        
    f.close()
    i += 1