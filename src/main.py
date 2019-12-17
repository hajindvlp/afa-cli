#!/usr/bin/env python3

import sys
import requests
from clint.textui import progress
from bs4 import BeautifulSoup

from utils.search import Search 
from utils.list import List
from utils.download import Download

def afa():
  listCode, aniName = Search()
  aniCode, epsName = List(listCode, aniName)
  Download(aniCode, epsName)

if __name__ == '__main__':
  afa()