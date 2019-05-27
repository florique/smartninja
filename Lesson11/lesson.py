import random
import json
import datetime

current_time = datetime.datetime.now()

print(current_time)

user = input("Please enter your name: ")

print("Hello" + user + "!")

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, user, date: " + score_dict.get("date"))

score_file.close()

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "user_name": user, "date": str(datetime.datetime.now())})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

