#!/usr/bin/env python3

import sys
import requests
from clint.textui import progress
from bs4 import BeautifulSoup

from utils.search import Search 
from utils.list import List
from utils.download import Download

def afa():
  while True:
    listCode, aniName = Search()
    if(listCode == -1 and aniName == -1):
      continue
    aniCode, epsName = List(listCode, aniName)
    if(aniCode != -1 and epsName != -1):
      break
  Download(aniCode, epsName)

if __name__ == '__main__':
  afa()