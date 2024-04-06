import anthropic
import os

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=os.environ.get("CLAUDE_API"),
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Is it late to get a job at 19 if you never had any prior job? I am a fulltime student studying Engineering, and my parents have asked me to move out; however, I do not have any money saved up, but I am optimistic to find a job and embark on a new phase of life."}
    ]
)
print(message.content[0].text)
