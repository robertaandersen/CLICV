from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt
import Work as work
import RootMenu as menu
from os import system
import sys
from examples import custom_style_2, custom_style_1


def prompt_main_menu():
    try:        
        topic = menu.topic_menu()    
        if (topic == 'Exit'):
            print('Bye now')
            sys.exit()
        if (topic == 'Work experience'):
            clear()
            work.prompt_user()
        else:
            prompt_main_menu()
    except:
        print("Please use the arrow keys for maximum retroness")
        prompt_main_menu()


def prompt_back(callback):
    prompt([{
            'type': 'input',
            'message': '\n\n\n\nPress enter to return...',
            'name': 'continue'
            }],style=custom_style_1
        )
    clear()
    callback()
    
    

def clear(): 
    _ = system('clear') 