import random

winners = 0
comp_Win = 0

options =["Players 1", "Players 2","Players 3"]

while True:
    users = input("Choose Players 1/ Players 2/ Players 3 or type Q to quit: ").lower()

    if users == "q":
        break

    if users not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]

    print("computer picked", computer_pick + ".")

    if users == "Players 1" and computer_pick == "football":
        print("Winner Players 1")
        winners += 1

    elif users == "Players 2" and computer_pick == "voleyball":
        print("Winner Players 2")
        winners += 1

    elif users == "Players 3" and computer_pick == "basketball":
        print("Winner Players 3")
        winners += 1

    else:
        print("you lost")
        comp_Win +=1

print ("Player win", winners, "times. ")
print("Computer win", comp_Win, "times. ")

input("Press enter to exit")
