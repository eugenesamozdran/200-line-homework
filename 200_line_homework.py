import random

#defining the order
def player_order(p1,p2):
    global order
    
    print("Player 1 rolled ", p1)
    print("Player 2 rolled ", p2)
    
    if p1 == "rock" and p2 == "scissors":
        print("Player 1 goes first!")
        order = 1
    elif p1 == "rock" and p2 == "paper":
        print("Player 2 goes first!")
        order = 2
    elif p1 == "scissors" and p2 == "rock":
        print("Player 2 goes first!")
        order = 2
    elif p1 == "scissors" and p2 == "paper":
        print("Player 1 goes first!")
        order = 1
    elif p1 == "paper" and p2 == "rock":
        print("Player 1 goes first!")
        order = 1
    elif p1 == "paper" and p2 == "scissors":
        print("Player 2 goes first!")
        order = 2
    elif p1 == p2:
        print("It's a draw! One more time:")
        p1 = random.choice(("rock", "scissors", "paper",))
        p2 = random.choice(("rock", "scissors", "paper",))
        player_order(p1,p2)

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

#basic hit points depending on the race
orc_hp = 55
human_hp = 50
elf_hp = 47
gnoll_hp = 49

#hit points modifier for each class
t_mod = 1.1
b_mod = 1.2
s_mod = 1
w_mod = 0.9

#attack modifier for each weapon
sw_att = 1
ham_att = 1
cr_att = 1.2
sb_att = 1.4

