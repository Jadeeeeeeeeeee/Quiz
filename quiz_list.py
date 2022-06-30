#Base quiz learning code

#importing the random libary
import random
#globals and questions lists
score = 0
name = input("")
#global and quesitons lists
question_name = ["Question 1: ", "Question 2: ", "Question 3: ", "Question 4: ", "Question 5: "]
english = ["hello", "welcome", "goodmorning", "egg", "dog", ]
right_answer = ["Kia ora", "Nau mai, haere mai mean", "mōrena", "hēki", "pero"]
option_1 = ["Wrong Answer" , "Wrong Answer" , "Wrong Answer", "Wrong asnwer", "Wrong asnwer"]
option_2 = ["Wrong Answer" , "Wrong Answer" , "Wrong Answer", "Wrong asnwer", "Wrong asnwer"]
#Define a fuction to greet the user
def greeting():
  greet = input("Please enter your name :")

  if greet == "":
    print("Kia ora", name , "welcome to Te Reo quiz!,this program is a quiz about teaching you māori words.The quiz is a multiple choice quiz so please pick one of the choices.Have fun and enjoy the quiz!")
#define a function to generate a question
def generate_question(question_name, english, right_answer, option_1, option_2):
  global score
  print("What is", english , "in english?" )
  random_sequence = random.randint(0,2)
#seperate print statements for readability
  if (random_sequence == 0):
    print("A", option_1)
    print("B", option_2)
    print("C", right_answer)
    answer = input().lower()
    if answer == "c":
      score += 1
    else:
      print("incorrect.")

  elif (random_sequence == 1):
    print("A", option_1)
    print("B", right_answer)
    print("C", option_2)
    answer = input().lower()
    if answer == "b":
      score += 1
    else:
      print("incorrect.")

  elif (random_sequence == 2):
    print("A", right_answer)
    print("B", option_2)
    print("C", option_2)
    answer = input().lower()
    if answer == "a":
      score += 1
      
    else:
      print("incorrect.")

for i in range (0, 5):
  generate_question(question_name[i],english[i],right_answer[i],option_1[i],option_2[i])

print (score)