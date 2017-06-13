# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request
import json
import re


class GetDic:
    def __init__(self):
        pass

    def request(self, url, keyword):

        resp = urllib.request.urlopen(url+"keyword="+urllib.request.quote(keyword)+"&lang=cht")  # open web
        encoding = resp.info().get_content_charset('utf-8')
        output = json.loads(resp.read().decode(encoding))
        return output


if __name__ == '__main__':
    playerlist = []

    ReadFromTxt = open('Dic/Soccerplayer.txt', 'r')
    for line in ReadFromTxt:
        if line not in playerlist:
            playerlist.append(line.rstrip())
    ReadFromTxt.close()
    print(playerlist)
    # WriteToTxt = open('Dic/baseballplayer.txt', 'a')
    # WriteToTxt = open('Dic/baseballterm2.txt', 'w')
    WriteToTxt = open('Dic/soccerplayer2.txt', 'w')
    # WriteToTxt = open('Dic/soccerterm3.txt', 'w')

    for player in playerlist:
        url = 'http://api.udic.cs.nchu.edu.tw/api/kcm/?'

        json_set = GetDic().request(url, player)
        for i in json_set:
            WriteToTxt.writelines(i[0]+'\n')
            print(i[0])

    WriteToTxt.close()