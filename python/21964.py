import sys

n = sys.stdin.readline()
song = sys.stdin.readline()



for s in song[len(song)-6:len(song)]:
    print(s, end='')