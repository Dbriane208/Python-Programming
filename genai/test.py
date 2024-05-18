import requests
import openai

openai.api_key = "sk-proj-Z88MJ5hAhW0u9lnJB0XuT3BlbkFJSYylHd7iAdwFDDvohNvX"

messages = [
    {"role": "system","content":"You generate messages for the given context randomly"}
]

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role":"user", "content": message}
        )
        chat = openai.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages
        )

        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})