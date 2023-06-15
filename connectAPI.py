import openai

# Set up your OpenAI API credentials
openai.api_key = 'API_KEY'

# Define the function to interact with ChatGPT


def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Choose the appropriate GPT model
        prompt=prompt,
        max_tokens=100,  # Adjust as needed to control the response length
        temperature=0.7,  # Adjust as needed to control the response randomness
        n=3,  # Number of alternative completions to generate
        stop=None,  # Stop generating after a specific token (optional)
    )

    return response.choices


# Step 1: Receive the mathematical expression from the user
expression = input("Enter a mathematical expression: ")

# Step 2: Prepare the input for ChatGPT
prompt = f"Given the expression '{expression}', please generate a function that does not contain floating-point extensions or iterations."

# Step 3: Interact with ChatGPT
response_choices = chat_with_gpt(prompt)

# Step 4: Parse and process the response choices
generated_functions = [choice.text.strip() for choice in response_choices]

# Print the generated functions
for i, function in enumerate(generated_functions, start=1):
    print(f"Generated function {i}: {function}")


