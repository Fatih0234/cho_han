import random, sys

entry_message = """Welcome to cho(even)-han(odd) game, this version of this game is dealt with two players.
In the beginning of the game, dealer decides the first starter of the game with head or tails game.
As you might guess, starting first decides the other player's guess automatically.
Because when we say even, other player should say odd in order to compete. 
In this game, dealer cuts 10 percent of the income earned out of per round.
Not => Who wins in the current round will start first next round.
"""

player1_name = input("What is your name?, Player1: ")
player2_name = input("What is your name?  Player2: ")

players = {player1_name: {"purse":5000
                            },
           player2_name: {"purse":5000}}
player1_purse = players[player1_name]["purse"]
player2_purse = players[player2_name]["purse"]


JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                     4: 'SHI', 5: 'GO', 6: 'ROKU'}

print(f"Player_1 = {player1_name}")
print(f"Player_2 = {player2_name}")


# Who will start first? 
print("In order to decide who will start first, we will play heads or tails.")
while True:
    print(f"Head or tail? {player1_name}")
    player1 = input("> ").upper()
    print(f"Head or tail?, {player2_name}")
    player2 = input("> ").upper()
    if player1 not in ["HEAD", "TAIL"] or player2 not in ["HEAD", "TAIL"]:
        print("Type either tail or head")
        continue
    else:
        break


head_tail = random.choice(["head","tail"])

if player1 == head_tail:
    print(f"Congrats player1: {player1_name} guessed it right, You have the right to go first in the game.")
    starter= player1_name
    other = player2_name
else:
    print(f"Congrats player2: {player2_name} guessed it right, You have the right to go first.")
    starter = player2_name
    other = player1_name


def main():
    global starter, other, players
    while True:
        # Take the amount that will be bet.
        while True:
            print(f"How much are you guys willing to put? or (QUIT)?")
            print(f"Player1 {player1_name} purse: ", players[player1_name]["purse"])  
            print(f"Player2 {player2_name} purse: ", players[player2_name]["purse"])  
            mutual_bet = input("> ").upper()

            if mutual_bet == "QUIT":
                print("Thanks for playing")
                sys.exit()
            elif not mutual_bet.isdecimal():
                print("Please type a number")
                continue
            elif int(mutual_bet) > players[player1_name]["purse"] or int(mutual_bet) > players[player2_name]["purse"]:
                print("Guys one of you or both of you exceeding your budget, please type a valid amount.")
                continue
            else:
                mutual_bet = int(mutual_bet)
                break
        
        print('The dealer swirls the cup and you hear the rattle of dice.')
        print('The dealer slams the cup on the floor, still covering the')
        print('dice and asks for your bet.')
        print()
        print('    CHO (even) or HAN (odd)?')

        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        sum_even = (dice1 + dice2) % 2 == 0
        
        if sum_even:
            correct_ans = "CHO"
        else:
            correct_ans = "HAN"

        while True:
            # print(f"This round, {starter} goes first! Good luck people !!!!")
            
            guess_made = ""

            if starter == player1_name:
                print(f"Player1: {player1_name}, you are starting first; what's your guess? cho(even) or han(odd)?")
                guess_made = input("> ").upper()
            else:
                print(f"Player2: {player2_name}, you are starting first; what's your guess? cho(even) or han(odd)?")
                guess_made = input("> ").upper()
            
            if guess_made not in ["CHO", "HAN"]:
                print(f"Pleas type a correct value  {starter}")
                continue
            else:
                break
        print(f"  {JAPANESE_NUMBERS[dice1]} - {JAPANESE_NUMBERS[dice2]} ")
        print(f"   {dice1} - {dice2}")
        
        if correct_ans == guess_made:
            
            print(f"Congrats! {starter}, That was correct. You won against {other}")
            print(f"Dealer cuts 10 percen fee, {0.1*mutual_bet}, {starter} wins {0.9*mutual_bet}")
            print(f"Because you won this round, you will keep making the first guess next round as well.")

            players[other]["purse"] -= mutual_bet
            
            mutual_bet = 0.9*mutual_bet

            players[starter]["purse"] += mutual_bet
            
        else:
            

            print(f"That was wrong. You lost against {other}.")
            print(f"Dealer cuts 10 percent fee, {0.1*mutual_bet}, {other} wins {0.9*mutual_bet}.")
            print(f"Next round {other} will be making the first guess:")
            players[starter]["purse"] -= mutual_bet
            mutual_bet = 0.9*mutual_bet

            players[other]["purse"] += mutual_bet
            
            starter, other = other, starter

        if players[player1_name]["purse"] == 0:
            print(f"Player1: {player1_name}, You ran out of monney!")
            sys.exit()
        elif players[player2_name]["purse"] == 0:
            print(f"Player2: {player2_name}, You ran out of monney!")
            sys.exit()
            
        else:
            print("Press space in order to continue")
            input(">>> ")


if __name__ == "__main__":
    main()



        

    













