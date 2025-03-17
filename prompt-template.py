
from langchain.prompts import (PromptTemplate, ChatPromptTemplate, PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, ) 
from langchain.schema import HumanMessage, SystemMessage


template = """以下の料理のレシピを考えてください。 料理 名: {dish} """
prompt = PromptTemplate(input_variables=["dish"], template=template)
result = prompt.format(dish="ハンバーグ")
print(result)


chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("あなたは{country}料理のプロフェッショナルです。"),
    HumanMessagePromptTemplate.from_template("以下の料理のレシピを考えてください。\n\n料理名: {dish}")
])

messages = chat_prompt.format_prompt( country ="イギリス", dish ="肉じゃが").to_messages()

print(messages)
