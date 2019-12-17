import sys
import requests
from clint.textui import progress
from PyInquirer import style_from_dict, Token, prompt, Separator
from bs4 import BeautifulSoup

style = style_from_dict({
    Token.Separator: '#cc5454 bold',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction:'bold',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

def Search():
  print("[*] Anime Search String : ", end="")
  # try:
  searchString = input()

  url = f"https://ani24zo.com/ani/search.php?query={searchString}&search_button=%EA%B2%80%EC%83%89"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'lxml')
  linkList = soup.findAll("a", {"class": "subject"})

  questions = [{
    'type': 'list',
    'message': 'Selected Ani',
    'name': 'listCode',
    'choices': [
      Separator(f'= Search Results of {searchString} ... =')
    ],
    'validate': lambda answer: 'You must choose an Ani.' \
        if len(answer) == 0 else True
  }]

  for link in linkList:
    code =  link['href'].split("/")[-1].split(".")[0]
    name = link.get_text()
    questions[0]["choices"].append({'name': f"{name} @ {code}"})

  answers = prompt(questions, style=style)
  code = answers['listCode'].split('@')[-1][1:]
  aniName = answers['listCode'].split('@')[0]
  
  return code, aniName

  # except:
  #   print("[*] Error on Searching")