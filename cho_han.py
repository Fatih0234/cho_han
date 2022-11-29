import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                     4: 'SHI', 5: 'GO', 6: 'ROKU'}
entry_text = """This is a game called cho(even) or han(odd). Two-6 sided dices are thrown and
player try to guess the sum of two dice results whether it is even or odd. """

print(entry_text)

def main():

    
    purse = 6000

    while True: # Main game loop.
        # get a bet from user

        bet = input(f"How much do you want to bet out of {purse}(or QUIT) > ")
        if bet.upper() == "QUIT":
            print("Thanks for playing, though!")
            sys.exit()
        elif int(bet) > purse:
            print(f"Type a number that is suitable to your budget. Your budget: {purse}")
            continue
        elif not bet.isdecimal():
            print("Type a valid number")
            continue
        else: # Finally they put in a valid number.
            bet = int(bet)

        # Get the player's guess.

        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("Dices are rolled up, What is your guess? cho(even) or hon(odd)?")

        while True:

            guess = input("> ").upper()
            if guess != "CHO" and guess != "HAN":
                print("Please type eithe CHO or HAN.")
                continue
            else:
                break 
        
        print(f" {JAPANESE_NUMBERS[dice1]}  -  {JAPANESE_NUMBERS[dice2]} ")
        print(f" {dice1}  -  {dice2} ")

        result_even = (dice1 + dice2) % 2 == 0

        if result_even:
            correct_bet = "CHO"
        else:
            correct_bet = "HAN"
        
        if guess == correct_bet:
            print("Congrats, You won!")
            purse += bet
        else:
            print("You lost!")
            purse -= bet
        
        if purse == 0:
            print("You ran out of money, But hey,")
            print("The good news is that you didin't play with real money.")
            sys.exit()
            

        
        
if __name__ == "__main__":
    main()



