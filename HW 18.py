print("Welcome to our restaurant! ")

playing = input("Would you want menu? ")

if playing.lower() != "yes":
    quit()
    
print("Let's order?")
price = 0

answer = input("Do you want our signature dishes? ")
if answer == "yes":
    print("Now i told you 😃")
    price1 = price + 0
else:end(answer)
    
    
answer = input("For first dishes We have soup with shep met. Woud you like it? ")
if answer == "no":
    print("Then choos another dishes 😃")
    price2 = price + 0
else:
    print ("Then another dishes 🙂")
    
    
answer = input("We have veary delicios Farel for second dish.You want it? ")
if answer == "yes":
    print("OK. 😃")
    price3 = price + 50
else:
    print ("Then another dishes 🙂")
    

answer = input("And we have salad with vegetables. Would you want it? ")
if answer == "yes":
    print("Exelent 😃")
    price4 = price + 25
else:
    print ("Good 🙂")
    
answer = input("We have salad with froots. ")
if answer == "yes":
    print("OK 😃")
    price5 = price + 30
else:
    print ("Then someting else 🙂")
    
    
answer = input("We have some drinks. Would you lik to drink? ")
if answer == "yes":
    print("OK 😃")
    price6 = price + 0
else:
    print ("I dont want drienk 🙂")
    
    
answer = input("Brink to yo a shampain? ")
if answer == "yes":
    print("OK 😃")
    price7 = price + 45
else:
    print ("Something ese 🙂")
    
answer = input("In te end mayby you want disert? ")
if answer == "yes":
    print("OK Thank a lot. 😃")
    price8 = price + 15
else:
    print ("It's ol 🙂")
    
print("You choused " + str(score) + " dishes.")
print("You chousing percentege is " + str((score/3)*100))   

print("You price is " + str(price) + str(price1) + str(price2) + str(price3) + str(price4) + str(price5) + str(price6) + str(price7) + str(price8))   



input("press enter to exit")