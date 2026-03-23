import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from google import genai

f = ""
if os.path.isfile("APIKEY/APIKEY.txt"):
    f = open("APIKEY/APIKEY.txt")
elif os.path.isfile("../APIKEY/APIKEY.txt"):
    f = open("../APIKEY/APIKEY.txt")
else:
    Tk.withdraw()
    filename = askopenfilename()
    f = open(filename)
apikey = f.read()

client = genai.Client(api_key=apikey)
loop = True
name = input("What is the name you want the AI to call you?: ")
conversation = "Me: Talk to me as if we were friends, call me " + name
print("Write 0 to exit conversation or write normally to continue")

while(loop):
    userPhrase = input("Me: ")
    conversation += "\nMe: " + userPhrase
    if (userPhrase == "0"):
        loop = False
        continue
    else:
        AIResponse = client.models.generate_content(model= "gemini-2.5-flash-lite", contents=conversation)
        conversation += "\nYou: " + AIResponse.text
        print(f"AI: {AIResponse.text}")