from decouple import config

import openai

openai.api_key = config('SECRET_KEY_OPENAI')

modelo = "gpt-3.5-turbo"
chat_history = []

while True:
    prompt = input('Ingresa un prompt: ')
    if prompt == "exit":
        break
    else:
        chat_history.append({"role": "user", "content": prompt}) 

        response = openai.chat.completions.create(
            model = modelo,
            messages = chat_history,
            stream = True,
            max_tokens = 1000 # tope de respuesta
        )

        collected_messages = []

        for chunk in response:
            chunk_messages = chunk["choise"][0]["delta"] # mensaje
            collected_messages.append(chunk_messages)
            full_reply_content = ''.join([m.get('content', '') for m in collected_messages]) # Bot response
            print(full_reply_content)
            print("\033[H\033[J", end="") # para limpiar la terminal

        chat_history.append({"role": "assistant", "content": full_reply_content})
        print(full_reply_content) # al final lo muestro completo      


