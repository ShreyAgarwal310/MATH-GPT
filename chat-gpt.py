import openai

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

#test