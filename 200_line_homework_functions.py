import random

#defining the order
def player_order(p1,p2):
      
    print("Player 1 rolled ", p1)
    print("Player 2 rolled ", p2)
    
    if p1 == "rock" and p2 == "scissors":
        print("Player 1 goes first!")
        return 1
    elif p1 == "rock" and p2 == "paper":
        print("Player 2 goes first!")
        return 2
    elif p1 == "scissors" and p2 == "rock":
        print("Player 2 goes first!")
        return 2
    elif p1 == "scissors" and p2 == "paper":
        print("Player 1 goes first!")
        return 1
    elif p1 == "paper" and p2 == "rock":
        print("Player 1 goes first!")
        return 1
    elif p1 == "paper" and p2 == "scissors":
        print("Player 2 goes first!")
        return 2
    elif p1 == p2:
        print("It's a draw! One more time:")
        p1 = random.choice(("rock", "scissors", "paper",))
        p2 = random.choice(("rock", "scissors", "paper",))
        player_order(p1,p2)

#counting damage amount dealt after one attack 
def damage_caused(chosen_weap):

    #damage modifier for each weapon
    Sw_dmg = 1
    Ham_dmg = 1
    Cr_dmg = 1.2
    Sb_dmg = 1.4
    if chosen_weap == "sword":
        return Sw_dmg*random.randint(1,15)
    elif chosen_weap == "hammer":
        return Ham_dmg*random.randint(1,15)
    elif chosen_weap == "crossbow":
        return Cr_dmg*random.randint(1,20)
    elif chosen_weap == "spell book":
        return Sb_dmg*random.randint(1,23)

#counting hit points based on the chosen race and class
def race_and_class_hp(chosen_race, chosen_class):

    #basic hit points depending on the race
    Orc_hp = 55
    Human_hp = 50
    Elf_hp = 47
    Gnoll_hp = 49

    #hit points modifier for each class
    Tank_mod = 1.1
    Bers_mod = 1.2
    Shoot_mod = 1
    Wiz_mod = 0.9

    #hit points formula for each race/class combination
    orc_classes_hp = {
                      ("orc", "tank"): Orc_hp*Tank_mod,
                      ("orc", "berserker"): Orc_hp*Bers_mod,
                      ("orc", "shooter"): Orc_hp*Shoot_mod,
                      ("orc", "wizard"): Orc_hp*Wiz_mod
                     }
    
    human_classes_hp = {
                        ("human", "tank"): Human_hp*Tank_mod,
                        ("human", "berserker"): Human_hp*Bers_mod,
                        ("human", "shooter"): Human_hp*Shoot_mod,
                        ("human", "wizard"): Human_hp*Wiz_mod
                       }
    
    elf_classes_hp = {
                      ("elf", "tank"): Elf_hp*Tank_mod,
                      ("elf", "berserker"): Elf_hp*Bers_mod,
                      ("elf", "shooter"): Elf_hp*Shoot_mod,
                      ("elf", "wizard"): Elf_hp*Wiz_mod
                     }
    
    gnoll_classes_hp = {
                        ("gnoll", "tank"): Gnoll_hp*Tank_mod,
                        ("gnoll", "berserker"): Gnoll_hp*Bers_mod,
                        ("gnoll", "shooter"): Gnoll_hp*Shoot_mod,
                        ("gnoll", "wizard"): Gnoll_hp*Wiz_mod
                       }
    if chosen_race == "orc":
        return orc_classes_hp[(chosen_race, chosen_class)]
    elif chosen_race == "human":
        return human_classes_hp[(chosen_race, chosen_class)]
    elif chosen_race == "elf":
        return elf_classes_hp[(chosen_race, chosen_class)]
    elif chosen_race == "gnoll":
        return gnoll_classes_hp[(chosen_race, chosen_class)]

#describing races, classes, weapons, hit points and damage
race = ("orc",
        "human",
        "elf",
        "gnoll")
battle_class = ("tank",
                "berserker",
                "shooter",
                "wizard")
weapons = ("sword",
           "hammer",
           "crossbow",
           "spell book")

while True:

    print("Greetings! Let the fate decide who goes first: ")

    p1 = random.choice(("rock", "scissors", "paper",))
    p2 = random.choice(("rock", "scissors", "paper",))
    order = player_order(p1,p2)
    print("Let the fun begin!")
    
    #creating the character
    p1_race = input("Player 1, choose your race {}: ".format(race))
    while p1_race not in race:
        p1_race = input("Please try again: ")
    p1_class = input("Your class {}: ".format(battle_class))
    while p1_class not in battle_class:
        p1_class = input("Please try again: ")
    p1_weap = input("And your weapon {}: ".format(weapons))
    while p1_weap not in weapons:
        p1_weap = input("Please try again: ")
    p2_race = input("Player 2, choose your race {}: ".format(race))
    while p2_race not in race:
        p2_race = input("Please try again: ")
    p2_class = input("Your class {}: ".format(battle_class))
    while p2_class not in battle_class:
        p2_class = input("Please try again: ")
    p2_weap = input("And your weapon {}: ".format(weapons))
    while p2_weap not in weapons:
        p2_weap = input("Please try again: ")

    #player 1 and 2 hit points
    p1_hp = race_and_class_hp(p1_race, p1_class)
    p2_hp = race_and_class_hp(p2_race, p2_class)
    
    #starting the fight if Player 1 should go first
    if order == 1:
        while True:
            print("Player 1 has {0} HP and Player 2 has {1} HP".format(p1_hp, p2_hp))

            attack_1 = input("Player 1, describe your attack to your opponent and enter 'go!': ")
            while attack_1 not in ("go!",):
                attack_1 = input("Please try again: ")
            if attack_1 == "go!":
                p2_hp -= damage_caused(p1_weap)
                
            attack_2 = input("Player 2, describe your attack to your opponent and enter 'go!': ")
            while attack_2 not in ("go!",):
                attack_2 = input("Please try again: ")
            if attack_2 == "go!":
                p1_hp -= damage_caused(p2_weap)   

            if p1_hp <= 0 or p2_hp <= 0:
                print("Player 1 has {0} HP and Player 2 has {1} HP, congratulations to the winner!".format(p1_hp, p2_hp))
                break
            else:
                continue

    #starting the fight if Player 2 should go first
    if order == 2:
        while True:
            print("Player 1 has {0} HP and Player 2 has {1} HP".format(p1_hp, p2_hp))

            attack_2 = input("Player 2, describe your attack to your opponent and enter 'go!': ")
            while attack_2 not in ("go!",):
                attack_2 = input("Please try again: ")
            if attack_2 == "go!":
                p1_hp -= damage_caused(p2_weap)

            attack_1 = input("Player 1, describe your attack to your opponent and enter 'go!': ")
            while attack_1 not in ("go!",):
                attack_1 = input("Please try again: ")
            if attack_1 == "go!":
                p2_hp -= damage_caused(p1_weap)   

            if p1_hp <= 0 or p2_hp <= 0:
                print("Player 1 has {0} HP and Player 2 has {1} HP, congratulations to the winner!".format(p1_hp, p2_hp))
                break
            else:
                continue
    
    #asking if players want to start the game again
    repeat = input("Would you like to play again? Enter 'y' for another game or 'n' to quit: ")
    while repeat not in ("y","n"):
        repeat = input("Please make a valid choice ('y' or 'n'): ")
    if repeat=="y":
        continue
    else:
        print("Good bye!")
        break
