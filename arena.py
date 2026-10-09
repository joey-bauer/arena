import random

# Hero Info
hero = {
    "name": "",
    "race": "",
    "level": 1,
    "health": 10,
    "speed": 3,
    "gold": 5,
    "exp": 0,
    "weapon": "wood sword"
}

# Enemy Info
enemies = [
    {
        "name": "Goblin",
        "health": 5,
        "damage": 1,
        "speed": 1,
        "gold_given": 3,
        "exp_given": 4,
        "defeated": False
    },

    {
        "name": "Warg",
        "health": 5,
        "damage": 3,
        "speed": 4,
        "gold_given": 4,
        "exp_given": 6,
        "defeated": False
    },

    {
        "name": "Beastmaster",
        "damage": 5,
        "speed": 2,
        "gold_given": 6,
        "exp_given": 8,
        "pet": {
            "health": 2,
            "damage": 2,
            "speed": 8
        },
        "defeated": False
    },

    {
        "name": "Shaman",
        "health": 8,
        "damage": 10,
        "speed": 7,
        "gold_given": 10,
        "exp_given": 15,
        "defeated": False
    },

    {
        "name": "Orc Chief",
        "health": 16,
        "damage": 8,
        "speed": 1,
        "gold_given": 8,
        "exp_given": 12,
        "defeated": False
    }
]

# Weapon Info
weapons = {
    "wood sword": {
        "name": "Wood Sword",
        "gold": 1,
        "damage": 1
    },

    "dagger": {
        "name": "Dagger",
        "gold": 3,
        "damage": 2
    },

    "steel sword": {
        "name": "Steel Sword",
        "gold": 5,
        "damage": 3
    },

    "battleaxe": {
        "name": "Battleaxe",
        "gold": 10,
        "damage": 5
    }
}

verbal_jousts = [
    "You're bad.",
    "You're mad.",
    "You're trash."
]

def main():
    battle()


def character_creation():
    hero["name"] = input("What is your name? ")
    hero["race"] = input("Are you a human, elf, or dwarf? ").strip().lower()

    while hero["race"] not in ["human", "elf", "dwarf"]:
        hero["race"] = input("Please choose human, elf, or dwarf.").strip().lower()

    if hero["race"] == "human":
        hero["gold"] += 5
    elif hero["race"] == "dwarf":
        hero["health"] += 1
    elif hero["race"] == "elf":
        hero["speed"] += 1

    print(
        f"Welcome, {hero["name"]}, to The Arena. Defeat enemies to escape.\n"
        "Visit the shop between matches to upgrade your gear."
    )

def armory():
    print("Welcome to The Armory! Gear up for your next battle.")
    while True:
        buy_or_sell = input("Are you looking to buy or sell? Or would you like to exit? ").strip().lower()

        while buy_or_sell not in ["buy", "sell", "exit"]:
            buy_or_sell = input("Please enter buy, sell, or exit ").strip().lower()

        if buy_or_sell == "buy":
            for weapon in weapons:
                print(f"{weapons[weapon]["name"]}: {weapons[weapon]["gold"]}\n")

            purchase = input("What weapon would you like to buy? ").strip().lower()

            if purchase in weapons:
                hero["weapon"] = purchase

        elif buy_or_sell == "sell":
            while True:
                sell_choice = input(f"Would you like to sell your {hero["weapon"]}? yes/no ").strip().lower()

                if sell_choice not in ["yes", "no"]:
                        input("Please enter yes or no. ")
                elif sell_choice == "yes":
                    hero["gold"] += weapons[hero["weapon"]]["gold"]
                else:
                    break

        elif buy_or_sell == "exit":
            return

def battle():
    print("You enter the arena.")

    for enemy in enemies:
        if enemy["defeated"] == True:
            continue
        elif enemy["defeated"] == False:
            print(f"You have encountered {enemy["name"]}.")

            while enemy["health"] > 0 or hero["health"] > 0:
                    action = input(f"Choose your next move: Attack / Verbal Joust ").strip().lower()

                    while action not in ["attack", "verbal joust"]:
                        action = input("Please choose Attack or Verbal Joust. ")

                    if action == "attack" and hero["speed"] >= enemy["speed"]:
                        print(f"{hero["name"]} attacks the {enemy["name"]}!")
                        enemy["health"] -= weapons[hero["weapon"]]["damage"]

                    elif action == "attack" and hero["speed"] < enemy["speed"]:
                        print(f"{enemy["name"]} attacks {hero["name"]}")
                        hero["health"] -= enemy["damage"]
                    elif action == "verbal joust" and hero["speed"] >= enemy["speed"]:
                        print(f"{hero["name"]} points at {enemy["name"]} and shouts, '{random.choice(verbal_jousts)}'")
                        enemy["speed"] -= 2

                    elif action == "attack" or action == "verbal joust" and enemy["speed"] > hero["speed"]:
                        print(f"{enemy["name"]} attacks!")
                        hero["health"] -= enemy["damage"]



main()