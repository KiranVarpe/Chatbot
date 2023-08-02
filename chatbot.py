print("ChatBot for  Question and Answering ")
print("=====================================")
print(" You may ask any one of these questions")
print("Hi")
print("How are you?")
print("Are you working?")
print("What is your name?")
print("what did you do yesterday?")
print("Quit")
while True:
 question = input("\n\nEnter one question from above list:")
 question = question.lower()
 if question in ['hi']:
     print("Hello Kiran ")
 elif question in ['how are you?','how do you do?']:
     print("I am Good Kiran . \nWhat about you ?")
     input(":")
     print("Ohh Nice")
 elif question in ['are you working?','are you doing any job?']:
     print(" I don't have a job like a human does. I exist solely to provide information and answer "
           "\nquestions to the best of my ability. My purpose is to assist and help users in various tasks, "
           "\nsuch as providing recommendations, generating text, and answering questions.")
 elif question in ['what is your name?']:
     print("My name is ChatBot")
     name=input("what is your name ?")
     print("Nice name and Nice meeting you",name)
 elif question in ['what did you do yesterday?']:
     print("Yesterday I didn't do anything yesterday as "
           "\nI don't have a physical presence and I am running 24/7 to assist users like you.")
 elif question in ['quit']:
         break
 else:
     print("I don't understand what you said")