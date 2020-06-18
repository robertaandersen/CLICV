from __future__ import print_function, unicode_literals
from PyInquirer import prompt

def topic_menu():
    topic_prompt = {
        'type': 'list',
        'name': 'topic',
        'message': 'Which direction would you like to go?',
        'choices': ['Work experience', 'Education', 'Bio', 'Exit']
    }
    answers = prompt(topic_prompt)
    return answers['topic']