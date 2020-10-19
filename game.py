import random

relations = {'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
             'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
             'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
             'devil': ['human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning'],
             'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
             'water': ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
             'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
             'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
             'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
             'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
             'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
             'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
             'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
             'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
             'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors']}
default_options = ['rock', 'paper', 'scissors']
score = 0

rating_file = open('rating.txt', 'r+')
user_name = input("Enter your name: ")
print(f"Hello, {user_name}")

chosen_options = input("Enter the game's options: ").split(',')
if chosen_options == ['']:
    chosen_options = default_options
print("Okay, let's start")

for line in rating_file.readlines():
    playerstats = line.split()
    player_name = playerstats[0]
    if player_name == user_name:
        score = int(playerstats[1])

while 1:
    choice = input()
    cmove = random.choice(chosen_options)
    if choice == '!exit':
        print("Bye!")
        break
    elif choice == '!rating':
        print(f"Your rating: {score}")
    elif choice not in chosen_options:
        print("Invalid input")
    elif cmove in relations[choice]:
        print(f"Well done. The computer chose {cmove} and failed")
        score += 100
    elif choice == cmove:
        print(f"There is a draw ({cmove})")
        score += 50
    else:
        print(f"Sorry, but the computer chose {cmove}")

rating_file.close()
