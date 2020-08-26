import os
import requests
import sys
from bs4 import BeautifulSoup
from collections import deque

folder_name = sys.argv[1]
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

stack = deque()

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

        text = soup.get_text()

        stack.append(input_str)
        with open(file_path, 'w') as file:
            file.write(text)

        print(text)
"""
        try:
            file_path = os.path.join(folder_name, input_str)
            with open(file_path, 'r') as file:
                print(file.read)
        except FileNotFoundError:
            print("Error: Incorrect URL")

    elif 'back' in input_str:
        if len(stack) > 0:
            if stack[-2] == "bloomberg.com":
                print(bloomberg_com)
                stack.pop()
                continue
"""


