# -*- coding: utf-8 -*-

import os
import sys

import readchar
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.id3._util import ID3NoHeaderError

rootdir = os.getcwd()

for artist in os.listdir(rootdir):
    if os.path.isfile(artist):
        continue
    print artist
    album_list = []
    for album in os.listdir(os.path.join(rootdir, artist)):
        if os.path.isfile(album):
            continue
        album_list.append(album)
        print '   ' + album
    print "Press 'a' to input a common genre for the artist"
    print "Press 'l' to input a genre for each album"
    print "Press Enter to skip directory"
    print "Press Spacebar to quit loop"
    choice = readchar.readchar()
    print
    if choice == 'a':
        genre = raw_input("Enter artist genre: ")
    elif choice == 'l':
        for album in album_list:
            print '   ' + album
            genre = raw_input("   Enter album genre: ")
    elif choice == '\r':
        pass
    elif choice == ' ':
        sys.exit()
    print
