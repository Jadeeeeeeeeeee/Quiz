#Sequence 1 | Jade Ramos | 11/05/22 | V.1
#Ask the user what their name is and tell them about the program 

print("Welcome to Te Reo quiz, Please enter your name")

import time 
name = input("")

print("\n")
print("Kia ora, " + name + "!, Welcome to Te Reo quiz!, This program is designed to teach you some basic words in Te Reo Māori enjoy the quiz!")
print("\n")
time.sleep(2)
print("Also please use letters to answer aswell c:")

#Sequnce 2 | Jade Ramos | 11/05/22 | V.1
#Start the quiz and keep track of the users answer if they are right or wrong.
#Display the users score

time.sleep(3)
score = 0
print("\n")
question_1 = input("What is Kia ora in english? \na. Good moring \nb. Hello \nc.Welcome \nAnswer: ").lower()

if question_1 == "a" or question_1 == "Hello":
  score += 1
  print("You are correct!")
  print("Score:", score)
elif question_1 == "b" or question_1 == "Goodmorning" or question_1 == "c" or question_1 == "Welcome" :
  print("unfortunately you are wrong, the correct answer is a.Hello")
else:
  print("Please answer a letter")
  

