from __future__ import print_function
import pytube
from pytube import YouTube
import nltk.data

yt = YouTube('https://www.youtube.com/watch?v=arj7oStGLkU')
caption = yt.captions.get_by_language_code('en')
caption = caption.generate_srt_captions()

def delTimeStamps(caption):
    start = 0
    end = 0
    preString = ''
    postString = ''
    caption = ' ' + caption[1:]
    while ' \n' in caption:
        preString = caption[:caption.index(' \n')]
        postString = caption[caption.index('\n') + 1:]
        postString = postString[postString.index('\n') + 1:]
        caption = preString + ' ' + postString
    return caption
            

def lineNumbers(caption):
    preString = ''
    postString = ''
    captionList = list(caption)
    count = 2
    for i in range(0, len(caption)):
        dele = '\n\n' + str(count)
        if dele in caption:
            preString = caption[:caption.index(dele)]
            postString = caption[caption.index(dele)+len(dele):]
            caption = preString + ' ' + postString
        count += 1
    return caption
    
caption = lineNumbers(caption)
caption = delTimeStamps(caption)
print(caption)


