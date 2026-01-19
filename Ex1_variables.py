# -------------------------------------------
# Exercise 1: Variables
# -------------------------------------------
# This exercise introduces you to the concept of Variables. 
# Think of a variable as a labeled box that stores information
# so you can reuse it later without typing it out every time!
#
# Key Concepts to practise:
# - Storing data in variables
# - Using f-strings (formatted strings)
# - Doing simple math with variables
# - Using Git to save your work to a "Remote Repository"
# -------------------------------------------
# INDIVIDUAL INSTRUCTIONS
# -------------------------------------------
# Work independently. If you get stuck, look at the EXAMPLES provided.
# Part of being a developer is "searching" for answers—feel free to 
# look up what GitHub, GitLab, and Bitbucket are as you work!
# -------------------------------------------


# -------------------------------------------
# Task 1: Introduction to Variables
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Introduction to Variables\n"
    + "-------------------------------------------")

# CONCEPT: Instead of "hard-coding" a name like "Alice" everywhere,
# we use a variable. If we change the variable once, the whole 
# program updates automatically!

# TODO:
# 1. Create a variable called 'name' and set it to "Alice".
# 2. Create a variable called 'age' and set it to 25.
# 3. Create a variable called 'food' and set it to "pizza".
# 4. Use an f-string to print: "Hello, Alice!"
#
# EXAMPLE:
# colour = "Red"
# print(f"My favourite colour is {colour}")

# Write your code below:


# -------------------------------------------
# Task 2: Using Variables in Sentences
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 2: Using Variables in Sentences\n"
    + "-------------------------------------------")

# CONCEPT: We can use f-strings to build complex sentences and even
# do math inside the curly braces { }.

# TODO:
# 1. Print: "Alice is 25 years old." (Use your variables!)
# 2. Print: "In 5 years, Alice will be 30." (Calculate 25 + 5 inside the f-string).
# 3. Print: "Alice really likes pizza."
#
# EXAMPLE:
# score = 10
# print(f"Your double score is {score * 2}")

# Write your code below:


# -------------------------------------------
# Task 3: The Power of Refactoring
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Task 3: The Power of Refactoring\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a second set of variables for a person named "Bob".
# 2. Give Bob an age and a different favourite food.
# 3. Print the same 4 sentences as above, but for Bob.

# Write your code below:


# -------------------------------------------
# CHECKPOINT: WHAT IS GIT?
# -------------------------------------------
# You are about to use "Source Control", specifically a tool called GIT.
# This saves your work to platforms like GitHub, GitLab, or Bitbucket.
#
# - git add: Picks which files you want to save.
# - git commit: Takes a "snapshot" of the code with a message.
# - git push: Sends that snapshot to the cloud (GitHub/GitLab/Bitbucket).
#
# RUN THESE IN THE TERMINAL:
# 1. git add Ex1_variables.py
# 2. git commit -m "Completed tasks 1 to 3"
# 3. git push origin main
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: The Input Function
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 1: The Input Function\n"
    + "-------------------------------------------")

# TODO: Use the input() function to ask the user for their OWN name
# and store it in a variable. Print a welcome message for them.
#
# EXAMPLE:
# city = input("Which city do you live in? ")
# print(f"{city} sounds like a lovely place!")

# Write your code below:


# Extension 2: Integer Conversion
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: Integer Conversion\n"
    + "-------------------------------------------")

# TODO: When you use input(), Python thinks the answer is text. 
# Use int() to turn a user's age into a number so you can add 1 to it.
# Ask the user for their age and tell them how old they will be next year.

# Write your code below:


# Extension 3: Case Formatting
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 3: Case Formatting\n"
    + "-------------------------------------------")

# TODO: Take the 'food' variable from Task 1. 
# Use .upper() to print the food in all capital letters.
#
# EXAMPLE:
# name = "alice"
# print(name.capitalize())

# Write your code below:


# -------------------------------------------
# SAVE YOUR PROGRESS
# -------------------------------------------
# 1. git add Ex1_variables.py
# 2. git commit -m "Completed extensions"
# 3. git push origin main
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: The Mini Bio-Generator
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: The Mini Bio-Generator\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for 4 different pieces of information about themselves.
# 2. Store them all in variables.
# 3. Print out a neat "Profile Card" using multiple f-strings.
# 4. Use an IF statement to check if their age is over 18.
#    If it is, print "Account type: Adult". 
#    Otherwise, print "Account type: Junior".

# Write your code below:


# -------------------------------------------
# FINAL SUBMISSION
# -------------------------------------------
# Well done! You have successfully used variables and saved your 
# work to a remote server. This is exactly how professional 
# developers manage their programs.
#
# 1. git add Ex1_variables.py
# 2. git commit -m "Final submission - All tasks complete"
# 3. git push origin main
# -------------------------------------------
