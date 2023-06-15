import openai
import ast
import math
import re

def get_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

api_key = get_file_contents('api_key.txt')
openai.api_key = api_key

def chat_with_gpt(prompt):
    reponse = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 100,
        temperature = 0.2,
        n = 5,
        stop = None
    )

    return reponse.choices

# expression = input("Enter a mathematical expression: ")

# prompt = f"Given the expression (expression]', please generate an integer-based function in C with the name compute_result that computes the result without using floating-point operations (like sqrt) and without using iterations (like while and for loop). The function should take the same parameters but in integer-based form and return an integer result and have the highest approximation result compared to the original expression and please ouput exact like this format:\n\nint compute_result(int x) {{\n *your code goes here*\n}} (remember the open bracket is at same line as function name do not break line for open bracket."

# response_choices = chat_with_gpt(prompt)

# Step 1: Receive the mathematical expression from the user
expression = input("Enter a mathematical expression: ")

# Step 2: Prepare the input for ChatGPT
prompt = f"Given the expression '{expression}', please write a solution that correctly addresses the problem and solves it."

# Step 3: Interact with ChatGPT
response_choices = chat_with_gpt(prompt)

# Step 4: Parse and process the response choices
generated_functions = [choice.text.strip() for choice in response_choices]

# Print the generated functions
for i, function in enumerate(generated_functions, start=1):
    print(f"Generated function {i}: {function}")