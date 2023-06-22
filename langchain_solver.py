import streamlit as st
from langchain import OpenAI, LLMMathChain
import os

def get_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

api_key = get_file_contents('api_key.txt')

os.environ["OPENAI_API_KEY"] = api_key
llm = OpenAI(temperature = 0)
llm_math = LLMMathChain.from_llm(llm, verbose = True)

with open('declarative-math-word-problem/algebra222.csv') as f:
    iata = [i.split(',')[0] for i in f.readlines()]

print(iata)
print(len(iata))

# question = input("Enter a mathematical expression: ")
# solution = llm_math.run(question)
# print(solution)

# def main():
#     st.title("Complex Word Math Solver")
#     question = st.text_input("Enter your Math question:")
#     solve_button = st.button("Solve")

#     if solve_button:
#         solution = llm_math.run(question)
#         st.write("Solution:", solution)

# if __name__ == "__main__":
#     main()