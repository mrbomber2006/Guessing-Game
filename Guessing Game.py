import random
from colorama import Fore, Style
import os

attempts = 5
challenger = input(Style.BRIGHT + "Challenger, enter your name: ")
questioner = input(Style.BRIGHT +
                   "Questioner, enter your name (if there is no questioner, insert 'bot'): ")

if questioner.lower() == "bot":
    the_number = random.randint(0, 99)
    print(Fore.CYAN + "bot is thinking ...")
else:
    while True:
        try:
            the_number = int(
                input(Fore.LIGHTCYAN_EX + f"{questioner}, enter the number (between 0 and 99): "))
            if 0 <= the_number <= 99:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print(Fore.RED +
                      "The number must be between 0 and 99. Please enter a valid number.")
        except ValueError:
            print(Fore.RED + "You must enter a number. Please try again.")

print(Fore.GREEN + "*" * 10)
while True:

    try:

        while attempts > 0:
            answer = int(input(Fore.LIGHTWHITE_EX +
                         f"{challenger}, guess the number: "))
            if answer == the_number:
                print(Fore.GREEN + "*" * 10)
                print(Fore.LIGHTGREEN_EX +
                      f"{challenger}, you guessed it right!")
                print(Fore.LIGHTMAGENTA_EX +
                      f"The number {questioner} entered was {the_number}.")
                print(Fore.GREEN + "*" * 10)
                break
            elif answer < the_number:
                print(Fore.LIGHTYELLOW_EX + "This number is smaller.")
                attempts -= 1
                print(Fore.LIGHTRED_EX + f"Number of attempts: {attempts}")
                print(Fore.GREEN + "*" * 10)
            elif answer >= 100 or answer < 0:
                print(
                    Fore.LIGHTRED_EX + "The number must be between 0 and 99. Please enter a valid number.")
                attempts -= 1
                print(Fore.LIGHTRED_EX + f"Number of attempts: {attempts}")

            elif answer > the_number:
                print(Fore.LIGHTYELLOW_EX + "This number is bigger.")
                attempts -= 1
                print(Fore.LIGHTRED_EX + f"Number of attempts: {attempts}")
                print(Fore.GREEN + "*" * 10)
    except ValueError:
        print(Fore.RED + "You must enter a number. Please try again.")
    else:
        break


if attempts == 0 and answer != the_number:
    print(Fore.LIGHTWHITE_EX + "{challenger}, you lose!")
    print(Fore.LIGHTMAGENTA_EX + f"The number was {the_number}.")
    print(Fore.GREEN + "*" * 10)
elif answer == the_number:
    print(Fore.LIGHTGREEN_EX + f"{challenger}, you guessed it right!")
    print(Fore.LIGHTMAGENTA_EX +
          f"The number {questioner} entered was {the_number}.")

print(Fore.LIGHTWHITE_EX + "Press the up arrow and enter to play again.")
print(Fore.GREEN + "*" * 10)
