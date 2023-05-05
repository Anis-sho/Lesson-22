import random
# 1 - 1000

top_of_range = input("Type a number: ")

#Validation
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <=0:
        print("Please enter a lage number!")
        quit()
else:
    print("Please enter a number next time!")
    quit()
    
random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess? ")
    
    #Validation
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter number only")
        continue
    
    if user_guess == random_number:
        print("You guessed the correct number!")
        break
    elif user_guess > random_number:
        print("You gessed a biger number, please select lower nomber!")
    else:
        print("You gessed a smaller number, please select biger nomber!")

print("You found the random number after", guesses, "guesses")