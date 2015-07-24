import sys
from bs4 import BeautifulSoup
import urllib2, urllib

def getLyricsHtml (songName, artistName):
  BASE_URL="http://lyrics.wikia.com/api.php"
  args = { 
    'artist': artistName,
    'song' : songName,
    'fmt' : "xml"
  }
  data = urllib.urlencode (args)
  url = "{0}?{1}".format(BASE_URL, data)
  res = urllib2.urlopen (url).read()
  return res

def getFullLyricsUrl (xml):
  soup = BeautifulSoup (xml, "html.parser")
  url = soup.find ("url")

  if url:
    return url.contents[0]

  raise Exception("Lyrics not available")

def getFullLyricsFromUrl (url):
  html = urllib2.urlopen (url).read()
  soup = BeautifulSoup (html, "html.parser")

  box = soup.find("div", {"class" : "lyricbox"})
  children = [child for child in box.children]

  try:
    lyricsChildren = children[1:-5]
    strLyrics = map(str, lyricsChildren)
    lyrics = "".join (strLyrics).replace ("<br/>", "\n")
    return lyrics
  except:
    raise Exception("Lyrics not available")

  raise Exception ("Unreachable")

def getLyrics (songName, artistName):
  response = getLyricsHtml (songName, artistName)

  try:
    url = getFullLyricsUrl (response)
    lyrics = getFullLyricsFromUrl (url)
    return lyrics
  except:
    return "Sorry! Lyrics not available!"
  
  raise Exception ("Unreachable")

if __name__=="__main__":
  if len (sys.argv) < 3:
    print ("Usage: ./py <SONG_NAME> <ARTIST_NAME>")
    sys.exit (1)

  songName = sys.argv[1]
  artistName = sys.argv[2]
  print getLyrics (songName, artistName)
