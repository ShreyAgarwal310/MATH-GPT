# you'll have to change the file paths to whatever they are on your computer - just these 3
import sys
sys.path.insert(0, '/Users/shreyagarwal/Code/GitHub/MATH-GPT/declarative-math-word-problem')
sys.path.insert(0, '/Users/shreyagarwal/Code/GitHub/MATH-GPT/declarative-math-word-problem/prompts')
sys.path.insert(0, '/Users/shreyagarwal/Code/GitHub/MATH-GPT/pal')
import tkinter as tk
from utils import *
from declarative_three_shot import DECLARATIVE_THREE_SHOT_AND_PRINCIPLES
import openai
import pal
from pal.prompt import math_prompts
from langchain import OpenAI, LLMMathChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
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
root.title('math-gpt')
root.resizable(False, False)

interface = pal.interface.ProgramInterface(
  model='text-davinci-003',
  stop='\n\n\n', # stop generation str for Codex API
  get_answer_expr='solution()' # python expression evaluated after generated code to obtain answer 
)

def chat_with_gpt(prompt):
    response=openai.Completion.create(
        engine='text-davinci-003',  # Choose the appropriate GPT model
        prompt=prompt,
        max_tokens=100,  # Adjust as needed to control the response length
        temperature=0.7,  # Adjust as needed to control the response randomness
    )
    return response.choices

os.environ["OPENAI_API_KEY"] = api_key
llm = OpenAI(temperature=0, model_name="text-davinci-003")
tools = load_tools(["llm-math"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    return_intermediate_steps=True,
)

# initialize the canvas
canvas1 = tk.Canvas(root, width=750, height=750)
canvas1.pack()

# title text
title_text = tk.Label(canvas1, bg="white", fg="black", height=1, width=8, font=("Gill Sans MT", 36))
title_text.place(relx=0.5, y=20, anchor="center")
title_text.config(text='math-gpt')

names_text = tk.Label(canvas1, bg="white", fg="black", height=1, width=53, font=("Gill Sans MT", 20))
names_text.place(relx=0.5, y=70, anchor="center")
names_text.config(text='Shrey Agarwal, Christina Xu, Hamid Bagheri, Lisong Xu')

prompt_label = tk.Label(canvas1, bg="white", fg="black", height=1, width=50, font=("Gill Sans MT", 14))
prompt_label.place(relx=0.5, y=120, anchor="center")
prompt_label.config(text='Enter Prompt:')

method_label = tk.Label(canvas1, bg="white", fg="black", height=1, width=50, font=("Gill Sans MT", 14))
method_label.place(relx=0.5, y=190, anchor="center")
method_label.config(text="Choose your method after you've entered your prompt:")

answer_label = tk.Label(canvas1, bg="white", fg="black", height=1, width=50, font=("Gill Sans MT", 14))
answer_label.place(relx=0.5, y=290, anchor="center")
answer_label.config(text="The answer will be displayed here:")

explanation_label = tk.Label(canvas1, bg="white", fg="black", height=1, width=65, font=("Gill Sans MT", 14))
explanation_label.place(relx=0.5, y=390, anchor="center")
explanation_label.config(text="For the vanilla DaVinci and the Symbolic Solver, an explanation will be provided here:")

# create the entry box
entry1 = tk.Entry(width=50, font=("Arial 16"), bg="white", fg="black", justify='center')
entry1.pack(padx=10, pady=10)
entry1.place(relx=0.5, y = 150, anchor="center")

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
    response = agent(
        {
            "input": x1
        }
    )
    l = response["intermediate_steps"]
    list = l[0]
    explanation_text.config(text="")
    answer_text.config(text=str(list[1]))
    explanation_text.config(text=str(list[0]).split(", ", 2)[2][6:-2])

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
canvas1.create_window(225, 240, window=button1)

button2 = tk.Button(text='LangChain', command=use_langchain)
canvas1.create_window(345, 240, window=button2)

button3 = tk.Button(text='PAL', command=use_pal)
canvas1.create_window(425, 240, window=button3)

button3 = tk.Button(text='Symbolic Solver', command=use_symbolic_solver)
canvas1.create_window(525, 240, window=button3)

answer_text = tk.Label(canvas1, bg="white", fg="black", height=1, width=65, font=("Gill Sans MT", 14))
answer_text.place(relx=0.5, y=340, anchor="center")

explanation_text = tk.Label(canvas1, bg="white", fg="black", height=10, width=65, font=("Gill Sans MT", 14), wraplength=300, justify='center')
explanation_text.place(relx=0.5, y=520, anchor="center")

root.mainloop()
