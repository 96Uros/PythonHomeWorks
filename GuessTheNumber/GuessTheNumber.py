import random
import time #dodal ker potrebujem za čakanje za izhod iz programa Stack
import sys #dodal ker potrebujem za izhod iz programa stack
import json
import datetime #vnosi datumov in ure vrstica 9
from termcolor import colored #knjizica za barve, google Stakckowerflow

#Dodajanje Časa;
currentTime = datetime.datetime.now()
#avtorske pravice:
print(colored("Created by: Uroš Kukovec", "light_red"))
#Izbira uporabniškega imena
username = input(colored("Enter your unserName: ", "black"))
#pozdrav igralca:
print(colored(f"hello {username}, please chose your difficulty;", "black"))

#Določanje naključnih števil
easy = random.randint(1,25)
normal = random.randint(1,766)
hard = random.randint(-3584,8692)

#tuakj odpremo json
with open("scorelist.json", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top score: " + str(score_list))

#START:
#določanje dif. lvla s katerim bom igral.
def selectDifficulty(): #uporabil dictionary z malo domišlije
    levelSelect = {
        "1": ("Easy", easy),
        "2": ("Normal", normal),
        "3": ("Hard", hard),
        "4": ("Exit", None) #NONE pomoč Stack.
    }

    for number, (difficulty, randomNumber) in levelSelect.items():
        print(f"{number}: {difficulty}")
#izbira pogoja
    chose = None
    while chose not in levelSelect:
        chose = input(colored("Enter number from 1-3 to select difficulty or 4 for exit: ", "cyan"))
#izhod iz programa v primeru uproabe št.4
        if chose == "4":
            print(colored("Bad to hear but you chose Exit.", "light_red"))
            print(colored("Goodbye!","light_red"))
            time.sleep(2)
            sys.exit()
            #izbiranje stopnje
        elif chose == "1":
            print(colored("You chose Easy difficulty", "green"))
            easyLevel()
            time.sleep(1)
            return
        elif chose == "2":
            print(colored("You chose Normal difficulty", "yellow"))
            time.sleep(1)
            normalLevel()
            return
        elif chose == "3":
            print(colored("You chose Hard difficulty", "red"))
            time.sleep(1)
            hardLevel()
            return
        else:
            number, difficulty = levelSelect[difficulty]
            print(colored(f"You choosed number {number} on difficulty -> {difficulty}"))
            return difficulty


def easyLevel():
    attempts = 0
    while True: 
        guess = int(input("Enter your guess (between 1 and 25): "))
        secret = easy
        attempts += 1

        if guess == secret:
            print("Congrats, you won!")
            print(f"{attempts} attempt/s needed.")
            #dodajanje v json datoteko
            score_list.append({"Attempts": attempts, "Time": currentTime.isoformat(), "Name": username, "SecretNumber": secret})

            with open("scorelist.json", "w") as score_file:
                score_file.write(json.dumps(score_list)) #dumps zapise v json

            break
        elif guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print("Try again...")


def normalLevel():
    attempts = 0
    while True: 
        guess = int(input("Enter your guess (between 1 and 766): "))
        secret = normal
        attempts += 1

        if guess == secret:
            print("Congrats, you won!")
            print(f"{attempts} attempt/s needed.")
            #dodajanje v json datoteko
            score_list.append({"Attempts": attempts, "Time": currentTime.isoformat(), "Name": username, "SecretNumber": secret})

            with open("scorelist.json", "w") as score_file:
                score_file.write(json.dumps(score_list)) #dumps zapise v json      
            break
        elif guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print("Try again...")


def hardLevel():
    attempts = 0
    while True: 
        guess = int(input("Enter your guess (between secret and +8000?): "))
        secret = hard
        attempts += 1

        if guess == secret:
            print("Congrats, you won that's crazy!")
            print(f"{attempts} attempt/s needed.")
            #dodajanje v json datoteko
            score_list.append({"Attempts": attempts, "Time": currentTime.isoformat(), "Name": username, "SecretNumber": secret})

            with open("scorelist.json", "w") as score_file:
                score_file.write(json.dumps(score_list)) #dumps zapise v json
            break
        elif guess > secret:
            print("Higher but think...!") #zamenjani so znaki za vecje manjse >.<
        elif guess < secret:
            print("Lower or Hiher?...")
        else:
            print("Try again...")

selectDifficulty()
