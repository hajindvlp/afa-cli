import sys
import requests
from clint.textui import progress
from bs4 import BeautifulSoup

from utils.send import sendMessage

def TryDownload(epsName, url, idx):
  with requests.get(url, stream=True) as response:
    if(response.status_code == 200):
      sendMessage(epsName, url)
      print(f"= Successed on mirror{idx} site =")
      totalLength = response.headers.get('content-length')
      f = open(f"/home/hajin/Videos/{epsName}.mp4", "wb")

      if totalLength is None:
        f.write(response.content)
      else:
        dl = 0
        totalLength = int(totalLength)
        for chunk in progress.bar(response.iter_content(chunk_size=8192), expected_size=(totalLength/8192) + 1): 
          if chunk:
            f.write(chunk)
            f.flush()
      return True
    else:
      print(f"= Failed on mirror{idx} site =")
      return False

def Download(aniCode, epsName):
  print(f"= Downloading {epsName} =")

  startSec = int(int(aniCode)/4000)*4000+1
  endSec = (int(int(aniCode)/4000)+1)*4000

  urls = [
    f"http://files0.filegroupa.com/files/0/new/id_{aniCode}.mp4",
    f"http://files1.filegroupa.com/files/0/new/id_{aniCode}.mp4",
    f"http://files2.filegroupa.com/files/0/new/id_{aniCode}.mp4",
    f"http://files2.filegroupa.com/files/0/{startSec}~{endSec}/id_{aniCode}.mp4",
    f"http://gasfsa.com/abab/id_{aniCode}.mp4"
  ]

  for idx, url in enumerate(urls):
    stop = TryDownload(epsName, url, idx)

    if(stop): break