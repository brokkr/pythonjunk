#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# harmonize_genre_tag.py (CC0)
# http://creativecommons.org/publicdomain/zero/1.0/
# To the extent possible under law, the author, Mads Michelsen, 
# has waived all copyright and related or neighboring rights to 
# this software.
#
# This script runs on a music collection and writes genre tags to music files
# therein on an artist/album basis. Common genre values are gathered and 
# available for easy use.

import os
import sys
import time

import readchar

from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.id3._util import ID3NoHeaderError

class MusicTree:
    def __init__(self, rootdir):
        '''run user input loop on main root dir'''
        self.rootdir = rootdir
        self.genre_lst = []
        self.artist_list = os.listdir(self.rootdir)
        for artist in self.artist_list:
            self.artist(artist)

    def artist(self, artist):
        '''get user input for each top-level directory'''
        artist_path = os.path.join(self.rootdir, artist)
        if os.path.isfile(artist_path):
            return
        os.system('clear')
        print artist
        album_list = []
        for album in os.listdir(artist_path):
            if os.path.isfile(os.path.join(artist_path, album)):
                continue
            album_list.append(album)
            print '  ' + album
        print
        genredic = { k: self.genre_lst.count(k) for k in set(self.genre_lst) }
        topten = sorted(genredic, key=genredic.get, reverse=True)[:10]
        for entry in enumerate(topten):
            print entry[0], '    ', entry[1]
        print "\nEnter  Input a common genre for the artist"
        print "L      Input a genre for each album"
        print "Space  Skip directory"
        print "Q      Quit loop"
        genre = False
        choice = readchar.readchar()
        if choice == ' ':
            return
        elif choice == 'q':
            sys.exit()
        elif choice.isdigit():
            try:
                genre = topten[int(choice)]
                self.genre_lst.append(genre)
                self.harmonize_dir(artist_path, genre)
            except IndexError:
                pass
        print
        if choice == '\r':
            genre = raw_input("Enter artist genre: ")
            self.genre_lst.append(genre)
            self.harmonize_dir(artist_path, genre)
        elif choice == 'l':
            for album in album_list:
                print '   ' + album
                genre = raw_input("   Enter album genre: ")
                self.genre_lst.append(genre)
                self.harmonize_dir(os.path.join(artist_path, album), genre)

    def harmonize_dir(self, path, genre):
        '''for the path write genre in all music files under that path'''
        for (dirname, subdirlist, filelist) in os.walk(path):
            for filename in filelist:
                file_path = os.path.join(dirname, filename)
                file_ext = os.path.splitext(file_path)[1]
                if file_ext == '.flac' or file_ext == '.mp3':
                    self.write_genre(file_path, file_ext, genre)

    def write_genre(self, file_path, file_ext, genre):
        '''write genre to a single file'''
        if file_ext == '.flac':
            tag = FLAC(file_path)
        elif file_ext == '.mp3':
            tag = EasyID3(file_path)
        tag['genre'] = genre
        tag.save()

if __name__ == "__main__":
    MusicTree(os.getcwd())

