import random, os

# number_to_guess = random.randint(1,20)
# print(number_to_guess)

# correct_guess = False
# counter = 1

# while not correct_guess:
#     user_guess = int(input("Guess the number: "))
#     if user_guess>number_to_guess:
#         print("You guees too High")
#     elif user_guess<number_to_guess:
#         print("You guees too Low")
#     else:
#         print(f"Correct! You got it in {counter} guesses")
#         correct_guess = True
#     counter += 1


# Where are you right now?
print(os.getcwd())          # Current working directory
# List files in current folder
print(os.listdir())         # Returns a list of filenames
# List files in a specific folder
print(os.listdir("/home/ksingh/python_learning"))
# Check if a file/folder exists
print(os.path.exists("hello.py"))    # True or False
# Join folder + filename safely (handles / correctly)
path = os.path.join("/home/ksingh", "python_learning", "hello.py")
print(path)