import os
import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

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
        if input_str == "bloomberg.com":
            with open(file_path, 'w') as file:
                file.write(bloomberg_com)
            print(bloomberg_com)
        elif input_str == "nytimes.com":
            with open(file_path, 'w') as file:
                file.write(nytimes_com)
            print(nytimes_com)

    try:
        file_path = os.path.join(folder_name, input_str)
        with open(file_path, 'r') as file:
            print(file.read)
    except FileNotFoundError:
        print("Error: Incorrect URL")
