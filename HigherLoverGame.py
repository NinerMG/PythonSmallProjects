import random

data = [
    {"name": "Cristiano Ronaldo", "followers": 600},
    {"name": "Lionel Messi", "followers": 500},
    {"name": "Kylie Jenner", "followers": 400},
    {"name": "Dwayne Johnson", "followers": 350},
    {"name": "Ariana Grande", "followers": 300},
    {"name": "Selena Gomez", "followers": 320}
]

def get_random_choice():
    return random.sample(data, 2)

def play_round():
    obj1, obj2 = get_random_choice()

    print(f"A: {obj1['name']}")
    print(f"B: {obj2['name']}")
    choice = input("Which one is more popular A or B?").upper()

    if (choice == "A" and obj1['followers'] > obj2['followers']) or \
        (choice == "B" and obj2['followers'] > obj1['followers']):
        print("Correct! You guessed right!")
    else:
        print("Wrong! Better luck next time")
    print(f"A: {obj1['name']} - {obj1['followers']}")
    print(f"B: {obj2['name']} - {obj2['followers']}")