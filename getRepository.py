#!/usr/bin/env python3
#
# Author: Joshua Wolfe (jbwolfe)
# The must-have, go-to script for cloning and/or pulling the latest lusth-music 
#     student repositories. This script ignores utility repositories

import os
import urllib.request
from html.parser import HTMLParser

class parseClass(HTMLParser):
  def handle_starttag(self, tag, attrs):
    ignore = ["getpack", "instrumentPlayer", "getRepository", "lusth-music.github.io"]
    if(tag == "a"):
      if(attrs[0][0]=='href' and attrs[0][1][1:12]=="lusth-music"):
        if(attrs[0][1][13:] not in ignore):
          print()
          if(not os.path.exists(attrs[0][1][13:])):
            #print("git clone https://github.com/lusth-music/"+attrs[0][1][13:])
            os.system("git clone https://github.com/lusth-music/"+attrs[0][1][13:])
          else:
            print("Entering: " + attrs[0][1][13:])
            os.chdir(attrs[0][1][13:])
            #print("git pull")
            os.system("git pull")
            print("Leaving: " + attrs[0][1][13:])
            os.chdir("..")

def main():
  url = "https://github.com/lusth-music"
  try:
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
  except:
    print("Error: could not reach lusth-music repository")

  parser = parseClass()
  parser.feed(text.strip())

main()
