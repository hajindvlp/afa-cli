import requests
import json

TOKEN = "848876705:AAGlO-ppwN2dnDQIDGSA048pwpCFTcdDr5A"
URL = f"https://api.telegram.org/bot{TOKEN}/"
CHATID = 665273272

def getUrl(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def getJson(url):
  content = get_url(url)
  js = json.loads(content)
  return js

def getUpdates():
  url = URL + "getUpdates"
  js = getJson(url)
  return js

def sendMessage(epsName, url):
  text = f"Epsiode Name : {epsName}, URL : {url}"
  url = URL + f"sendMessage?text={text}&chat_id={CHATID}"
  getUrl(url)

def sendVideo(epsName, url):
  text = f"Epsiode Name : {epsName}"
  url = URL + f"sendMessage?text={text}&chat_id={CHATID}"
  getUrl(url)

  url = URL + f"sendVideo?chat_id={CHATID}&video={url}"
  getUrl(url)