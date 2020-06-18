from examples import custom_style_2
from PyInquirer import prompt, Separator
from examples import custom_style_1
import Navigation as navigate
import Main

from pyfiglet import Figlet
f = Figlet(font='speed')


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
    workAnswers = prompt(experience_prompt,style=custom_style_2)
    return workAnswers['experience']

def prompt_user():    
    experience = work_menu()     
    if (experience == 'Return to main menu'):        
        navigate.prompt_main_menu()
        return   
    if (experience == 'Trackwell'):       
        trackwell()
    if (experience == 'Stokkur'):       
        stokkur()
    if (experience == 'AGR-Reynd'):       
        agr_reynd()
    if (experience == 'Advania'):       
        advania()
    if (experience == 'Einkaleyfastofa'):       
        einkaleyfastofa()
    
    navigate.prompt_back(lambda : prompt_user())
    

def trackwell():    
    print(f.renderText('Trackwell'))
    print('+----------+---------+')
    print('| Aug 2017   Present |')
    print('|  Senior developer  |')
    print('+--------------------+')
    print()


def stokkur():    
    print(f.renderText('Stokkur'))
    print('+----------+---------+')
    print('| Aug 2017   Present |')
    print('|  Senior developer  |')
    print('+--------------------+')

def agr_reynd():    
    print(f.renderText('AGR - Reynd'))
    print('+----------+---------+')
    print('| Aug 2017   Present |')
    print('|  Senior developer  |')
    print('+--------------------+')

def advania():    
    print(f.renderText('Advania'))
    print('+----------+---------+')
    print('| Aug 2017   Present |')
    print('|  Senior developer  |')
    print('+--------------------+')

def einkaleyfastofa():    
    print(f.renderText('Einkaleyfastofa'))
    print('+----------+---------+')
    print('| Aug 2017   Present |')
    print('|  Senior developer  |')
    print('+--------------------+')