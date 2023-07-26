from utils import *
from prompts.declarative_three_shot import DECLARATIVE_THREE_SHOT_AND_PRINCIPLES
from prompts.declarative_eight_shot import DECLARATIVE_EIGHT_SHOT
import openai

def get_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

api_key = get_file_contents('api_key.txt')
openai.api_key = api_key

question = input("Enter a mathematical expression: ")

eq_list = get_declarative_equations(model='text-davinci-003', question=question, prompt=DECLARATIVE_EIGHT_SHOT, max_tokens=600, stop_token='\n\n\n', temperature=0)
answer = get_final_using_sympy(eq_list)
print(eq_list)
print(answer)