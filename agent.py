import anthropic

system_prompt = open("prompt.md").read()
client = anthropic.Anthropic(api_key="XXX")
history = []

print("Design agent ready. Type your request.\n")

while True:
    user_input = input("You: ")
    history.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=8000,
        system=system_prompt,
        messages=history
    )

    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    print(f"\nAgent: {reply}\n")
