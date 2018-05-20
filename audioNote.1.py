from __future__ import print_function
import pytube
from pytube import YouTube
import nltk.data

yt = YouTube('https://www.youtube.com/watch?v=NiKtZgImdlY')
caption = yt.captions.get_by_language_code('en')
caption = caption.generate_srt_captions()


def delTags(caption):
    start = 0
    end = 0
    for i in range(0, len(caption)):
        if caption[i] == '<':
            start = i
            caption[i] = '*'
        if caption[i] == '>':
            end = i
            for j in range(start, end + 1):
                caption[j] = '*'
    retCaption = []
    for i in caption:
        if i != '*':
            retCaption.append(i)
    return ''.join(retCaption)

def delTimeStamps(caption):
    start = 0
    end = 0
    for i in range(0, len(caption)):
        if caption[i] == '\n' and end >= start:
            start = i
            caption[i] = '*'
        if caption[i] == '\n':
            end = i
            for j in range(start, end + 1):
                caption[j] = '*'
    retCaption = []
    for i in caption:
        if i != '*':
            retCaption.append(i)
    return ''.join(retCaption)
    
def lineNumbers(caption):
    preString = '*'
    postString = '*'
    captionString = ''.join(caption)
    captionString = captionString[1:]
    count = 2
    for i in range(0, len(caption)):
        if str(count) in captionString:
            preString = captionString[:captionString.index(str(count))]
            postString = captionString[captionString.index(str(count))+len(str(count)):]
            captionString = preString + ' ' + postString
        count += 1
    return captionString
    

if '.' in caption:
    print('Subtitles are not auto generated, and may only work for certain videos')
    caption = delTimeStamps(list(caption))
    caption = lineNumbers(list(caption))
    print(caption)
else:
    caption = delTimeStamps(list(caption))
    caption = lineNumbers(list(caption))
    print(caption)

def word_count(string):
    counts = dict()
    words = caption.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


tokens = nltk.word_tokenize(caption)
#sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
#print('\n-----\n'.join(sent_detector.tokenize(caption.strip())))