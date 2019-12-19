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
		
def List(listCode, aniName):
  url = f"https://ani24zo.com/ani_list/{listCode}.html"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'lxml')

  nameList = soup.findAll("div", {"class": "subject"})

  questions = [{
    'type': 'list',
    'message': 'Selected Ani',
    'name': 'aniCode',
    'choices': [
      Separator(f'= Episodes of {aniName} ... ='),
      {"name": "Search"}
    ],
    'validate': lambda answer: 'You must choose an Ani.' \
        if len(answer) == 0 else True
  }]

  for name in reversed(nameList):
    aniName = name.get_text()
    aniImg = soup.find("img", {"alt": aniName})
    aniCode = aniImg["src"].split("/")[-1].split(".")[0]

    questions[0]['choices'].append({'name': f'{aniName} @ {aniCode}'})
  
  answers = prompt(questions, style=style)
  if(answers['aniCode'] == 'Search'):
    return -1, -1

  code = answers['aniCode'].split('@')[-1][1:]
  aniName = answers['aniCode'].split('@')[0]

  return code, aniName
