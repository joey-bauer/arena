import random

# Hero Info
hero = {
    "name": "",
    "race": "",
    "level": 1,
    "health": 10,
    "max health": 30,
    "speed": 15,
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
        "health": 8,
        "damage": 5,
        "speed": 2,
        "gold_given": 6,
        "exp_given": 8,
        "pet": {
            "name": "Hawk",
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
        "damage": 5
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
    character_creation()

    while True:
        armory()
        if all(enemy["defeated"] for enemy in enemies):
            break

    print(f"{hero["name"]} has conquered the arena.")
            
    


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
        "Visit the armory between matches to upgrade your gear."
    )

def armory():
    print("Welcome to The Armory! Gear up for your next battle.")
    while True:
        buy_or_sell = input("Are you looking to buy or sell? Or would you like to enter the arena? ").strip().lower()

        while buy_or_sell not in ["buy", "sell", "enter", "enter arena", "enter the arena"]:
            buy_or_sell = input("Please enter buy, sell, or enter the arena. ").strip().lower()

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

        elif buy_or_sell in ["enter", "enter arena", "enter the arena"]:
            battle()
            return

def battle():
    hero["health"] = hero["max health"]

    print(f"{hero["name"]} enters the arena.")

    for enemy in enemies:
        if enemy["defeated"] == True:
            continue
        print(f"The {enemy["name"]} challenges {hero["name"]}.\n"
              "The battle begins.")
        while enemy["health"] > 0 and hero["health"] > 0:
            if hero["speed"] > enemy["speed"]:
                hero_action(enemy)
                if enemy["health"] > 0:
                    enemy_action(enemy)
            elif enemy["speed"] > hero["speed"]:
                enemy_action(enemy)
                if hero["health"] > 0:
                    hero_action(enemy)
            elif hero["speed"] == enemy["speed"]:
                turn_order = [hero_action, enemy_action]
                random.shuffle(turn_order)
                for turn in turn_order:
                    turn(enemy)
                    if hero["health"] <= 0 or enemy["health"] <= 0:
                        break
        if hero["health"] <= 0 and enemy["health"] > 0:
            print(f"{hero["name"]} has been defeated and is carted out of the arena. ")
            armory()
            break
        
        elif hero["health"] > 0 and enemy["health"] <= 0:
            print(f"{enemy["name"]} has been defeated.")
            print(f"{hero["name"]} gains {enemy["exp_given"]} exp.")
            hero["exp"] += enemy["exp_given"]
            print(f"{hero["name"]} gains {enemy["gold_given"]} gold.")
            hero["gold"] += enemy["gold_given"]
            enemy["defeated"] = True

        if enemy["defeated"] == True:
            print(f"{hero["name"]} is the winner! You gather your rewards and return to the armory.")
            break

def hero_action(enemy):
    action = input("Choose your next action. Attack / Verbal Joust ").strip().lower()

    while action not in ["attack", "verbal joust"]:
        action = input("Please choose Attack or Verbal Joust. ")

    if action == "attack":
        print(f"{hero["name"]} attacks {enemy["name"]}!")
        enemy["health"] -= weapons[hero["weapon"]]["damage"]
        print(f"{enemy["name"]} Health: {enemy["health"]}")
    elif action == "verbal joust":
        print(f"{hero["name"]} insults the {enemy["name"]}!")
        print(random.choice(verbal_jousts))
        if enemy["speed"] <= 1:
            print(f"{enemy["name"]}'s speed cannot be lowered any further.")
        else:
            enemy["speed"] -= 1

def enemy_action(enemy):
    if "pet" in enemy:
        print(f"The {enemy["name"]}'s {enemy["pet"]["name"]} attacks!")
        hero["health"] -= enemy["pet"]["damage"]
        print(f"Hero Health: {hero["health"]}")

    print(f"The {enemy["name"]} attacks!")
    hero["health"] -= enemy["damage"]
    print(f"Hero Health: {hero["health"]}")

main()