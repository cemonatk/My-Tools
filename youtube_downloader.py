#!/usr/bin/env python
# -*- coding: utf-8 -*-

__DATE__ = '09.10.2016'
__AUTHOR__ = 'cemonatk'


def ReadTxt(file):
    return [line.split(',') for line in [line.strip() for line in open(file)]]
    
def CrawlSite(link):
    # returns videolist[]
    pass

def ParseId(link):
    return (parse_qs(urlparse(link).query))["v"][0]

def Check(data):
    print data

def LogError(data):
    with open(logpath+'log.txt','a+') as f:
        f.write(data+'\n')
        f.close()

def Download(url):
    data = parse_qs(urlopen(url).read())
    filename = savepath+str(data['title'][0])+'.mp4'
    videos = (data['url_encoded_fmt_stream_map'][0]).split(',')
    url = str(parse_qs(videos[0])["url"][0])
    urlretrieve(url,filename)
    return filename

def VideoToMusic(video):
    # return music
    #AudioSegment.from_file('test.mp4').export('test', format="mp3")
    pass

if(__name__ == '__main__'):
    from urllib2 import urlopen
    from urllib import urlretrieve
    from urlparse import parse_qs, urlparse
    from sys import argv
    from datetime import datetime

    # videolistfile = argv[1]
    videolistfile = 'list.txt'
    savepath = 'C:\Users\ XXX \Desktop\\'
    logpath = 'C:\Users\ XXX \Desktop\\'
    #foo = 'https://www.youtube.com/watch?v=XXX'

    url = 'https://www.youtube.com/get_video_info?video_id='
    videolist = ReadTxt(videolistfile)

    for v in videolist:
        for video in filter(None, v):
            try:
                #VideoToMusic(Download(url+ParseId(video)))
                Download(url+ParseId(video))
            except:
                LogError("Couldn't Save this => "+video+'\t'+str(datetime.now()))
                pass



# video temp' e , win ise nt ise temp, posix ise tmp
# bazı telif vs lere çözüm? 403?