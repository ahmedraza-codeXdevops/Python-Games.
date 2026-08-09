import random

player = {
    "name": "",
    "health": 100,
    "max_health": 100,
    "attack": 20,
    "coins": 0,
    "potions": 3,
    "level": 1,
    "xp": 0
}

enemies = [
    {"name": "Goblin", "health": 40, "attack": 10, "xp": 20},
    {"name": "Skeleton", "health": 50, "attack": 12, "xp": 30},
    {"name": "Orc", "health": 70, "attack": 15, "xp": 40},
    {"name": "Dark Knight", "health": 100, "attack": 20, "xp": 60}
]


def show_status():
    print("\n========== PLAYER STATUS ==========")
    print("Name:", player["name"])
    print("Level:", player["level"])
    print("Health:", player["health"], "/", player["max_health"])
    print("Attack:", player["attack"])
    print("Coins:", player["coins"])
    print("Potions:", player["potions"])
    print("XP:", player["xp"])
    print("===================================")


def level_up():
    required_xp = player["level"] * 50

    if player["xp"] >= required_xp:
        player["level"] += 1
        player["max_health"] += 20
        player["health"] = player["max_health"]
        player["attack"] += 5

        print("\n🎉 LEVEL UP!")
        print("You reached Level", player["level"])
        print("Health increased!")
        print("Attack increased!")


def battle(enemy):
    enemy_health = enemy["health"]

    print("\n⚔️ A", enemy["name"], "appeared!")

    while enemy_health > 0 and player["health"] > 0:

        print("\nYour Health:", player["health"])
        print(enemy["name"], "Health:", enemy_health)

        print("\n1. Attack")
        print("2. Use Potion")
        print("3. Run")

        choice = input("Choose: ")

        if choice == "1":
            damage = random.randint(
                player["attack"] - 5,
                player["attack"] + 5
            )

            enemy_health -= damage

            print(
                "\n⚔️ You attacked the",
                enemy["name"],
                "for",
                damage,
                "damage!"
            )

            if enemy_health <= 0:
                print("\n🏆 You defeated the", enemy["name"])
                player["coins"] += random.randint(10, 30)
                player["xp"] += enemy["xp"]

                print("💰 Coins:", player["coins"])
                print("⭐ XP:", player["xp"])

                level_up()
                return True

        elif choice == "2":

            if player["potions"] > 0:

                healing = random.randint(20, 35)

                player["health"] = min(
                    player["health"] + healing,
                    player["max_health"]
                )

                player["potions"] -= 1

                print(
                    "\n🧪 You recovered",
                    healing,
                    "health!"
                )

            else:
                print("\n❌ You don't have any potions!")

        elif choice == "3":

            if random.choice([True, False]):
                print("\n🏃 You escaped!")
                return True
            else:
                print("\n❌ You couldn't escape!")

        else:
            print("\n❌ Invalid choice!")
            continue

        if enemy_health > 0:

            damage = random.randint(
                enemy["attack"] - 3,
                enemy["attack"] + 3
            )

            player["health"] -= damage

            print(
                "💥 The",
                enemy["name"],
                "attacked you for",
                damage,
                "damage!"
            )

    if player["health"] <= 0:
        print("\n💀 You have been defeated!")
        return False


def explore():
    print("\n🌲 You enter a mysterious forest...")

    event = random.randint(1, 4)

    if event == 1:
        enemy = random.choice(enemies)
        return battle(enemy)

    elif event == 2:
        coins = random.randint(10, 50)
        player["coins"] += coins

        print("\n💰 You found", coins, "coins!")
        return True

    elif event == 3:
        player["potions"] += 1

        print("\n🧪 You found a health potion!")
        return True

    else:
        print("\n🌿 The forest is quiet...")
        print("Nothing happened.")
        return True


def treasure():
    print("\n🏰 You discovered an ancient castle!")

    print("\nA giant Dark Knight guards the treasure.")

    enemy = {
        "name": "Dark Knight",
        "health": 120,
        "attack": 22,
        "xp": 100
    }

    if battle(enemy):

        print("\n🎉 You defeated the Dark Knight!")
        print("💎 You found the legendary treasure!")
        print("\n🏆 YOU WIN THE GAME! 🏆")

        return True

    return False


def shop():
    print("\n🏪 Welcome to the shop!")

    print("Coins:", player["coins"])

    print("\n1. Health Potion - 20 coins")
    print("2. Attack Upgrade - 50 coins")
    print("3. Leave")

    choice = input("\nChoose: ")

    if choice == "1":

        if player["coins"] >= 20:
            player["coins"] -= 20
            player["potions"] += 1

            print("\n🧪 Potion purchased!")

        else:
            print("\n❌ Not enough coins!")

    elif choice == "2":

        if player["coins"] >= 50:
            player["coins"] -= 50
            player["attack"] += 5

            print("\n⚔️ Attack increased!")

        else:
            print("\n❌ Not enough coins!")

    elif choice == "3":
        return

    else:
        print("\n❌ Invalid choice!")


print("===================================")
print("       🏰 ADVENTURE RPG 🏰")
print("===================================")

player["name"] = input("\nEnter your character name: ")

print("\nWelcome,", player["name"] + "!")
print("Your adventure begins...")

while player["health"] > 0:

    print("\n========== MAIN MENU ==========")
    print("1. Explore Forest")
    print("2. Visit Shop")
    print("3. Show Status")
    print("4. Search for Treasure")
    print("5. Exit")
    print("===============================")

    choice = input("Choose an option: ")

    if choice == "1":

        if not explore():
            break

    elif choice == "2":
        shop()

    elif choice == "3":
        show_status()

    elif choice == "4":

        if treasure():
            break
        else:
            break

    elif choice == "5":
        print("\nThanks for playing!")
        break

    else:
        print("\n❌ Invalid choice!")

print("\nGame Over!")