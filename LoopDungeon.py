import random
import sys
import time
from colorama import Fore, Style, init
init(autoreset=True)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

suits = ["♠", "♥", "♦", "♣"]
ranks = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
COLORS = {
    "♠": Fore.LIGHTBLACK_EX,
    "♥": Fore.RED,
    "♦": Fore.CYAN, 
    "♣": Fore.GREEN,
    "Special": Fore.YELLOW
}

def create_deck():
    deck = []
    deck.append("Exit")
    deck.append("Campfire")
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank}{suit}")
    random.shuffle(deck)
    return deck
def create_temple(deck):
    temple = []
    for i in range(54):
        temple.append([deck.pop(0), "H"])
    return temple
def remove(temple, inventory):
    if temple[0][0].isdigit():
        inventory.append(temple[0])
        temple.pop(0)
    return temple, inventory
def is_number(card):
   if card[1] != "H": 
    return card[0][:-1].isdigit()
def number(card):
    if card[0][:-1].isdigit():
     return int(card[0][:-1])
def trap(card):
   if card[1] != "H": 
    if not is_number(card) and card[0] != "Exit" and card[0] != "Campfire" and card[0][0] != "A":
        return True
def is_hidden(card):
   return card[1] == "H"
def is_hiddenface(card):
   if card[1] == 'H':
      if not card[0][:-1].isdigit() and card[0] != "Exit" and card[0] != "Campfire" and card[0][0] != "A":
        return True
def name(s):
    if s == "♠":
        return f"{Fore.LIGHTBLACK_EX}Spades{Style.RESET_ALL}"
    elif s == "♥":
        return f"{Fore.RED}Hearts{Style.RESET_ALL}"
    elif s == "♦":
        return f"{Fore.CYAN}Diamonds{Style.RESET_ALL}"
    elif s == "♣":
        return f"{Fore.GREEN}Clubs{Style.RESET_ALL}"
