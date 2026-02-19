# demo.py

from llm_gateway import generate

messages = [
    {"role": "system", "content": "You are concise."},
    {"role": "user", "content": "Explain what an API is in one sentence."},
]

print(
    generate(
        provider="together",
        model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
        messages=messages,
    )["text"]
)

print(
    generate(
        provider="anthropic",
        model="claude-haiku-4-5",
        messages=messages,
    )["text"]
)
