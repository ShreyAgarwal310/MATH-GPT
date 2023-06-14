import pal
from pal.prompt import math_prompts

interface = pal.ProgramInterface(
  model='code-davinci-002',
  stop='\n\n\n', # stop generation str for Codex API
  get_answer_expr='solution()' # python expression evaluated after generated code to obtain answer 
)

question = 'The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store returned 6 unsold loaves. How many loaves of bread did they have?'
prompt = math_prompts.MATH_PROMPT.format(question=question)
answer = interface.run(prompt)