from random import randrange 
 
 
def get_user_weapon(): 
    print("SELECT YOUR WEAPON (1-3)") 
    print("-----------------------") 
    print("1. Rock") 
    print("2. Paper") 
    print("3. Scissors") 
 
    choice = input("Enter your Weapon: ").lower() 
 
    if choice == "rock" or choice == "1": 
        return 1 
    elif choice == "paper" or choice == "2": 
        return 2 
    elif choice == "scissors" or choice == "3": 
        return 3 
 
 
def get_opponent_weapon(): 
    opponent_weapon = randrange(1, 4) 
    return opponent_weapon 
 
 
def determine_winner(user_weapon, opponent_weapon): 
    if user_weapon == opponent_weapon: 
        print("It's a tie!") 
    elif user_weapon == 1 and opponent_weapon == 3: 
        print("You win, rock crushes scissors!") 
    elif user_weapon == 2 and opponent_weapon == 1: 
        print("You win, paper covers rock!") 
    elif user_weapon == 3 and opponent_weapon == 2: 
        print("You win, scissors cuts paper!") 
    elif opponent_weapon == 1 and user_weapon == 3: 
        print("You lose, rock crushes scissors!") 
    elif opponent_weapon == 2 and user_weapon == 1: 
        print("You lose, paper covers rock!") 
    elif opponent_weapon == 3 and user_weapon == 2: 
        print("You lose, scissors cuts paper!") 
 
 
def main(): 
    continue_playing = "y" 
 
    while continue_playing == "y": 
        user_weapon = get_user_weapon() 
        opponent_weapon = get_opponent_weapon() 
        determine_winner(user_weapon, opponent_weapon) 
        continue_playing = input("Want to play again (y/n): ").lower() 
 
    print("Completed by, Brock Harrison") 
    input("Press Enter to close...") 
 
 
if __name__ == "__main__": 
    main() 
