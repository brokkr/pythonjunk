#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# harmonize_genre_tag.py (CC0)
# http://creativecommons.org/publicdomain/zero/1.0/
# To the extent possible under law, the author, Mads Michelsen, 
# has waived all copyright and related or neighboring rights to 
# this software.
#
# Very rudimentary tool to get an overview of genre frequency in 
# music collection

import os
import sys
import time

from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.id3._util import ID3NoHeaderError

class MusicTree:
    def __init__(self, rootdir):
        self.rootdir = rootdir
        self.genre_lst = []
        self.file_dic = {}

        for (dirname, subdirlist, filelist) in os.walk(self.rootdir):
            for filename in filelist:
                file_path = os.path.join(dirname, filename)
                file_ext = os.path.splitext(file_path)[1]
                if file_ext == '.flac' or file_ext == '.mp3':
                    genre = self.return_genre(file_ext, file_path)
                    self.genre_lst.append(genre)
                    if self.file_dic.has_key(genre):
                        self.file_dic[genre].append(file_path)
                    else:
                        self.file_dic[genre] = []
                        self.file_dic[genre].append(file_path)

        self.genre_dic = { k: self.genre_lst.count(k) for k in set(self.genre_lst) }
        self.ranked = sorted(self.genre_dic, key=self.genre_dic.get, reverse=True)
        #for genre in self.ranked[:20]:
        #    print genre, self.genre_dic[genre]

    def return_genre(self, file_ext, file_path):
        if file_ext == '.flac':
            tag = FLAC(file_path)
        elif file_ext == '.mp3':
            tag = EasyID3(file_path)
        try:
            genre = tag['genre'][0]
        except KeyError:
            genre = ''
        return genre



