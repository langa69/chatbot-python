import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
mensagens = [
    {"role": "system", "content": "Você é um assistente útil e amigável."}
]
while True:
    pergunta_usuario = input("\nVocê: ")
    if pergunta_usuario.lower() == "sair":
        break
    try:
        resposta = client.chat.completions.create(
            model="gpt-3.5-turbo", # Ou "gpt-4o-mini" que é mais barato/melhor
            messages=mensagens
        )
        texto_resposta = resposta.choices[0].message.content
        print(f"Bot: {texto_resposta}")
        mensagens.append({"role": "assistant", "content": texto_resposta})

    except Exception as e:
        print(f"Erro na comunicação com a API: {e}")