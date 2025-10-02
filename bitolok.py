import random
choice = input("This is number game .Do you wish to continue (y/n):")
if choice == "y":
 print("Welcome to guessing game")
 name = input("What is your name: ")
elif choice == "n":
 print(f"Goodbye ")
 exit()
secret_number = random.randint(1,10)
attempts = 0 
guess = None
while guess != secret_number:
    try:
       guess = int(input(f"{name},Enter secret number between 1 and 20:"))
       if guess < secret_number:
          print(f"{guess} too low, try again")
       elif guess > secret_number:
          print(f"{guess} too high,try again")
       else:
          print(f"Bravo {name},{guess} is the secret_number")

    except ValueError:
      print("Kindly follow number protocal")

    



