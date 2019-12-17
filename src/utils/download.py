import sys
import requests
from clint.textui import progress
from bs4 import BeautifulSoup

def TryDownload(epsName, url, idx):
  response = requests.get(url)

  if(response.status_code == 200):
    print(f"= Successed on mirror{idx} site =")
    totalLength = response.headers.get('content-length')
    f = open(f"../../donwloads/{epsName}.mp4", "wb")

    if totalLength is None:
      f.write(response.content)
    else:
      dl = 0
      totalLength = int(totalLength)
      for chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(totalLength/1024) + 1): 
        if chunk:
          f.write(chunk)
          f.flush()
  else:
    print(f"= Failed on mirror{idx} site =")

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
    TryDownload(epsName, url, idx)