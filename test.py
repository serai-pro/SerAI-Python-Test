#This is a test made with the SerAI Package

import SerAI  
SerAI.setup("demo") # Demo API.

#this is for images only:
response_image = SerAI.image("dog")
print(response_image) 

#This is to get Website informations:
website_get = SerAI.website("serai.pro")
print(website_get) 

#this is for chatting with the AI:
while True:
    user_input = input("You: ") #Your message 
    if user_input.lower() == "exit": #to exit the loop
        break  
    
    ai_response = SerAI.message(user_input) #the ressponse
    
    print("AI:", ai_response) #outputting the response
