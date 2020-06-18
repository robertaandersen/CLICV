from examples import custom_style_2
from PyInquirer import prompt, Separator
from examples import custom_style_1
import Navigation as navigate

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
    answers = prompt(experience_prompt,style=custom_style_2)
    return answers['experience']

def prompt_user():    
    experience = work_menu()     
    if (experience == 'Return to main menu'):
        navigate.prompt_main_menu()   
    if (experience == 'Trackwell'):       
        trackwell()         
    navigate.prompt_back(lambda : prompt_user())
    

def trackwell():
    print('stuffff')