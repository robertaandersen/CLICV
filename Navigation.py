from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt
from os import system
from examples import custom_style_2, custom_style_1
import sys
import Main
import Work as work
import RootMenu as menu
import Education as education
import Bio as bio 



def prompt_main_menu():

    try:
        topic = menu.topic_menu()
    except KeyError:
        clear()
        print("Please use the arrow keys")        
        prompt_main_menu()
    if (topic == 'Exit'):            
        Main.exit()
    if (topic == 'Work experience'):
        clear()
        work.prompt_user()
    if (topic == 'Education'):
        clear()
        education.prompt_educationList()
    if (topic == 'Bio'):
        clear()
        bio.prompt_educationList()
    else:
        Main.exit()
#    except:        
 #       print("Please use the arrow keys for maximum retro-ness")        


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