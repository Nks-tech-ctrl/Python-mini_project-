import random

Target = random.randint(1, 100)
attempt = 0
print("Welcome to Guess the Number GAme!")
print("\n")
print("Chosse Number between 1 to 100 !")
print("\n")

while True:
    userChoice = input("Enter your Target number or Quit(Q): ")

    if userChoice == "Q":
        break

    try:
        userChoice = int(userChoice)
        attempt += 1
    except ValueError:
        print("please enter valid guess!")
        continue

    if userChoice == Target:
        print("Success: Correct Guess")

        break
    elif userChoice < Target:
        print("Your guess is small ,guess again!")
    else:
        print("Your guess is greater please guess again!")


print("==================Game Over==================")
