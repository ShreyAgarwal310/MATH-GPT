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
        "input": "It takes Bongo two and a half hours to mow the front lawn. Find how many times he can mow the same lawn in 40 hours."
    }
)

l = response["intermediate_steps"]
# print(l)
# list = l[1]
# print(str(list[1]))
# print(str(list[0]).split(", ", 2)[2][6:-2])
# print(len(list))

# for i in list:
#     print(i)

if len(l) >= 2:
    print(str(l[len(l) - 1][1]))
    for i in l:
        print(str(i[0]).split(", ", 2)[2][6:-2])
    # first_list = l[0]
    # list = l[len(l) - 1]
    # print(str(first_list[0]).split(", ", 2)[2][6:-2])
    # print(str(list[0]).split(", ", 2)[2][6:-2])
    # .split(", ", 2)[2][6:-2]

# question = input("Enter a mathematical expression: ")

# [(AgentAction(tool='Calculator', tool_input='2.5/1', log=' I need to figure out how long it takes Bongo to mow the lawn once.\nAction: Calculator\nAction Input: 2.5/1'), 'Answer: 2.5'), (AgentAction(tool='Calculator', tool_input='40/2.5', log=' I need to figure out how many times Bongo can mow the lawn in 40 hours.\nAction: Calculator\nAction Input: 40/2.5'), 'Answer: 16.0')]

# llm_math.run(question)