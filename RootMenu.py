from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

def topic_menu():
    topic_prompt = {
        'type': 'list',
        'name': 'topic',
        'message': 'Select your area of interest',
        'choices': ['Work experience', 'Education', 'Bio', 'Exit']
    }
    answers = prompt(topic_prompt, style=style)
    return answers['topic']