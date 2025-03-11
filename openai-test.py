from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      #ai에게 내리는 지시
        {"role": "system", "content": "You are a helpful assistant."},
      #유저가 입력한 메시지
        {
            "role": "user",
            "content": "hi."
        },
    ],
)
print(completion)
