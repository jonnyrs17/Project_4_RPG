import time


def intro():

    print(" ---------------------------- ")
    print(" -------------THE------------ ")
    print(" --- COMPENDIUM OF POWER ---- ")
    print(" ---------------------------- ")
    time.sleep(1)
    while True:
        name = input("Character Name: ").capitalize()
        confirm_name = input(f"Confirm your name is {name}? Y/N ").upper()
        if confirm_name == "Y":
            break
        else:
            continue

    while True:
        print("""Choose your class?
            [S] SOLDIER
            [R] ROGUE
            [A] ADEPT""")
        role = input().upper()
        if role == "S":
            print("SOLDIER: Specializes in melee weapons, shields and armour. ")
            time.sleep(1)
            print("Confirm choice: SOLDIER? Y/N")
            confirm = input("").upper()
            if confirm == "Y":
                return name, role
            else:
                continue
        elif role == "R":
            print("ROGUE: Specializes in ranged combat, stealth, traps and poisons. ")
            time.sleep(1)
            print("Confirm choice: ROGUE? Y/N")
            confirm = input("").upper()
            if confirm == "Y":
                return name, role
            else:
                continue
        elif role == "A":
            print("ADEPT: Specializes in manipulating the Fringes of Power. ")
            time.sleep(1)
            print("Confirm choice: ADEPT? Y/N")
            confirm = input("").upper()
            if confirm == "Y":
                return name, role
            else:
                continue
        else:
            print("Invalid input. Choice is either [S], [R] or [A]")
            continue


def game_over():
    print(" ---------------------------- ")
    print(" -------- GAME OVER --------- ")
    print(" ---------------------------- ")


def combat(hero, enemy):

    hero_hp = hero.return_hp()
    enemy_hp = enemy.return_hp()

    while hero_hp > 0 or enemy_hp > 0:

        print("You attack the daamon!")
        hero_attack_roll = hero.attack_roll()
        time.sleep(1)
        print(f'You rolled {hero_attack_roll}')
        enemy_defense_roll = enemy.defense_roll()
        time.sleep(1)
        if hero_attack_roll > enemy_defense_roll:
            print("Your attack hits!")
            dmg = hero.damage_roll()
            enemy.damage_taken(dmg)
        else:
            print("Your attack missed.")
        time.sleep(1)

        print("The enemy attacks!")
        enemy_attack_roll = enemy.attack_roll()
        print(f'The enemy rolled {enemy_attack_roll}')
        hero_defense_roll = hero.defense_roll()
        if enemy_attack_roll > hero_defense_roll:
            print("You have been hit!")
            enemy_dmg = enemy.damage_roll()
            hero.damage_taken(enemy_dmg)
        else:
            print("The attack missed")

    if hero_hp == 0:
        print("You have died")
        time.sleep(2)
        game_over()
    else:
        print(f'Your HP is {hero_hp}')
        loot = enemy.get_inventory
        print(f'The enemy dropped {loot}')

        return hero


