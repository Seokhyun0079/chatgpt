from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
result = llm("自己紹介してください。")
print(result)

