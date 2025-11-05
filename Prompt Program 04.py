# Task 04 – Simulating an Assistant (Example: Job Interview Bot)

assistant_intro = "You are a friendly job interview assistant for data science roles."
conversation = [
    {"role": "system", "content": assistant_intro},
    {"role": "user", "content": "Hi, can you start my interview?"},
    {"role": "assistant", "content": "Sure! Let's begin. What inspired you to pursue data science?"},
    {"role": "user", "content": "I love analyzing data and finding insights that solve problems."},
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=conversation
)

print("🤖 Assistant reply:\n")
print(response.choices[0].message.content)
