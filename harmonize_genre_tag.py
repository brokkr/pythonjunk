# -*- coding: utf-8 -*-

import os
import sys

import readchar

from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.id3._util import ID3NoHeaderError

class MusicTree:
    def __init__(self, rootdir):
        self.rootdir = rootdir
        self.genre_lst = {}
        self.artist_list = os.listdir(self.rootdir)
        for artist in self.artist_list:
            self.artist(artist)

    def artist(self, artist):
        artist_path = os.path.join(self.rootdir, artist)
        if os.path.isfile(artist_path):
            return
        print artist
        album_list = []
        for album in os.listdir(artist_path):
            album_path = os.path.join(artist_path, album)
            if os.path.isfile(album_path):
                continue
            album_list.append(album)
            print '   ' + album
        # if there is only one album, no need for distinction
        print "\nPress Enter to input a common genre for the artist"
        if len(album_list) > 1:
            print "Press 'l' to input a genre for each album"
        print "Press Spacebar to skip directory"
        print "Press 'q' to quit loop"
        choice = readchar.readchar()
        print
        # genredic = { k: self.genre_lst.count(k) for k in set(self.genre_lst) }
        # topten = sorted(genredic, key=genredic.get, reverse=True)[:10]
        # print list of top ten genres, keywords 0-9
        # readchar for kwyword or enter to enter manually
        if choice == '\r':
            genre = raw_input("Enter artist genre: ")
        elif choice == 'l':
            for album in album_list:
                print '   ' + album
                genre = raw_input("   Enter album genre: ")
        elif choice == ' ':
            pass
        elif choice == 'q':
            sys.exit()
        print

    def harmonize_dir(self, path, genre):
        '''for the path provided, write genre in all music files under that path'''
        # use os.walk to get list of file_paths
        # run appropriate tag writing function on file_paths
        # append genre_list
        pass

    def write_genre(self, file_path, genre):
        '''write genre to a single file'''
        # identify file type
        # set module
        # create metadata object
        # write genre
        # close
        pass

MusicTree(os.getcwd())

