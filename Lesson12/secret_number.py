import datetime
import json
import random

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

print("Top scores: " + str(score_list))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

def play_game():
    attempts = 0
    secret = random.randint(1, 30)

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1
        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

while True:
    selection = int(input("Would you like to A) Play another game, B) See the best scores or C) quit?"))

    if selection == "A":
        play_game()
    #elif selection == "B":
        #for score_dict in get_top_scores():
            #print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break

#def getscorelist()