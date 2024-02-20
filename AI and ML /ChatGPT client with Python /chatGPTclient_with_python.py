import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
#print(os.environ.get("OPENAI_API_KEY"))

client = OpenAI(api_key=api_key)

while True:
    question = input('What is your question (type "quit" to exit): ')

    if question.lower() == 'quit':
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot knowledgeable in Cisco network technology"},
                {"role": "user", "content": f"{question}"},
                #{"role": "system", "content": "Provide a step-by-step guide."},
                #{"role": "assistant", "content": "As a Cisco-focused assistant, I can help you with queries related to network configurations, Cisco products, troubleshooting, and more."}
            ]
        )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(f"We asked ChatGPT: {question} - Here is their answer:")
    print("-----------------------------------------------------------------")
    print(result)
    
