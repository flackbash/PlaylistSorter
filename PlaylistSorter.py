import re
import operator
import os


def sortPlaylist(playlist):
    """Sorts playlist entries by artist

    Arguments:
    playlist - a string: name of the m3u playlist
    """
    # open playlist file
    source = open(playlist,  encoding="latin-1")
    lines = source.readlines()
    source.close()
    newList = []

    # get a list of 
    # 1: first line of the playlist entry, 
    # 2: artist, 
    # 3: second line of playlist entry
    for i, line in enumerate(lines[1:]):
        if (line[0] == '#'):
            playlistTuple = re.findall(r'(#EXTINF:[\d]+,([^-]*).*)', str(line))
            playlistEntry = list(playlistTuple[0])
            playlistEntry.append(lines[i+2])
            newList.append(playlistEntry)

    # sort the new list by artist
    newList.sort(key=lambda el: el[1].lower())

    # write sorted playlist entries to file
    playlistFile = open(playlist, "w", encoding="latin-1")
    playlistFile.write("#EXTM3U\n")
    for el in newList:
        playlistFile.write(el[0] + "\n")
        playlistFile.write(el[2])
    playlistFile.close()


def sortAllPlaylistsInDirectory(directory="."):
    """Sorts each playlist in a directory by artist

    Arguments:
    directory - a string
    """
    os.chdir(directory)
    files = os.listdir()
    for el in files:
        if el.endswith(".m3u"):
            sortPlaylist(el)

# sortAllPlaylistsInDirectory()
