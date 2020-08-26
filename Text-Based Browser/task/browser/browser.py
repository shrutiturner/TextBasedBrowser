import os
import requests
import sys
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
from collections import deque

init()

folder_name = sys.argv[1]
if not os.path.exists(folder_name):
    os.mkdir(folder_name)


while True:
    input_str = input()
    if input_str == "exit":
        break
    elif '.' in input_str:
        file_name = ''.join(input_str.split('.')[:-1])
        file_path = os.path.join(folder_name, file_name)

        if input_str[0:7] == 'https://':
            pass
        else:
            input_str = 'https://' + input_str

        web_request = requests.get(input_str)

        soup = BeautifulSoup(web_request.content, 'html.parser')

        x = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])

        final_text = ''
        for i in x:
            if i.script:
                i.script.extract()
            _text = ''
            if i.a:
                _text += Fore.BLUE + i.text
            else:
                _text += i.text
            final_text += _text

        with open(file_path, 'w') as file:
            file.write(final_text)

        print(final_text)


