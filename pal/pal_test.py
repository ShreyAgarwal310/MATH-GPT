import pal
from pal.prompt import math_prompts
import openai

def get_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

api_key = get_file_contents('api_key.txt')
openai.api_key = api_key

interface = pal.interface.ProgramInterface(
  model='text-davinci-003',
  stop='\n\n\n', # stop generation str for Codex API
  get_answer_expr='solution()' # python expression evaluated after generated code to obtain answer 
)

# def solution():
#     "Bob says to Alice: if you give me 3 apples and then take half of my apples away, then I will be left with 13 apples. How many apples do I have now?"
#     apple_given = 3
#     apple_left = 13
#     apple_now = (apple_left + apple_given) * 2
#     result = apple_now
#     return result

# print(solution())

question = 'The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store returned 6 unsold loaves. How many loaves of bread did they have?'
prompt = math_prompts.MATH_PROMPT.format(question=question)
answer = interface.run(prompt)
print(answer)