def map(temple):
    grid = []
    W = 8

    for cell in temple:
        if cell[1] == "H":
            text = "H".center(W)
            grid.append(Fore.LIGHTBLACK_EX + text + Style.RESET_ALL)
        else:
            card = cell[0]
            
            if card in ["Exit", "Campfire"]:
                text = card.center(W)
                grid.append(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")
            else:
                rank = card[:-1]
                suit = card[-1]
                color = COLORS.get(suit, Fore.WHITE)
                display_name = f"{rank}{suit}"
                text = display_name.center(W)
                grid.append(f"{color}{text}{Style.RESET_ALL}")

    for i in range(0, len(grid), 10):
        row = " | ".join(grid[i:i+10])
        print(f"| {row} |")
def color_card(card):
    if card in ["Exit", "Campfire"]:
        return f"{Fore.YELLOW}{card}{Style.RESET_ALL}"
    
    rank = card[:-1]
    suit = card[-1]
    color = COLORS.get(suit, Fore.WHITE)
    
    return f"{rank}{color}{suit}{Style.RESET_ALL}"

def get_colored_set(input_list):
    return [color_card(c) for c in input_list]
def play():
    deck = create_deck()
    deck_copy = deck[:]
    temple = create_temple(deck_copy)
    inventory = []
    backpack = []
    relics = []
    used_relics = []
    game_active = True
    escape = False
    mastered_suits = []
    boss_fight = False
    victory = 0
    suit_counter = 0
    print(" █████                                     \033[91m ██████████                                                             \033[0m    ")
    print("▒▒███                                \033[91m      ▒▒███▒▒▒▒███                                                              \033[0m  ")
    print(" ▒███         ██████   ██████  ████████   \033[91m  ▒███   ▒▒███ █████ ████ ████████    ███████  ██████   ██████  ████████   \033[0m  ")
    print(" ▒███        ███▒▒███ ███▒▒███▒▒███▒▒███  \033[91m  ▒███    ▒███▒▒███ ▒███ ▒▒███▒▒███  ███▒▒███ ███▒▒███ ███▒▒███▒▒███▒▒███  \033[0m  ")
    print(" ▒███       ▒███ ▒███▒███ ▒███ ▒███ ▒███   \033[91m ▒███    ▒███ ▒███ ▒███  ▒███ ▒███ ▒███ ▒███▒███████ ▒███ ▒███ ▒███ ▒███ \033[0m   ")
    print(" ▒███      █▒███ ▒███▒███ ▒███ ▒███ ▒███  \033[91m  ▒███    ███  ▒███ ▒███  ▒███ ▒███ ▒███ ▒███▒███▒▒▒  ▒███ ▒███ ▒███ ▒███   \033[0m ")
    print(" ███████████▒▒██████ ▒▒██████  ▒███████   \033[91m  ██████████   ▒▒████████ ████ █████▒▒███████▒▒██████ ▒▒██████  ████ █████  \033[0m ")
    print("▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒   ▒▒▒▒▒▒   ▒███▒▒▒   \033[91m  ▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒▒ ▒▒▒▒ ▒▒▒▒▒  ▒▒▒▒▒███ ▒▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒ ▒▒▒▒▒  \033[0m  ")
    print("                               ▒███             \033[91m                               ███ ▒███                             \033[0m   ")
    print("                               █████                 \033[91m                         ▒▒██████                             \033[0m    ")
    print("                              ▒▒▒▒▒                      \033[91m                      ▒▒▒▒▒▒        \033[0m   (ver 1.5)                     ")
    playing = True
    while game_active and playing:

        action = input("\nLook, Explore, Collect, Backpack, Relic or Check? (l/e/c/b/r/ch): ").lower()
#################################################################
        if action == "l":
            if temple[0][1] == "H":
                temple[0][1] = "V"
                deck.remove(temple[0][0])
                if temple[1][1] == "H":
                    temple[1][1] = "V"
                    print(f"You look at the dungeon and see: {color_card(temple[0][0])} and {color_card(temple[1][0])}")
                    deck.remove(temple[1][0])
                elif temple[1][1] != "H":
                    print(f"You look at the dungeon and see: {color_card(temple[0][0])}")
            elif temple[0][1] != "H":
                print(f"You can't do that, the first card is already revealed: {color_card(temple[0][0])}")
            if len(backpack) > 0:
                print(f"You have the following cards in your backpack: [{', '.join(get_colored_set(backpack))}]")
            if len(relics) > 0:
                print(f"You have the following relics: [{', '.join(get_colored_set(relics))}]")
            map(temple)
       ###############################################################     
        if action == "e":
            available_indices = [i for i in [0, 1] if is_number(temple[i])]

            if not available_indices:
                print("No moves available. You can't explore because neither of the first two cards are numbers.")
                if len(backpack) == 0 and len(relics) == 0 and temple[0][1] != "H" and temple[1][1] != "H":
                    print("You have no cards in your backpack and no relics to help you.")
                    game_active = False
            else:
                while True:
                    map(temple)
                    options = [str(i+1) for i in available_indices] + ["0"]
                    prompt_moves = " / ".join([str(color_card(temple[i][0])) for i in available_indices])
            
                    jump = input(f"Available moves: {prompt_moves}. Do you want to explore? ({'/'.join(options)}): ")
            
                    if jump == "0":
                       print("You decide not to explore.")
                       break
                    elif jump in options:
                        move_value = number(temple[int(jump)-1])
                        print("You decide to explore!")
                        for _ in range(move_value):
                            temple.append(temple[0])
                            temple.pop(0)
                        current_card = temple[0]
                        if trap(current_card):
                          if "A♥" in relics:
                            print(f"You face a statue ({color_card(current_card[0])})! However, Your {color_card('A♥')} relic saved you from the battle!")
                            relics.remove("A♥")
                            used_relics.append("A♥")
                            current_card[1] = "H"
                          else:
                            print(f"You face a statue ({color_card(current_card[0])})!")
                            game_active = False
                            break 
                        elif is_number(current_card):
                            inventory.append(current_card[0])
                            print(f"Collected: {color_card(current_card[0])}!")
                            for s in suits:
                                if s not in mastered_suits:
                                    in_inv = sum(1 for item in inventory if item.endswith(s))
                                    has_ace = f"A{s}" in relics or f"A{s}" in used_relics
                                    
                                    if in_inv == 9 and has_ace:
                                        mastered_suits.append(s)
                                        print(f"\n SUIT BLESSING: {s} ")
                                        print(f"You have collected every card of the {s} suit. You have been honored by the Royal house of {name(s)}")
                                        for item in temple:
                                            if item[0].endswith(s) and trap(item):
                                                print(f"All {s} statues in the dungeon won't attack you...for now")
                            temple.pop(0)
                        elif current_card[0][0] == "A" and current_card[1] != "H":
                            print(f"You found a relic ({color_card(current_card[0])})!")
                            relics.append(current_card[0])
                            temple.pop(0)
                        elif current_card[0] == "Exit" and current_card[1] != "H" or current_card[0] == "Campfire" and current_card[1] != "H":
                            if current_card[0] == "Exit":
                                escape = True
                                print("You found an exit!")
                                game_active = False
                            if current_card[0] == "Campfire":
                               if len(used_relics) == 0:
                                print("You found a campfire. You can use it to recover 2 relics, but you have no relics to recover.")
                               elif len(used_relics) > 0:
                                print("You found a campfire.You can use it to recover 2 relics")
                                choose_relics = True
                                while choose_relics:
                                    counter = 2
                                    relic_options = range(1, len(used_relics) + 1)
                                    prompt_relics = " / ".join(get_colored_set(used_relics))
                                    used_relics_input = input(f"You used {prompt_relics}. Which relic do you want to recover? ({'/'.join([str(i) for i in relic_options] + ['0'])}): ")
                                    if used_relics_input not in [str(i) for i in relic_options] and used_relics_input != "0":
                                        print("Invalid input. Try again.")
                                    elif used_relics_input == "0":
                                        print("You decide not to recover any relics.")
                                        choose_relics = False
                                    else:
                                        chosen_relic = used_relics[int(used_relics_input) - 1]
                                        relics.append(chosen_relic)
                                        used_relics.remove(chosen_relic)
                                        counter -= 1
                                        if counter == 1:
                                         print(f"You recovered the {color_card(chosen_relic)} relic. You can recover {counter} more relic(s).")
                                        elif counter == 0:
                                         print(f"You recovered the {color_card(chosen_relic)} relic. You have recovered all your relics for now.")
                                         choose_relics = False
                        if len(backpack) > 0:
                            print(f"You have the following cards in your backpack: [{', '.join(get_colored_set(backpack))}]")
                        if len(relics) > 0:
                            print(f"You have the following relics: [{', '.join(get_colored_set(relics))}]")
                        map(temple)
                        break 
                    else:
                        print("Invalid input. Try again.")
              ##############################################################          
        if action == 'c':
            if len(backpack) <= 2:
                if temple[0][1] != "H" and is_number(temple[0]):
                    print(f"You collected the card {color_card(temple[0][0])} and add it to your backpack.")
                    backpack.append(temple[0][0])
                    temple.pop(0)
                    print(f"You have the following cards in your backpack: [{', '.join(get_colored_set(backpack))}]")
                    if len(relics) > 0:
                     print(f"You have the following relics: [{', '.join(get_colored_set(relics))}]")
                    map(temple)
                else:
                    print("You can't collect a card that hasn't been revealed yet.")
            else:
                print("Your backpack is full. You can only have 3 cards in your backpack at a time.")
               ############################################################### 
        if action == 'b':
            if len(backpack) == 0:
                print("You have no cards in your backpack to use.")
            else:
                print(f"You have the following cards in your backpack: [{', '.join(get_colored_set(backpack))}]")
                options = [str(i) for i in range(1, len(backpack) + 1)]
                choose_backpack = True
                while choose_backpack:
                    index_card = input(f"Which card do you want to use? ({'/'.join(options)}/0): ")
                    if index_card not in options and index_card != "0":
                        print("Invalid input. Try again.")
                    elif index_card != "0" and index_card in options:
                        index_card = int(index_card)
                        temple.insert(0, [backpack[index_card-1], "V"])
                        print(f"You used the card {color_card(backpack[index_card-1])} and placed it back on top of the dungeon.")
                        backpack.pop(index_card-1)
                        if len(backpack) > 0:
                            print(f"You have the following cards in your backpack: [{', '.join(get_colored_set(backpack))}]")
                        map(temple)
                        choose_backpack = False

                    elif index_card == "0":
                        print("You decide not to use a card.")
                        choose_backpack = False
            ###########################################################            
        if action == 'r':
          if len(relics) == 0:
           print("You have no relics to use.")
          else: 
           using_relics = True
           while using_relics:
               options = [str(i) for i in range(1, len(relics) + 1)]
               prompt_relics = " / ".join(get_colored_set(relics))
               index_relic = input(f"You have the following relics: {prompt_relics}. Which relic do you want to use? ({'/'.join(options)}/0): ") 
               if index_relic not in options and index_relic != "0":
                    print("Invalid input. Try again.")
               elif index_relic != 0 and index_relic in options:
                    chosen_relic = relics[int(index_relic) - 1]
                    used_relics.append(chosen_relic)
                    relics.remove(chosen_relic)
                    specific_relic = True
                    while specific_relic:
                        #####################################
                        if chosen_relic == "A♥":
                         heart_chosen_relic = input(f"You used the {color_card('A♥')} relic. Which relic do you want to recover {' / '.join(get_colored_set(used_relics))}? ({'/'.join( [str(i) for i in range(1, len(used_relics) + 1)] + ['0'])}): " )
                         if heart_chosen_relic not in [str(i) for i in range(1, len(used_relics) + 1)] and heart_chosen_relic != "0":
                            print("Invalid input. Try again.")
                         elif heart_chosen_relic in [str(i) for i in range(1, len(used_relics) + 1)]:
                            recovered_relic = used_relics[int(heart_chosen_relic) - 1]
                            relics.append(recovered_relic)
                            used_relics.remove(recovered_relic)
                            print(f"You recovered the {color_card(recovered_relic)} relic.")
                            specific_relic = False
                         elif heart_chosen_relic == "0":
                            relics.append(chosen_relic)
                            used_relics.remove(chosen_relic)
                            print("You decide not to recover a relic.")
                            specific_relic = False
                            ##################################
                        elif chosen_relic == "A♠":
                          if is_number(temple[0]):
                            print(f"You used the {color_card(chosen_relic)} relic. You can collect/active the {number(temple[0])} next face-up number/event cards in the dungeon.")
                            counter = number(temple[0])
                            while counter > 0:
                               if temple[counter-1][1] != "H" and is_number(temple[counter-1]):
                                print(f"You collected the card {color_card(temple[counter-1][0])} and add it to your inventory.")
                                inventory.append(temple[counter-1][0])
                                temple.pop(counter-1)
                                for s in suits:
                                  if s not in mastered_suits:
                                    in_inv = sum(1 for item in inventory if item.endswith(s))
                                    has_ace = f"A{s}" in relics or f"A{s}" in used_relics
                                    
                                    if in_inv == 9 and has_ace:
                                        mastered_suits.append(s)
                                        print(f"\n SUIT BLESSING: {s} ")
                                        print(f"You have collected every card of the {s} suit. You have been honored by the Royal house of {name(s)}")
                                        for item in temple:
                                            if item[0].endswith(s) and trap(item):
                                                print(f"All {s} statues in the dungeon won't attack you...for now")
                               elif temple[counter-1][0] == "Exit" or temple[counter-1][0] == "Campfire" and temple[counter-1][1] != "H":
                                    if temple[counter-1][0] == "Exit":
                                        escape = True
                                        print("You found an exit!")
                                        game_active = False
                                    if temple[counter-1][0] == "Campfire":
                                        if len(used_relics) == 0:
                                         print("You found a campfire. You can use it to recover 2 relics, but you have no relics to recover.")
                                        elif len(used_relics) > 0:
                                            print("You found a campfire. You can use it to recover 2 relics.")
                                            choose_relics = True
                                            while choose_relics:
                                                counter_b = 2
                                                relic_options = range(1, len(used_relics) + 1)
                                                prompt_relics = " / ".join(used_relics)
                                                used_relics_input = input(f"You used {prompt_relics}. Which relic do you want to recover? ({'/'.join([str(i) for i in relic_options] + ['0'])}): ")
                                                if used_relics_input not in [str(i) for i in relic_options] and used_relics_input != "0":
                                                    print("Invalid input. Try again.")
                                                elif used_relics_input == "0":
                                                    print("You decide not to recover any relics.")
                                                    choose_relics = False
                                                else:
                                                    chosen_relic = used_relics[int(used_relics_input) - 1]
                                                    relics.append(chosen_relic)
                                                    used_relics.remove(chosen_relic)
                                                    counter_b -= 1
                                                    if counter_b == 1:
                                                     print(f"You recovered the {color_card(chosen_relic)} relic. You can recover {counter_b} more relic(s).")
                                                    elif counter_b == 0:
                                                     print(f"You recovered the {color_card(chosen_relic)} relic. You have recovered all your relics for now.")
                                                     choose_relics = False
                               elif temple[counter-1][0][0] == "A" and temple[counter-1][1] != "H":
                                print(f"You found a relic ({color_card(temple[counter-1][0])})!")
                                relics.append(temple[counter-1][0])
                                temple.pop(counter-1)
                               counter -= 1
                            map(temple)
                            specific_relic = False
                            ####################################
                        elif chosen_relic == "A♦":
                         if len(backpack) == 3:
                            print("Your backpack is full. You can only have 3 cards in your backpack at a time.")
                         elif len(backpack) < 3:   
                           diamond_chosen_relic = input(f"You used the {color_card(chosen_relic)} relic. Which card do you want to recover from your inventory? {' / '.join(get_colored_set(inventory))}? ({'/'.join( [str(i) for i in range(1, len(backpack) + 1)] + ['0'])}): " )
                           if diamond_chosen_relic not in [str(i) for i in range(1, len(inventory) + 1)] and diamond_chosen_relic != "0":
                             print("Invalid input. Try again.")
                           elif diamond_chosen_relic in [str(i) for i in range(1, len(inventory) + 1)]:
                             recovered_card = inventory[int(diamond_chosen_relic) - 1]
                             backpack.append(recovered_card)
                             inventory.remove(recovered_card)
                             print(f"You recovered the {color_card(recovered_card)} card and placed it in your backpack.")
                             specific_relic = False
                           elif diamond_chosen_relic == "0":
                             relics.append(chosen_relic)
                             used_relics.remove(chosen_relic)
                             print("You decide not to recover a card.")
                             specific_relic = False
                           #########################################  
                        elif chosen_relic == "A♣":
                          if temple[0][1] != "H" and trap(temple[0]):
                            print(f"You used the {color_card(chosen_relic)} relic. The statue {color_card(temple[0][0])} at the front of the dungeon is now removed.")
                            temple.pop(0)
                          else:
                            print(f"You used the {color_card(chosen_relic)} relic. However, there is no statue at the front of the dungeon to blow away.")
                            used_relics.remove(chosen_relic)
                            relics.append(chosen_relic)
                          map(temple)
                          specific_relic = False
                    using_relics = False
                    ################################################
               elif index_relic == "0":
                    print("You decide not to use a relic.")
                    using_relics = False
        if action == 'ch':
           print(f"Inventory has {len(inventory)} cards: [{',' .join(get_colored_set(inventory))}]")
           print(f"Backpack: [{',' .join(get_colored_set(backpack))}], Relics: [{',' .join(get_colored_set(relics))}], Used Relics: [{',' .join(get_colored_set(used_relics))}]")
           print(f"{color_card('♠')}:{sum(1 for item in inventory if item.endswith('♠')) + (1 if 'A♠' in relics or 'A♠' in used_relics else 0)}/10, {color_card('♥')}:{sum(1 for item in inventory if item.endswith('♥'))+(1 if 'A♥' in relics or 'A♥' in used_relics else 0)}/10, {color_card('♦')}:{sum(1 for item in inventory if item.endswith('♦'))+(1 if 'A♦' in relics or 'A♦' in used_relics else 0)}/10, {color_card('♣')}:{sum(1 for item in inventory if item.endswith('♣'))+(1 if 'A♣' in relics or 'A♣' in used_relics else 0)}/10")
           print(f"There are {sum(1 for item in temple if is_hidden(item))} hidden cards ({sum(1 for item in temple if is_hiddenface(item))} face cards) in the dungeon. The chance of the next card being an enemy is {sum(1 for item in temple if is_hiddenface(item))/sum(1 for item in temple if is_hidden(item))*100:.2f}%.")
           map(temple)
        if action == "help":
            print("You're a dungeon crawler trying to collect the four prestigious relics to pay off your crime. The deeper you go, the darker it gets.")
            print("Can you find the exit before the shadows find you...?")
            print()
            print("How to play?")
            print("=== Commands ===")
            print("l: Look at the first one or two cards in the dungeon. But you can only look at the second card if the first card is still hidden.")
            print("e: Explore by jumping forward based on the number on the card. You can only explore if the first or second card is a number. If you land on face-up cards, you will trigger that card.")
            print("c: Collect a revealed number card and put it in your backpack. You can only collect the first card in the dungeon and your backpack can only hold 3 cards.")
            print("b: Use a card from your backpack and place it back on top of the dungeon.")
            print("r: Use a relic from your inventory. Each relic has a different effect.")
            print("ch: Check your inventory, backpack, relics, and some stats about the dungeon.")
            print("exit: Give up the current run.")
            print("help: View the list of commands and how to play the game.")
            print()
            print("=== Relic Effects ===")
            print(f"{color_card('A♠')}: A spear. Based on the number on the top card, you can collect the corresponding number of number cards and even trigger the event cards.")
            print(f"{color_card('A♥')}: A totem. Saves you from a battle with an enemy card or you can use it to recover a used relic.")
            print(f"{color_card('A♦')}: A knapsack. Allows you to take a card from your inventory to your backpack if you have space.")
            print(f"{color_card('A♣')}: A fan. Blows an enemy away from the dungeon.")
            print()
            print("=== Event cards ===")
            print("Exit: Exit card. If you hit this card and it's revealed, you escape from the dungeon!")
            print("Campfire: Campfire card. If you hit this card and it's revealed, you can choose to recover 2 relics if you have any used relics.")
            print("During the proccess of the game, if you collect all 10 cards of a suit and have the relic of that suit, you will be blessed by that suit.")
            print("Blessing of a suit means all face-up face cards of that suit in the dungeon will be face-down.")
            print()
            print("=== Scoring ===")
            print("Your score is based on the number of cards in your inventory, the number of relics you have (including used relics), and the number of complete suits you have collected.")
            print("To pardon yourself, you need to find the exit card and escape the dungeon with 4 prestigious relics.")
            print("Your final score will be revealed after you escape. If you lose before escaping, your score will be none.")
            print("Good luck on your adventure!")
            print("===================================")
            print()
            print("Version: 1.5")
            print("Credits: This game was created by fatlock1712 with a huge inspiration from the Loot the Loop game.")
            print("It was made for a coding project and is not affiliated with the original game or its creators.")
            #########################
        if action == "cheat":
           inventory = [f"{rank}{suit}" for suit in suits for rank in [2,3,4,5,6,7,8,9,10]]
           relics = [f"A{suit}" for suit in suits]
           escape = True
           game_active = False
        if action == "exit":
            game_active = False
    if escape:
      for _ in suits:
        if sum(1 for item in deck if item.endswith(_)) == 13:
            suit_counter += 1
      score = len(inventory)*(1+len(relics)+len(used_relics))*(1+suit_counter)
      print(f"[{',' .join(get_colored_set(inventory))}]")
      print(f"[{', '.join(get_colored_set(relics + used_relics))}]")
      if(len(relics) + len(used_relics)) in [2, 3]: #2,3 relics you have no choice but to fight the King for your life.
       print(f"You escaped with {len(relics) + len(used_relics)} relics. With that feat, you had a chance to granted an audience with the King" )
       boss_fight = True
      elif(len(relics) + len(used_relics)) == 4:
       print(f"You escaped with all 4 relics! With that feat, you had a chance to be granted an audience with the King.")
       boss_fight = True
      elif(len(relics) + len(used_relics)) == 0:
       print(f"You barely escaped and didn't want to risk your life anymore. With no relics and few cards, you had nothing to offer the Royal army when you got out.")
       print(f"You had to pay for your death sentence." )
      elif (len(relics) + len(used_relics)) == 1:
       print(f"You escaped with only 1 relic. You barely made it out alive and your relic was taken by the Royal army. Your death sentence was reduced into a life sentence and every treasure you found is now the King's.")
       print("You lived the rest of your days as a prisoner, telling tales about the dungeon you escaped from." )
       print(f"Your score is based on the number of cards in your inventory, the number of relics you have (including used relics), and the number of complete suits you have collected. Your final score is {score}.")
    elif not escape:
      print("You got lost in the dungeon forever. The shadows eat you alive and drive you into madness. You will never escape...")
      print("Is this the karma of your crimes? Or is it just the fate of a dungeon crawler? Who knows...")
    while boss_fight:
       print("After a long journey, you are granted an audience with the king upon his throne. He asked you to give all your relics; in return, your crime will be pardoned, and you will be exiled from the kingdom.")
       fight_or_not = input("What is your choice here? accept/deny/coin flip? (a/d/c)").lower()
       if fight_or_not == "c":
        print("You let the God of luck decide your fate by a coin flip. Is it a wise choice? Who knows...")
        r_choice = random.randint(0,1)
        if r_choice == 1:
           print("You tossed a coin and it's... HEAD")
           fight_or_not = "a"
        elif r_choice == 0:
           print("You tossed a coin and it's... TAIL")
           fight_or_not = "d"
       if fight_or_not == "d" and (len(inventory) + len(backpack) == 0):
        print("You want to challenge the King and make him pay for what he has done to you!")
        print("However, you don't have any cards in your inventory or backpack. The King wonders how you could escape from the dungeon with the relics.")
        print("You fight him with your bare hands, but you were quickly defeated...")
        boss_fight = False 
       elif fight_or_not == "d" and (len(inventory) + len(backpack) > 0):
        print("You denied the King's offer. You decided to make him pay for what he has done to you!")
        print("The almighty King revealed his secret powers! His sceptre and sword are actually the two missing Joker cards.")
        print("His sceptre summoned a mirror image of you to fight against you. The mirror image has the same inventory, backpack as yours.")
        print("His sword isn't a normal one, your feelings say, and he even joined the fight?!?")
        print("This isn't a fair fight, but you have come this far. You have to fight for your life and the freedom you just got a taste of.")
        print("KING and MIRROR")
        king_health = 30
        mirror_health = 50
        your_health = 50
        deck_fight = inventory + backpack
        relic_fight = relics + used_relics
        turn = True
        turn_count = 0
        buff_greed = 10
        buff_health = 0
        buff_speed = 10
        buff_str =  10
        heart_relic = 1
        barehand = False
        once = False
        fan_cooldown = 0
        special_atk = 0
        allow_relic = 1
        mirror_died = False
        king_died = False
        relic_fight_copy = relic_fight.copy()
        copy_deck = deck_fight.copy()
        mirror_blow_away_counter = 0
        king_blow_away_counter = 0
        for r in backpack:
           if r[-1] == "♠":
              buff_str += 2*int(r[:-1])
           elif r[-1] == "♥":
              buff_health += 2*int(r[:-1])
           elif r[-1] == "♦":
              buff_greed += 2*int(r[:-1])
           elif r[-1] == "♣":
              buff_speed += 2*int(r[:-1])
        buff = [[buff_health,'health'], [buff_greed-10,'greed'], [buff_speed-10,'speed'], [buff_str-10,'strength']]
        ken = [f"+{val} {name}" for val, name in buff if val > 0]
        if(len(backpack) > 0):
         print(f"Since you have [{', '.join(get_colored_set(backpack))}] in your back pack, you received its blessing: {', '.join(ken)}")
        your_health += buff_health
        while turn:
         while True:
                fight_choose = input(f"Turn {turn_count}, what is your choice? fight/relic/check? (f/r/ch): ")
                if(fight_choose == "r"):
                    if len(relics) == 0:
                     print("You have no relics to use.")
                    if allow_relic == 0:
                       print("Relics can only be activated once per turn.") 
                    if (allow_relic == 1): 
                     using_relics = True
                     while using_relics:
                            options = [str(i) for i in range(1, len(relic_fight) + 1)]
                            if fan_cooldown > 0 and "A♣" in relic_fight:
                               relic_fight.remove("A♣")
                            if fan_cooldown == 0 and "A♣" not in relic_fight and "A♣" in relic_fight_copy:
                               relic_fight.append("A♣")   
                            prompt_relics = " / ".join(get_colored_set(relic_fight))
                            index_relic = input(f"You have the following relics: {prompt_relics}. Which relic do you want to use? ({'/'.join(options)}/0): ") 
                            if index_relic not in options and index_relic != "0":
                                    print("Invalid input. Try again.")
                            elif index_relic == "0":
                                    print("You decide not to use a relic.")
                                    using_relics = False
                            elif index_relic != "0" and index_relic in options:
                                    chosen_relic = relics[int(index_relic) - 1]
                                    specific_relic = True
                                    while specific_relic:
                                        if chosen_relic == "A♥" and heart_relic == 1:
                                           bai_random = random.choice(deck_fight)
                                           your_health += int(bai_random[:-1])
                                           print(f"You used the relic and healed yourself {int(bai_random[:-1])} HP.")
                                           allow_relic = 0
                                           specific_relic = False
                                           using_relics = False
                                        elif chosen_relic == "A♦":
                                           #make a copy
                                           if len(inventory) == 0:
                                            print("You have no cards in your inventory to recover.")
                                           else:
                                                which_card = input(f"You used the relic. Which card do you want to duplicate from your inventory? [{', '.join(get_colored_set(deck_fight))}]? ({'/'.join( [str(i) for i in range(1, len(inventory) + 1)])}): " )
                                                if which_card not in [str(i) for i in range(1, len(inventory) + 1)]:
                                                   print("Invalid input. Try again.")
                                                else:
                                                    chosen_card = inventory[int(which_card) - 1]
                                                    deck_fight.append(chosen_card)
                                                    print(f"You duplicated the {color_card(chosen_card)} card and added it to your deck for this fight.")
                                           allow_relic = 0
                                           specific_relic = False
                                           using_relics = False
                                        elif chosen_relic == "A♠":
                                       
                                           special_atk = 1
                                           allow_relic = 0
                                           print(f"Your next attack will be enchanced.")
                                           specific_relic = False
                                           using_relics = False
                                        elif chosen_relic == "A♣":
                                         
                                           fan_cooldown = 2
                                           blow_who = []
                                           if mirror_health > 0:
                                               blow_who.append("MIRROR")
                                           if king_health > 0:
                                               blow_who.append("KING")
                                           blow_options = [str(i) for i in range(1, len(blow_who) + 1)]
                                           if True:
                                               who_blow_away = input(f"Who do you want to blow away ({'/'.join(blow_who)})? ({'/'.join(blow_options)}): ")
                                               if who_blow_away not in blow_options:
                                                   print("Invalid input. Try again.")
                                               elif who_blow_away == "1" and blow_who[0] == "MIRROR":
                                                   print(f"You blew away the MIRROR! It won't be able to attack you for the next turn.")
                                                   mirror_blow_away_counter = 1
                            
                                               elif who_blow_away == "2" or (who_blow_away == "1" and blow_who[0] == "KING"):
                                                    print(f"You blew away the KING! It won't be able to attack you for the next turn.")
                                                    king_blow_away_counter = 1
                            
                                           allow_relic = 0
                                           specific_relic = False
                                           using_relics = False

                                       
                            
                elif(fight_choose == "f"):
                    turn_count += 1
                    allow_relic = 1
                    fan_cooldown = max(0, fan_cooldown - 1)
                    you_draw = random.choice(deck_fight)
                    if barehand == False:
                        print(f"You draw and reveal {color_card(you_draw)}")
                        time.sleep(0.7)
                        if(buff_greed > 0 and random.random() < buff_greed/100):
                            new_draw = random.choice(deck_fight)
                            print(f"Your greed gets the better of you! You draw again and reveal {color_card(new_draw)}")
                            time.sleep(0.5)
                            if(int(new_draw[:-1]) <= int(you_draw[:-1])):
                                print(f"You choose {color_card(you_draw)}")
                            else:
                                print(f"You choose {color_card(new_draw)}")
                                you_draw = new_draw
                    if barehand == True and once == False:
                        you_draw = "1♣"
                        print("You have no cards to fight with, so you fought the battle with your bare hands. Your attack is weak as a result.")
                        once = True 
                    if mirror_health > 0:
                        mirror_draw = random.choice(copy_deck)
                        print(f"MIRROR draw and reveal {color_card(mirror_draw)}")
                        time.sleep(0.5)
                    if king_health > 0:    
                        king_draw = random.randint(1,6)
                        print(f"KING roll the dice and get a {king_draw}")
                        time.sleep(0.5)
                    if(special_atk == 1):
                       print("You're waiting for the perfect moment to use your special attack...")
                       time.sleep(0.3)
                       if king_health > 0:
                        print("The KING attacks you.")
                        your_health -= king_draw
                       if mirror_health > 0:
                        print("The MIRROR attacks you.")
                        your_health -= int(mirror_draw[:-1])    
                       print(f"Your health is now {your_health if your_health > 0 else 0}")
                       if heart_relic == 1 and your_health <= 0:
                            print("Your heart relic saves you from death! You are revived with 20 HP, but the relic is now used up.")
                            your_health = 20
                            heart_relic = 0
                            relic_fight.remove("A♥")
                       elif your_health <= 0:
                               print("You failed to catch the right moment. You have been defeated by the KING and MIRROR...")
                               turn = False
                               boss_fight = False
                               victory = 1
                    if(int(you_draw[:-1]) < king_draw and king_health > 0 and special_atk == 0):
                        if king_blow_away_counter > 0:
                            print(f"The KING is blown away and can't attack you this turn!")
                            king_blow_away_counter -= 1
                            continue
                        print("The KING attacks you.")
                        your_health -= king_draw
                        time.sleep(0.5)
                        if random.random() < buff_speed/100:
                         print("Fortunately, you dodged the KING's attack!")
                         your_health += king_draw
                         time.sleep(0.5)
                        print(f"Your health is now {your_health if your_health > 0 else 0}")
                        if heart_relic == 1 and your_health <= 0:
                            print("Your heart relic saves you from death! You are revived with 20 HP, but the relic is now used up.")
                            your_health = 20
                            heart_relic = 0
                            relic_fight.remove("A♥")
                        elif your_health <= 0:
                               print("You have been defeated by the KING and MIRROR...")
                               turn = False
                               boss_fight = False
                               victory = 1
                    if(int(you_draw[:-1]) < int(mirror_draw[:-1]) and mirror_health > 0 and special_atk == 0):
                        if mirror_blow_away_counter > 0:
                            print(f"The MIRROR is blown away and can't attack you this turn!")
                            mirror_blow_away_counter -= 1
                            continue
                        print("The MIRROR attacks you.")
                        your_health -= int(mirror_draw[:-1])
                        time.sleep(0.5)
                        if random.random() < buff_speed/100:
                         print("Fortunately, you dodged the MIRROR's attack!")
                         your_health += int(mirror_draw[:-1])
                         time.sleep(0.5)
                        print(f"Your health is now {your_health if your_health > 0 else 0}")
                        if heart_relic == 1 and your_health <= 0:
                            print("Your heart relic saves you from death! You are revived with 20 HP, but the relic is now used up.")
                            your_health = 20
                            heart_relic = 0
                            relic_fight.remove("A♥")
                        elif your_health <= 0:
                               print("You have been defeated by the KING and MIRROR...")
                               turn = False
                               boss_fight = False
                               victory = 1
                    if(special_atk == 0):
                       choose_who_to_attack = True
                       who_attack = []
                       bua = 1
                       if int(you_draw[:-1]) >= int(mirror_draw[:-1]) and mirror_health > 0 and mirror_blow_away_counter == 0:
                           who_attack.append(f"MIRROR")
                       if int(you_draw[:-1]) >= king_draw and king_health > 0 and king_blow_away_counter == 0:
                          who_attack.append(f"KING")
                       options = [str(i) for i in range(1, len(who_attack) + 1)]
                       if len(who_attack) > 0:
                        while choose_who_to_attack:
                          attack_who = input(f"Who do you want attack {'/'.join(who_attack)}? ({'/'.join(options)}): ")
                          if attack_who not in options:
                            print("Invalid input. Try again.")
                          elif attack_who == "1" and who_attack[0] == f"MIRROR":
                            print(f"You attacked the MIRROR!")
                            if random.random() < buff_str/100:
                                time.sleep(0.5)
                                print("It's a critical hit! Your attack deals double damage!")
                                bua = 2
                            mirror_health -= bua*int(you_draw[:-1])
                            print(f"The mirror image's health is now {mirror_health if mirror_health > 0 else 0}")
                            choose_who_to_attack = False
                          elif attack_who == "2" or (attack_who == "1" and who_attack[0] == f"KING"):
                            print(f"You attacked the KING, but he blocked your attack. However, the KING suffered {int(you_draw[:-1]) - king_draw} damage from the impact!")
                            king_health -= int(you_draw[:-1]) - king_draw
                            print(f"The KING's health is now {king_health if king_health > 0 else 0}")
                            if random.random() < 0.5:
                             time.sleep(1)
                             print("Your weapon got destroyed by the KING's sword during the fight.")
                             deck_fight.remove(you_draw)
                             if len(deck_fight) == 0 and barehand == False:
                              time.sleep(1)
                              print("You have no more cards to fight with. You fought the battle with your bare hands...")
                              barehand = True
                            choose_who_to_attack = False
                    if(special_atk == 1):
                        bua = 1
                        print("Your attack hits both the KING and the MIRROR!")
                        if random.random() < buff_str/100:
                         time.sleep(0.5)
                         print("It's a critical hit! Your attack deals double damage!")
                         bua = 2
                        king_health -= bua*int(you_draw[:-1])
                        mirror_health -= bua*int(you_draw[:-1])
                        print(f"The KING's health is now {king_health if king_health > 0 else 0}")
                        print(f"The MIRROR's health is now {mirror_health if mirror_health > 0 else 0}")
                        special_atk = 0
                    king_blow_away_counter = max(0, king_blow_away_counter - 1)
                    mirror_blow_away_counter = max(0, mirror_blow_away_counter - 1)
                    if(king_health <= 0 and mirror_health > 0 and not king_died):
                       print(f"Against all odds, you defeated the KING but you still have another enemy to defeat.")
                       king_died = True
                    if(mirror_health <= 0 and king_health > 0) and not mirror_died:
                       print(f"You defeated the MIRROR, but the KING is still standing strong.")
                       mirror_died = True
                    if(king_health <= 0 and mirror_health <= 0):
                       print(f"You won the fight! Using his scepter, you created a mirror image of the KING and now you controlled the whole kingdom in the darkness.")
                       print(f"Shorty after your victory, you got pardoned by the puppet King and no ones dared to question about his decision anymore. You lived the rest of your days as a shadow ruler.")
                       boss_fight = False
                       turn = False
                       victory = 2
                       break


                elif(fight_choose == "ch"):
                   print(your_health)
                   print(f"Dexterity: {buff_speed}, Greed: {buff_greed}, Strength: {buff_str}")
                   print(f"KING's health: {king_health}")
                   print(f"MIRROR's health: {mirror_health}")
                   print(f"Relics: [{', '.join(get_colored_set(relic_fight))}]")
                   print(f"Deck: [{', '.join(get_colored_set(deck_fight))}]")
                elif(fight_choose == "help"):
                   print("Greed: Chance to draw 2 cards at the start of your turn.")
                   print("Speed: Chance to dodge an attack.")
                   print("Strength: Chance to deal double damage.")
                   print("Dexterity: Increase your health.")
                   print("Relics can only be used once per turn. You can choose to use a relic or fight first during your turn.")
                   print(f"{color_card('A♠')}: Enchances your next attack and hit both enemies.")
                   print(f"{color_card('A♥')}: Heals yourself an ammount equal to the value of the card drawn from your deck. It also can revive you from death once.")
                   print(f"{color_card('A♦')}: Create a duplicate of a card from your deck.")
                   print(f"{color_card('A♣')}: Blows an enemy away from the fight for a short time. But you can't attack the enemy that was blown away. This relic has a cooldown of 2 turns.")                
         
       elif fight_or_not == "a":
        print("After near-death experiences, you always dream for a peaceful life. Accepted the King's offer, you moved to isolated village and told tales about the dungeon you escaped from.")
        if (len(relics) + len(used_relics)) < 4:
         print(f"However, the hunt for the last {4 - (len(relics) + len(used_relics))} {'relics' if 4 - (len(relics) + len(used_relics)) != 1 else 'relic'} must be continued, more and more death sentence prisoners are sent to the dungeon.")
        print(f"Your score is based on the number of cards in your inventory, the number of relics you have (including used relics), and the number of complete suits you have collected. Your final score is {score}.")
        boss_fight = False
       elif fight_or_not not in ["a","d","c"]:
          print("Invalid input. Try again.")

    if escape and victory in [1,2]:
       if victory == 1:
        print(f"Is it the karma of your crimes? Or is it just the fate of a dungeon crawler? Who knows... Your final score is none.")
       if victory == 2:
        print(f"You defeated the KING. No numbers can describe your victory. Your final score is 999.")
           
    while True:  
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            play()
            break       
        elif play_again == "n":
            print("Thanks for playing!")
            time.sleep(2)
            playing = False
            sys.exit()
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    play()