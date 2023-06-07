import random
def play_again_menu():
    print("-------------------------End game-------------------------", end="\n")
    print("Do you want to play again?", end="\n")
    print("1 - Yes")
    print("2 - No")

name_by_level = {
    1: 'Easy',
    2: 'Medium',
    3: 'Hard',
    4: 'Breaking the game'
}

attempts_by_level = {
    1: 7,
    2: 5,
    3: 3,
    4: 3
}

secret_number_by_level = {
    1: 25,
    2: 30,
    3: 50,
    4: 50
}

exit_game = 1
while (exit_game == 1):
    print("-----------------Welcome to Guessing Game-----------------")
    print("How to play?", end="\n", )
    print("> You have to discover the secret number. For this you will have a limited amount of attempts.", end="\n")
    print("> The number of attempts will vary according to the selected level.", end="\n")
    print("> Difficulty levels:", end="\n")
    print(" 1 - Easy - 28% chance to discover: Secret number is between 1 ~ 25; You will have 7 attempts; Tips every attempt; Gold tip at the last "
          "attempt.",
          end="\n")
    print(" 2 - Medium - 16,66% chance to discover: Secret number is between 1 ~ 30; You will have 5 attempts; Tips every attempt; Gold tip at the "
          "last attempt.",
          end="\n")
    print(" 3 - Hard - 10% chance to discover: Secret number is between 1 ~ 50; You will have 5 attempts; Tips every attempt.", end="\n")
    print(" 4 - Breaking the game - 6% chance to discover: Secret number is between 1 ~ 50; You will have 3 attempts; No tips.", end="\n")
    print("----------------------------------------------------------", end="\n")
    try:
        game_level = int(input("Enter with the level difficulty level: "))

        if game_level in name_by_level:
            level = name_by_level.get(game_level)
            max_attempts = attempts_by_level.get(game_level)
            secret_number = random.randint(1, secret_number_by_level.get(game_level))
            print("Difficulty level selected: ", level, end="\n")
            print("Attempts: ", max_attempts, end="\n")
            print("Secret number is between: 1 to", secret_number_by_level.get(game_level), end="\n")
            if game_level == 1 or game_level == 2:
                gold_tip = True
                if secret_number <= 5:
                    min_secret_number = 1
                    max_secret_number = secret_number + 5
                elif secret_number >= (secret_number_by_level.get(game_level) - 5):
                    min_secret_number = secret_number - 5
                    max_secret_number = secret_number_by_level.get(game_level)
                else:
                    min_secret_number = secret_number - 5
                    max_secret_number = secret_number + 5
                print("Gold tip: Enable")
            else:
                gold_tip = False
                print("Gold tip: Disable")
        print("------------------------------------ ----------------------", end="\n")
    except ValueError:
        print("Invalid input. Please enter an integer.")

    attempt = 0
    while (attempt < max_attempts):
        print("You have:", (max_attempts - attempt), "attempts")
        try:
            input_number = int(input("Enter a number: "))
            print("----------------------------------------------------------")
            attempt += 1
            difference = input_number - secret_number
            if input_number == secret_number:
                print("Congratulations!!!")
                print("You discover the number", secret_number, "in", attempt, "attempts")

                play_again_menu()
                try:
                    exit_game = int(input())
                    if exit_game != 1:
                        print("Exit game...")
                    attempt = max_attempts
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    print("Exit game...")
                    attempt = max_attempts
            elif attempt == max_attempts and input_number != secret_number:
                print("Game over!!!")
                print("You have no more attempts.")
                print("The correct number is:", secret_number)

                play_again_menu()
                try:
                    exit_game = int(input())
                    if exit_game != 1:
                        print("Exit game...")
                    attempt = max_attempts
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    print("Exit game...")
                    attempt = max_attempts
            elif (max_attempts - attempt) == 1 and gold_tip == True:
                print("The number it's incorret :(")
                print("Gold tip: The number is between", min_secret_number, "to", max_secret_number, end="\n")
            else:
                print("The number it's incorret :(")
                if (difference >= 1 and difference <= 3) or (difference <= -1 and difference >= -3) and level != "Breaking the game":
                   print("Tip: You are close to discovering the number!")
                else:
                    print("Tip: You aren't close to discovering the number!")
            print("----------------------------------------------------------")

        except ValueError:
            print("Invalid input. Please enter an integer.")
            print("----------------------------------------------------------", end="\n")