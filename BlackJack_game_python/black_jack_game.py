import random
from os import system, name 
from logos import logo1, logo3
# The deck is unlimited. Jack, Queen, King all count as 10. Ace may count as 11 or 1.
# Cards are not removed from the deck as they are drawn.
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')

def deal_cards():
    chosen_card= int(random.choice(cards))
    return chosen_card

def calc_score(card_set):
    if sum(card_set)==21 and len(card_set)== 2:
        return 0
        # 0 indicates blackjack
    if 11 in card_set and sum(card_set) > 21:
        card_set.remove(11)
        card_set.append(1)
    return sum(card_set)

def compare(playerscore, compscore):
    if playerscore== compscore:
        return "Draw!!"
    elif compscore==0:
        return "you lose! computer has a BlackJack"    
    elif playerscore==0:
        return "You win with a BlackJack!" 
    elif playerscore > 21:
        return "You went over 21, you lose."
    elif compscore >21:
        return "Computer went over 21, you win."    
    elif playerscore> compscore:
        return "You win!"
    else:
        return "You lost. Computer wins!"        

def play_game():
    print(f"{logo3}")
    print(logo1)
    print("....................................................................................................")
    print("\n\n")

    player_cards  =[]
    comp_cards= []
    isGameOver = False

    for _ in range(2):
        player_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    # player_score= calc_score(player_cards)
    # comp_score= calc_score(comp_cards)

    while not isGameOver:
        player_score= calc_score(player_cards)
        comp_score= calc_score(comp_cards)

        print(f"Your cards: {player_cards}")
        print(f" Your Current Score: {player_score}")
        print(f"Computer's first card: [{comp_cards[0]}] ")
        print()

        if player_score==0 or comp_score==0 or player_score > 21:
            isGameOver = True
            break
        else:
            draw_again = input("Enter 'y' to Draw another card or 'n' to pass: ")    
            if draw_again == 'y':
                player_cards.append(deal_cards())
                # print(f"new card added= {player_cards[-1]}")
            else:
                isGameOver= True
                break   

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_cards())
        comp_score= calc_score(comp_cards)     

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print()
    print(compare(player_score, comp_score))
    if input("\n Do you want to play again? (y/n)")=='y':  
        clear() 
        play_game()    

play_game()        