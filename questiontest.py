#Functions | Jade Ramos | 21/06/22 | V.7
import sys, json
import time
from time import sleep
from simple_colors import *
#Functions goes here
#This functions makes it possible to write the words meaning that letters will pop up 1 by 1 when used the function write instead of print
def instructions():
  instructions = input("Would you like to see the insrutions? ").lower()

  if instructions == "yes":
    write("This quiz is a multiple choice quiz,you are given 3 choices which you to pick from.You get a point for every correct asnwer and the game will check on how you did based on this score \n \n")
    question1()

  else:
    print("")
    question1()
def write(words):
  for char in words:
    sleep(0.03)
    sys.stdout.write(char)
    sys.stdout.flush()

#Questions | Jade Ramos | 21/06/22 | V.7
#The questions 
def question1():
  global score
  print("\033[4mQuestion 1:\033[0m")
  answer1 = input("What does Kia ora mean in english? \na. Good morning \nb. Hello \nc.Welcome \nAnswer: ").lower()

  if answer1 == "b":
    print("You are correct!")
    score += 1
    print("Score:", score)
    print("")
    question2()
  elif answer1 == "a" or answer1 == "c":
    print("You are wrong, the correct answer is a.Hello")
    print("score:", score)
    print("")
    question2()
  else:
    print("\n", '\033[1m' + "Please asnwer a,b or c")
    question1()
#Question2
def question2():
  print("\033[4mQuestion 2:\033[0m")
  global score
  answer2 = input("What is does Nau mai, haere mai mean in english? \na. Goodbye \nb. Welcome \nc. Take care \nAnswer :").lower()

  if answer2 == "b":
    print("You are correct!")
    score += 1
    print("Score:", score)
    print("")
    question3()
  elif answer2 == "a" or answer2 == "c":
    print("You are wrong, the correct answer is b.Welcome")
    print("Score:", score)
    print("")
    question3()
  else:
    print("")
    print('\033[1m' + "Please asnwer a,b or c")
    question2()
#Question3
def question3():
  print("\033[4mQuestion 3:\033[0m")
  global score
  answer3 = input("What is mōrena in english \na. Good morning \nb. Good afternoon \nc. Good evening \nAnswer :").lower()

  if answer3 == "a":
    print("You are correct!")
    score += 1
    print("Score:", score)
    print("")
    question4()
  elif answer3 == "b" or answer3 == "c":
    print("You are wrong, the correct answer is a.Good morning")
    print("Score:", score)
    print("")
    question4()
  else:
    print("")
    print('\033[1m' + "Please asnwer a,b or c")
    question3()
#Question4
def question4():
  print("\033[4mQuestion 4:\033[0m")
  global score
  answer4 = input("What is hēki in english? \na.bread \nb.bacon \nc.egg \nAnswer :").lower()

  if answer4 == "c":
    print("You are correct!")
    score += 1
    print("Score:", score)
    print("")
    question5()
  elif answer4 == "a" or answer4 == "b":
    print("You are wrong, the answer is c.egg")
    print("Score:", score)
    print("")
    question5()
  else:
    print("")
    print('\033[1m' + "Please asnwer a,b or c")
    question4()
#Question5
def question5():
  print("\033[4mQuestion 5:\033[0m")
  global score
  answer5 = input("What is pero in english? \na.cat \nb.bird \nc.dog \nAnswer :").lower()

  if answer5 == "c":
    print("You are correct!")
    score += 1
    print("Score:", score)
    print("")
    question6()
  elif answer5 == "a" or answer5 == "b":
    print("You are wrong, the correct answer is c.dog")
    print("Score:", score)
    print("")
    question6()
  else:
    print("")
    print('\033[1m' + "Please asnwer a,b or c")
    question5()
#Question6
def question6():
  print("\033[4mQuestion 6:\033[0m")
  global score
  answer6 = input("What is egg in Te Reo Māori? \na.ngeru  \nb.koe  \nc.hēki  \nAnswer :").lower()

  if answer6 == "c":
    print("You are correct!")
    score += 1
    print("Score:", score)
    print("")
    question7()
  elif answer6 == "a" or answer6 == "b":
    print("You are wrong, the correct answer is c.hēki ")
    print("Score:", score)
    print("")
    question7()
  else:
    print("")
    print('\033[1m' + "Please asnwer a,b or c")
    question6()
#Question7
def question7():
  print("\033[4mQuestion 7:\033[0m")
  global score
  answer7 = input("What is Good morning in Te Reo Māori? \na.tēnā koe i tēnei ahiahi  \nb.mōrena  \nc.pō mārie  \nAnswer :").lower()

  if answer7 == "b":
    print("You are correct!")
    score += 1
    print("Score:", score)
    print("")
    question8()
  elif answer7 == "a" or answer7 == "c":
    print("You are wrong, the correct answer is b.mōrena")
    print("Score:", score)
    print("")
    question8()
  else:
    print("")
    print('\033[1m' + "Please asnwer a,b or c")
    question7()
#Question8
def question8():
  print("\033[4mQuestion 8:\033[0m")
  global score
  answer8 = input("What is Hello in Te Reo Māori? \na.Kia ora \nb.Nau mai  \nc.mōrena  \nAnswer :").lower()

  if answer8 == "a":
    print("You are correct!")
    score += 1
    print("Score:", score)
    print("")
    question9()
  elif answer8 == "b" or answer8 == "c":
    print("You are wrong, the correct answer is a.Kia ora")
    print("Score:", score)
    print("")
    question9()
  else:
    print("")
    print('\033[1m' + "Please asnwer a,b or c")
    question8()
#Question9
def question9():
  print("\033[4mQuestion 9:\033[0m")
  global score
  answer9 = input("What is Welcome in Te Reo Māori? \na.Kia ora \nb.Nau mai, haere mai  \nc.mōrena  \nAnswer :").lower()

  if answer9 == "b":
    print("You are correct!")
    score += 1
    print("Score:", score)
    print("")
    question10()
  elif answer9 == "a" or answer9 == "c":
    print("You are wrong, the correct answer is c.aroha")
    print("Score:", score)
    print("")
    question10()
  else:
    print("")
    print('\033[1m' + "Please asnwer a,b or c")
    question9()   
#Question10
def question10():
  print("\033[4mQuestion 10:\033[0m")
  global score
  answer10 =  input("What is egg in Te Reo Māori? \na.ngeru  \nb.koe  \nc.hēki  \nAnswer :").lower()

  if answer10 == "c":
    print("You are correct!")
    score += 1
    print("Score:", score)
  elif answer10 == "a" or answer10 == "b":
    print("You are wrong, the correct answer is c.hēki")
    print("Score:", score)
  else:
    print("")
    print('\033[1m' + "Please asnwer a,b or c")
    question10()   

#This function tells the user about their total score and how they did based on it
def totalscore():
  global score 
  
  if score <= 4:
    print("Your total score is:",score , "You did pretty bad,please try again")
  elif score <= 9:
    print("Your total score is:",score ,"You did great,please try again if you want to get a perfect score")
  else:
    print("Your total score is:",score ,"Congratulations you got all the questions correct!")
    
#Greeting | Jade Ramos | 21/06/22 | V.7
#Ask the user what their name is and tell them about the program 
#after the user puts their name in start the quiz
write("Welcome to Te Reo quiz, Please enter your name:")
name = input("")
print("")
write("Kia ora!, " + name + "!, Welcome to Te Reo quiz!, This quiz is a multiple choice quiz so please pick one of the letter choices.Have fun and enjoy the quiz!")
print("\n")
#The quiz
score = 0
time.sleep(0.5)
instructions()
print("")
totalscore()