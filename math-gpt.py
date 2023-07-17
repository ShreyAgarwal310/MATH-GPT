
import tkinter as tk
import sys
# you'll have to change the file paths to whatever they are on your computer - just these 3
sys.path.insert(0, '/Users/shreyagarwal/Code/GitHub/MATH-GPT/declarative-math-word-problem')
from utils import *
sys.path.insert(0, '/Users/shreyagarwal/Code/GitHub/MATH-GPT/declarative-math-word-problem/prompts')
from declarative_three_shot import DECLARATIVE_THREE_SHOT_AND_PRINCIPLES
import openai
sys.path.insert(0, '/Users/shreyagarwal/Code/GitHub/MATH-GPT/pal')
import pal
from pal.prompt import math_prompts
from langchain import OpenAI, LLMMathChain
import os

# access the api key from whatever file you have it in
def get_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

api_key = get_file_contents('api_key.txt')
openai.api_key = api_key

root= tk.Tk()

interface = pal.interface.ProgramInterface(
  model='text-davinci-003',
  stop='\n\n\n', # stop generation str for Codex API
  get_answer_expr='solution()' # python expression evaluated after generated code to obtain answer 
)

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Choose the appropriate GPT model
        prompt=prompt,
        max_tokens=100,  # Adjust as needed to control the response length
        temperature=0.7,  # Adjust as needed to control the response randomness
    )

    return response.choices

os.environ["OPENAI_API_KEY"] = api_key

# initialize the canvas
canvas1 = tk.Canvas(root, width=750, height=500)
canvas1.pack()

# create the entry box
entry1 = tk.Entry(width=50, font=("Arial 16"), bg="white", fg="black", justify='center')
entry1.pack(padx=10, pady=10)
canvas1.create_window(350, 120, window=entry1)

# function to call for using vanilla davinci
def use_vanilla_davinci():  
    expression = entry1.get()
    # finding the answer
    prompt_for_answer = f"Given the expression '{expression}', please generate an answer."
    response_choices = chat_with_gpt(prompt_for_answer)
    answer = [choice.text.strip() for choice in response_choices]
    # finding the explanation
    prompt_for_explanation = f"Given the expression '{expression}', please write a solution that correctly addresses the problem and solves it."
    response_choices_for_explanation = chat_with_gpt(prompt_for_explanation)
    answer_for_explanation = [choice.text.strip() for choice in response_choices_for_explanation]
    # configuring labels to display answer and explanation
    explanation_text.config(text="")
    answer_text.config(text=f"Vanilla answer: '{answer}'.")
    explanation_text.config(text=answer_for_explanation)

# function to call for using langchain
def use_langchain():  
    x1 = entry1.get()
    llm = OpenAI(temperature = 0)
    llm_math = LLMMathChain.from_llm(llm, verbose = True)
    answer = llm_math.run(x1)
    explanation_text.config(text="")
    answer_text.config(text=f"Langchain answer: '{answer[8:]}'.")

# function to call for using PAL
def use_pal():  
    x1 = entry1.get()
    prompt = math_prompts.MATH_PROMPT.format(question=x1)
    answer = interface.run(prompt)
    explanation_text.config(text="")
    answer_text.config(text=f"PAL answer: '{answer}'.")

# function to call for using the symbolic solver
def use_symbolic_solver():  
    x1 = entry1.get()
    eq_list = get_declarative_equations(model='text-davinci-003', question=x1, prompt=DECLARATIVE_THREE_SHOT_AND_PRINCIPLES, max_tokens=600, stop_token='\n\n\n', temperature=0)
    answer = get_final_using_sympy(eq_list)
    explanation_text.config(text="")
    answer_text.config(text=f"Symbolic Solver answer: '{answer}'.")
    explanation_text.config(text=eq_list)

# creating all the buttons and the answer text
button1 = tk.Button(text='Vanilla DaVinci', command=use_vanilla_davinci)
canvas1.create_window(200, 180, window=button1)

button2 = tk.Button(text='LangChain', command=use_langchain)
canvas1.create_window(315, 180, window=button2)

button3 = tk.Button(text='PAL', command=use_pal)
canvas1.create_window(400, 180, window=button3)

button3 = tk.Button(text='Symbolic Solver', command=use_symbolic_solver)
canvas1.create_window(500, 180, window=button3)

answer_text = tk.Label(canvas1, bg="white", fg="black", height=1, width=65, font=("Gill Sans MT", 14))
answer_text.place(x=50, y=230)

explanation_text = tk.Label(canvas1, bg="white", fg="black", height=10, width=65, font=("Gill Sans MT", 14), wraplength=300, justify='center')
explanation_text.place(x=50, y=270)

root.mainloop()