from art import  logo,vs
from game_data import data
from random import choice
import json
import os

def random_pick():
    person = choice(data)
    return person

def compare():
    if first_option.get('follower_count') > second_option.get('follower_count'):
        return 'A'
    else:
        return 'B'

def main():
    play_game = True
    score = 0
    global first_option
    global second_option
    first_option = random_pick()
    second_option = random_pick()

    while first_option == second_option:
        second_option = random_pick()
    
    print(logo)
    print(f"Compare A: {first_option.get('name')}, a {first_option.get('description')}, from {first_option.get('country')}.{first_option.get('follower_count')}")
    print(vs)
    print(f"Compare B: {second_option.get('name')}, a {second_option.get('description')}, from {second_option.get('country')}.{second_option.get('follower_count')}")
    user_choice = input("Who has more followers? Type 'A' or 'B':").upper()
    if user_choice == compare():
        score += 1  
    else:
        play_game = False
        os.system('cls')

    while play_game != False:
        first_option = second_option
        second_option = random_pick()
        while first_option == second_option:
            second_option = random_pick()
        print(logo)
        print(f"You're right! Current score: {score}") 
        print(f"Compare A: {first_option.get('name')}, a {first_option.get('description')}, from {first_option.get('country')}.{first_option.get('follower_count')}")
        print(vs)
        print(f"Compare B: {second_option.get('name')}, a {second_option.get('description')}, from {second_option.get('country')}.{second_option.get('follower_count')}")
        user_choice = input("Who has more followers? Type 'A' or 'B':").upper()
        if user_choice == compare():
            score += 1   
        else:
            play_game = False
            os.system('cls')

    f = open("high_record.txt", "r")
    if score > int(f.read()):
        f = open("high_record.txt", "w")
        high_score = json.dumps(score)
        f.write(high_score)
        f.close()

    print(logo)
    print(f"Sorry, that's wrong. final score: {score}")

if __name__ == "__main__":
    main()