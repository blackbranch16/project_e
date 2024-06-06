# Movie Recommendation Tool

# Import random functions (ex. for choosing random questions)
import random
# Import json stuff
import json

# Declare choice global variable
choice = []

# HELPER FUNCTIONS 
def rand_num(start, finish):
  num = random.randrange(start, finish)
  return num

def create_code():
  # This is a random code that will determine which questions to ask the user
  code = []
  n = 0
  while n < 6:
    num = rand_num(1, 9)
    if num in code:
      rand_num(1, 9)
    else:
      code.append(num)
      n = n + 1
  return code

def ask_question(code):
  opinions = []
  n = 0
  while n < 8:
    current_q = questions[n]
    print('')
    print(current_q["intro"])
    print(current_q['q1'])
    print(current_q['q2'])
    print(current_q['q3'])
    print(current_q['q4'])
    choice = input("Enter Selection (1-4): ")
    opinions.append(choice)
    n += 1

# Create a Movie class
class Movie:
  # Define constructor method with parameters
  def __init__(self, user_mood, genre, occasion, age, pg, setting, rating):
    # Add properties to empty self object
    self.user_mood = user_mood
    self.genre = genre
    self.occasion = occasion
    self.age = age
    self.pg = pg
    self.setting = setting
    self.rating = rating

# Define some movies
stuart_little = Movie("Happy", "Comedy", "Family Movie Night", "Published 9 or more years ago", ) # NOT DONE
# MAIN PROGRAM LOOP
loop = True
while loop:
  # Load Questions from File
  file = open("questions.json")
  questions = json.load(file)
  file.close()
  # Print Main Menu
  print("\nMAIN MENU")
  print("1: Choose a movie")
  print("2: Suggest a movie")
  print("3: Add to favorites")
  print("4: Browse favorites")
  print("5: EXIT")
  # Get Menu Selection from User
  selection = input("Enter Selection (1-5): ")

  # Take Action Based on Menu Selection  
  if selection == "1":
    print("\nChoose a movie")
    code = create_code()
    print(code)
    ask_question(code)
  elif selection == "2":
    print("Suggest a movie")
  elif selection == "3":
    print("Add to favorites")
  elif selection == "4":
    print("Browse favorites")
  elif selection == "5":
    print("EXIT")
    loop = False