from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain, SimpleSequentialChain

chat = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

cot_template = """以下の質問に回答してください。 質問: {question} ステップバイステップ で考えましょう。""" 
cot_prompt = PromptTemplate(input_variables =[" question"], template = cot_template, ) 
cot_chain = LLMChain( llm = chat, prompt = cot_prompt)



summarize_template = """以下の文章を結論だけ 一言に要約してください。 {input} """ 
summarize_prompt = PromptTemplate( input_variables =[" input"], template = summarize_template, ) 
summarize_chain = LLMChain( llm = chat, prompt = summarize_prompt)
cot_summarize_chain = SimpleSequentialChain(chains =[cot_chain, summarize_chain]) 
result = cot_summarize_chain( "私は市場に行って10個 のリンゴを買いました。隣人に2つ、修理工に2つ渡しました。それ から 5 つ の リンゴ を 買っ て 1 つ 食べ まし た。 残り は 何個 です か？" ) 
print( result["output"])

