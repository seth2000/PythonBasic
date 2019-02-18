# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:22:00 2019

@author: s.lee


    pip install pytube
    
    # Change the youtbe code in the URL will be enough
    python
    >>> from pytube import YouTube
    >>> YouTube('http://youtube.com/watch?v=QNT8jBmtQP8&autoplay=1&loop=1&rel=0').streams.first().download()
    
    Please remember adding the parameters as  &autoplay=1&loop=1&rel=0 which is very important to download the files.


    Usage: Python YoutubeToMP4.py QNT8jBmtQP8
"""

import sys

from pytube import YouTube

def main(argv):
    if len(argv) != 1:
        print("Usage: Python YoutubeToMP4.py QNT8jBmtQP8")
    else:
        YouTube(f'http://youtube.com/watch?v={argv[0]}&autoplay=1&loop=1&rel=0').streams.first().download()

if __name__ == "__main__":
   main(sys.argv[1:])
   

