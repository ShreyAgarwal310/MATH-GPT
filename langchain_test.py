from langchain import OpenAI, LLMMathChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import os

def get_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

api_key = get_file_contents('api_key.txt')

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

response = agent(
    {
        "input": "What is 4+4?"
    }
)

l = response["intermediate_steps"]

# question = input("Enter a mathematical expression: ")
 
# llm_math.run(question)