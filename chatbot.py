data={
    "Hey!":"Hey there! How's it going? What's up?",
    "Hello":"Hello there! How can I help you today?",
    "How are you?" :"I'm good,thanks for asking!Just ready to assist you",
    "What are you doing?":"I'm just a chatbot,but I'm here to assist you",
    "What are your hobbies?" :"I dont have any hobbies like you do,but I love chatting with you and learning about your interests!",
    "Do you like music?" :"Yeah!I think music is awesome!What kind of music do you like ?",
    "What is your favourite colour?" :"I'm a chatbot ,so I don't have any personal preferences for colours",
    "Okay Bye!" :"Goodbye! If you ever want to chat again or need anything ,just send me a message.Take care!",
}
def get_response(user_input):
    for pattern,response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry! I didn't understand that! .Can you please rephrase your sentence?"
print("Chatbot: Hi! I'm a simple chatbot, I'm here to assist you!")
while True:
    user_input=input("Me:")
    if user_input=='Bye':
        print("Chatbot:Goodbye! Have a great day!")
        break
    response=get_response(user_input)
    print("Chatbot:" , response)   