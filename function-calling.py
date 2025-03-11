import json 
from openai import OpenAI

client = OpenAI()
def get_current_weather( location, unit =" celsius") : 
  weather_info = { "location": location, "temperature": "25", "unit": "celsius", "forecast": ["sunny", "windy"], } 
  return json. dumps( weather_info)

functions = [ 
  { 
    "name": "get_current_weather", 
    "description": "Get the current weather in a given location", 
    "parameters": { 
      "type": "object", "properties": 
      { 
        "location": { "type": "string", "description": "The city and state, e. g. Tokyo", }, 
        "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }, }, 
        "required": ["location"], 
    }, 
  } 
]

messages = [ 
  {
    "role": "user", 
    "content": "오늘 도쿄날씨 어때?"
  } 
] 
response = client.chat.completions.create(
    model="gpt-4o-mini", 
    messages = messages, 
    functions = functions 
    ) 
print(response)