while True:

    print("Greetings! Let the fate decide who goes first: ")

    p1 = random.choice(("rock", "scissors", "paper",))
    p2 = random.choice(("rock", "scissors", "paper",))
    player_order(p1,p2)
    print("Let the fun begin!")

    #creating the character
    p1_race = input("Player 1, choose your race ('orc', 'human', 'elf' or 'gnoll'): ")
    while p1_race not in race:
        p1_race = input("Please try again: ")
    p1_class = input("Your class ('tank', 'berserker', 'shooter' or 'wizard'): ")
    while p1_class not in battle_class:
        p1_class = input("Please try again: ")
    p1_weap = input("And your weapon ('sword', 'hammer', 'crossbow' or 'spell book'): ")
    while p1_weap not in weapons:
        p1_weap = input("Please try again: ")
    p2_race = input("Player 2, choose your race ('orc', 'human', 'elf' or 'gnoll'): ")
    while p2_race not in race:
        p2_race = input("Please try again: ")
    p2_class = input("Your class ('tank', 'berserker', 'shooter' or 'wizard'): ")
    while p2_class not in battle_class:
        p2_class = input("Please try again: ")
    p2_weap = input("And your weapon ('sword', 'hammer', 'crossbow' or 'spell book'): ")
    while p2_weap not in weapons:
        p2_weap = input("Please try again: ")

    #player 1 hit points
    if p1_race == "orc" and p1_class == "tank":
        p1_hp = orc_hp*t_mod
    elif p1_race == "orc" and p1_class == "berserker":
        p1_hp = orc_hp*b_mod
    elif p1_race == "orc" and p1_class == "shooter":
        p1_hp = orc_hp*s_mod
    elif p1_race == "orc" and p1_class == "wizard":
        p1_hp = orc_hp*w_mod
    elif p1_race == "human" and p1_class == "tank":
        p1_hp = human_hp*t_mod
    elif p1_race == "human" and p1_class == "berserker":
        p1_hp = human_hp*b_mod
    elif p1_race == "human" and p1_class == "shooter":
        p1_hp = human_hp*s_mod
    elif p1_race == "human" and p1_class == "wizard":
        p1_hp = human_hp*w_mod
    elif p1_race == "elf" and p1_class == "tank":
        p1_hp = elf_hp*t_mod
    elif p1_race == "elf" and p1_class == "berserker":
        p1_hp = elf_hp*b_mod
    elif p1_race == "elf" and p1_class == "shooter":
        p1_hp = elf_hp*s_mod
    elif p1_race == "elf" and p1_class == "wizard":
        p1_hp = elf_hp*w_mod
    elif p1_race == "gnoll" and p1_class == "tank":
        p1_hp = gnoll_hp*t_mod
    elif p1_race == "gnoll" and p1_class == "berserker":
        p1_hp = gnoll_hp*b_mod
    elif p1_race == "gnoll" and p1_class == "shooter":
        p1_hp = gnoll_hp*s_mod
    elif p1_race == "gnoll" and p1_class == "wizard":
        p1_hp = gnoll_hp*w_mod

    #player 2 hit points
    if p2_race == "orc" and p2_class == "tank":
        p2_hp = orc_hp*t_mod
    elif p2_race == "orc" and p2_class == "berserker":
        p2_hp = orc_hp*b_mod
    elif p2_race == "orc" and p2_class == "shooter":
        p2_hp = orc_hp*s_mod
    elif p2_race == "orc" and p2_class == "wizard":
        p2_hp = orc_hp*w_mod
    elif p2_race == "human" and p2_class == "tank":
        p2_hp = human_hp*t_mod
    elif p2_race == "human" and p2_class == "berserker":
        p2_hp = human_hp*b_mod
    elif p2_race == "human" and p2_class == "shooter":
        p2_hp = human_hp*s_mod
    elif p2_race == "human" and p2_class == "wizard":
        p2_hp = human_hp*w_mod
    elif p2_race == "elf" and p2_class == "tank":
        p2_hp = elf_hp*t_mod
    elif p2_race == "elf" and p2_class == "berserker":
        p2_hp = elf_hp*b_mod
    elif p2_race == "elf" and p2_class == "shooter":
        p2_hp = elf_hp*s_mod
    elif p2_race == "elf" and p2_class == "wizard":
        p2_hp = elf_hp*w_mod
    elif p2_race == "gnoll" and p2_class == "tank":
        p2_hp = gnoll_hp*t_mod
    elif p2_race == "gnoll" and p2_class == "berserker":
        p2_hp = gnoll_hp*b_mod
    elif p2_race == "gnoll" and p2_class == "shooter":
        p2_hp = gnoll_hp*s_mod
    elif p2_race == "gnoll" and p2_class == "wizard":
        p2_hp = gnoll_hp*w_mod

    #starting the fight if Player 1 should go first
    if order == 1:
        while True:
            print("Player 1 has {0} HP and Player 2 has {1} HP".format(p1_hp, p2_hp))

            #different range of integers is chosen to show the difference between each weapon
            
            attack_1 = input("Player 1, describe your attack to your opponent and enter 'go!': ")
            while attack_1 not in ("go!",):
                attack_1 = input("Please try again: ")
            if attack_1 == "go!":
                if p1_weap == "sword":
                    p2_hp -= sw_att*random.randint(1,15)
                elif p1_weap == "hammer":
                    p2_hp -= ham_att*random.randint(1,15)
                elif p1_weap == "crossbow":
                    p2_hp -= cr_att*random.randint(1,20)
                elif p1_weap == "spell book":
                    p2_hp -= sb_att*random.randint(1,23)

            attack_2 = input("Player 2, describe your attack to your opponent and enter 'go!': ")
            while attack_2 not in ("go!",):
                attack_2 = input("Please try again: ")
            if attack_2 == "go!":
                if p2_weap == "sword":
                    p1_hp -= sw_att*random.randint(1,15)
                elif p2_weap == "hammer":
                    p1_hp -= ham_att*random.randint(1,15)
                elif p2_weap == "crossbow":
                    p1_hp -= cr_att*random.randint(1,20)
                elif p2_weap == "spell book":
                    p1_hp -= sb_att*random.randint(1,23)    

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
                if p2_weap == "sword":
                    p1_hp -= sw_att*random.randint(1,15)
                elif p2_weap == "hammer":
                    p1_hp -= ham_att*random.randint(1,15)
                elif p2_weap == "crossbow":
                    p1_hp -= cr_att*random.randint(1,20)
                elif p2_weap == "spell book":
                    p1_hp -= sb_att*random.randint(1,23)

            attack_1 = input("Player 1, describe your attack to your opponent and enter 'go!': ")
            while attack_1 not in ("go!",):
                attack_1 = input("Please try again: ")
            if attack_1 == "go!":
                if p1_weap == "sword":
                    p2_hp -= sw_att*random.randint(1,15)
                elif p1_weap == "hammer":
                    p2_hp -= ham_att*random.randint(1,15)
                elif p1_weap == "crossbow":
                    p2_hp -= cr_att*random.randint(1,20)
                elif p1_weap == "spell book":
                    p2_hp -= sb_att*random.randint(1,23)    

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
