from pydantic import BaseModel, Field 
from langchain. output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from openai import OpenAI
from langchain.schema import HumanMessage
from langchain_openai import ChatOpenAI

client = OpenAI()

class Recipe( BaseModel): 
  ingredients: list[str] = Field( description =" ingredients of the dish") 
steps: list[str] = Field( description ="steps to make the dish")
parser = PydanticOutputParser( pydantic_object = Recipe)

format_instructions = parser. get_format_instructions()
print(format_instructions)
template = """料理のレシピを考えてください。{format_instructions} 料理名: {dish} """ 
prompt = PromptTemplate(template = template, input_variables =["dish"], partial_variables ={"format_instructions": format_instructions})

formatted_prompt = prompt.format(dish="カレー")
print(formatted_prompt)



chat = ChatOpenAI(model ="gpt-4o-mini", temperature = 0) 
messages = [HumanMessage(content = formatted_prompt)] 
output = chat( messages) 
print( output.content)

recipe = parser.parse(output.content) 
print(type(recipe)) 
print(recipe)

