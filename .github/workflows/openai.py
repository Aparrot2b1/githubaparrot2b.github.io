
import openai

# should be replaced by your API keyopenai.api_key = "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"

# if nothing is typed, this content will be sentmessages = [    {"role": "system", "content": "What can you do as an AI."},]

while True:    
message = input("User : ")    
if message:        
messages.append(            
{"role": "user", "content": message},        )        
chat = openai.ChatCompletion.create(            
model="gpt-3.5-turbo", messages=messages        )    
reply = chat.choices[0].message.content    
print(f"ChatGPT: {reply}")    
messages.append({"role": "assistant", "content": reply})
