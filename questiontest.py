def question1():
  global score
  print("\033[4mQuestion 1:\033[0m")
  answer1 = input("What does Kia ora mean in english? \na. Good morning \nb. Hello \nc.Welcome \nAnswer: ").lower()

  if answer1 == "b":
    print("You are correct!")
    score += 1
    print("Score:", score)
    print("")
  elif answer1 == "a" or answer1 == "c":
    print("You are wrong, the correct answer is a.Hello")
    print("score:", score)
    print("")
  else:
    print("")
    print('\033[1m' + "Please asnwer a,b or c")
    question1()

print("")
score = 0
question1()