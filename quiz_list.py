#imports
import sys, json
import time
from time import sleep
#Define a fuction to write words
def write(words):
  for char in words:
    sleep(0.03)
    sys.stdout.write(char)
    sys.stdout.flush()

#Instructions and greeting
write("Welcome to Te Reo quiz, Please enter your name:")
name = input("")
print("")
write("Kia ora!, " + name + "!, Welcome to Te Reo quiz!, This quiz is a multiple choice quiz so please pick one of the letter choices.Have fun and enjoy the quiz!\n")
time.sleep(0.5)
#import random library
import random  

#globals and questions lists
score = 0
#global and quesitons lists
english = ["hello", "welcome", "goodmorning", "egg", "dog", "cat", "love","lake","sea","family" ]
right_answer = ["Kia ora", "Nau mai, haere mai mean", "mōrena", "hēki", "pero","ngeru", "aroha", "awa","moana","whanau"]
option_1 = ["pero" , "aroha" , "kai ", "ngeru", "koe","aroha","pō mārie","tāne","taonga","awa"]
option_2 = ["Nau mai, haere hai" , "mōrena" , "hēki", "Nau mai", "ngeru","awa","tama","tamāhine","motu"]

#define a function to generate a question
def generate_question(english, right_answer, option_1, option_2):
  global score
  time.sleep(0.5)
  print("\nWhat is the maori word for", english)
  random_sequence = random.randint(0,2)
#seperate print statements for readability
  if (random_sequence == 0):
    print("A.", option_1)
    print("B.", option_2)
    print("C.", right_answer ,"\nAnswer:")
    answer = input().lower()
    if answer == "c":
      score += 1
      print("Correct!")
      print("Score:", score)
    else:
      print("Score:", score)
      print("Incorrect")

  elif (random_sequence == 1):
    print("A.", option_1)
    print("B.", right_answer)
    print("C.", option_2 ,"\nAnswer:")
    answer = input().lower()
    if answer == "b":
      print("Correct!")
      score += 1
      print("Score:", score)
    else:
      print("Score:", score)
      print("incorrect.")

  elif (random_sequence == 2):
    print("A.", right_answer)
    print("B.", option_2)
    print("C.", option_1 ,"\nAnswer:")
    answer = input().lower()
    if answer == "a":
      print("Correct!")
      score += 1
      print("Score:", score)
    else:
      print("incorrect.")
      print("Score:", score)

for i in range (0, 10):
  generate_question(english[i],right_answer[i],option_1[i],option_2[i])

def total_score():
  if score <= 4:
    print("Your total score is:",score , "You did pretty bad,please try again")
  elif score <= 9:
    print("Your total score is:",score ,"You did great,please try again if you want to get a perfect score")
  else:
    print("Your total score is:",score ,"Congratulations you got all the questions correct!")


total_score()