import openai
import sys
sys.path.insert(0, '/Users/shreyagarwal/Code/GitHub/MATH-GPT/pal')
import pal
from pal.prompt import colored_object_prompt, math_prompts
import os
from langchain.chains import PALChain
from langchain import OpenAI
from langchain.chains.llm import LLMChain

def get_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

api_key = get_file_contents('api_key.txt')

openai.api_key = api_key
os.environ["OPENAI_API_KEY"] = api_key
llm = OpenAI(model_name='code-davinci-edit-001',
             temperature=0,
             max_tokens=512)

pal_chain = PALChain.from_colored_object_prompt(llm, verbose=True)
question = "The cafeteria has 23 apples. If they used 20 for lunch and bought 6 more, how many apples do they have?"
pal_chain.run(question)