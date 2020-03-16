import random
random_number = random.randint(0, 10)

x = 10
for i in range(x):
    user_guess = int(input("Your guess:\n"))
    if user_guess == random_number:
        print("Correct number!")
        break
    elif user_guess < random_number:
        print("The random number is bigger.")
    else:
        print("The random number is smaller.")

