from PyInquirer import prompt, Separator
from os import system
import sys


def main():
    with open('resources/ProfilePic.txt','r') as pic:
        print(pic.read())
     
    prompt([{
            'type': 'input',
            'message': '\n\nPress enter like it\'s 1987 to continue',
            'name': 'continue'
            }])
    clear()
    prompt_main_menu()



def prompt_main_menu():
    try:
        topic = topic_menu()
    except KeyError:
        clear()
        print("Please use the arrow keys")
        prompt_back(lambda : prompt_main_menu())
    if (topic == 'Exit'):            
        exit()
    if (topic == 'Work experience'):
        clear()
        prompt_workplace()
    if (topic == 'Exit'):
        sys.exit()
    with open('resources/'+topic+'.txt','r') as topic:
        print(topic.read()) 
        prompt_back(lambda : prompt_main_menu())
    

def topic_menu():
    topic_prompt = {
        'type': 'list',
        'name': 'topic',
        'message': '',
        'choices': ['Work experience', 'Education', 'Bio', 'Exit']
    }
    answers = prompt(topic_prompt)
    return answers['topic']

def prompt_back(callback):
    prompt([{
            'type': 'input',
            'message': '\n\nPress enter to return...',
            'name': 'continue'
            }])
    clear()
    callback()



def work_menu():    
    experience_prompt = {
        'type': 'list',
        'name': 'experience',
        'message': 'Here are some of the places I have worked at:',
        'choices': [
            'Trackwell',
            'Stokkur',
            'AGR-Reynd',
            'Advania',
            'Einkaleyfastofa',
            Separator('------'),
            'Return to main menu'
        ]
    }
    workAnswers = prompt(experience_prompt)
    return workAnswers['experience']

def prompt_workplace():
    try:
        experience = work_menu()
    except KeyError:
        clear()
        print("Please use the arrow keys")
        prompt_back(lambda : prompt_workplace())
    if (experience == 'Return to main menu'):        
        clear()
        prompt_main_menu()        
    with open('resources/'+experience+'.txt','r') as logo:
        print(logo.read())
    prompt_back(lambda : prompt_workplace())

    
def clear(): 
    _ = system('clear') 

    
if __name__ == '__main__':
    main()