import random

print(" Select Diofficulty Level!")
print("1.Easy(1-50): ")
print("2.Medium(1-50): ")
print("3.Hard(1-200): ")

choice = input("Enter choice(1/2/3):")
if choice == "1":
    max_num = 50
    max_attempt = 10
elif choice == "2":
    max_num = 100
    max_attempt = 7
elif choice == "3":
    max_num = 200
    max_attempt = 5
else:
    print("Please Enter Valid Choice!")
    max_num = 100

Target = random.randint(1, max_num)
attempt = 0
print("Welcome to Guess the Number GAme!")
print("\n")
print(f"\nChosse Number between 1 to {max_num} !\n")
print("\n")

while attempt < max_attempt:
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
        print("Attempt: ", attempt)

        break
    elif userChoice < Target:
        print("Your guess is small ,guess again!")
    else:
        print("Your guess is greater please guess again!")

if attempt == max_attempt:
    print("used all attempts!")
    print("Torrect number was:", Target)


print("==================Game Over==================")
