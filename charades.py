# Modules:
import random

# Global variables:

# strings:
game = "Charades"
user_ask_start = "Shall we begin (y/n)?"
user_welcome = "Welcome Players!"
user_ask_version_of_game = "Please select from the following list the version of" 
user_ask_game_type = user_ask_version_of_game + game

# lists:
charades_version_list = ['PG', 'R-RATED']
playerList = []

# Welcoming user and listing version of Charades user wants to play.
print(f"\n{user_welcome} \n\n{user_ask_version_of_game} {game} you would like to play by inputing the number associated with your choice.\n")
for i in charades_version_list:
     print(charades_version_list.index(i) +1, end=" ")
     print(" ", i)

# Choice outcome.
answer = (input("\nWhats it going to be?:"))
if answer == "1":
     print("\nGood Choice,", charades_version_list[0]," it is!")
elif answer == "2":
     print("\nAwesome!", charades_version_list[1]," it is!")


user_ask_start = (input("\nAre you ready (y/n)?"))


# Player answers y to begin playing:
if user_ask_start == "y":
    userNun=int(input("\n Number of players?\n> "))
    while len(playerList) != userNun:
        userNames=input(f"Please input name of player {len(playerList)+1}/{userNun} :\n")
        playerList.append(userNames)

# Player answers n to begin game:
elif user_ask_start == "n":
    print("\n\n Goodbye \n")
    exit()

# Player enters other input:   
else:
     print("\n Want to try that again? I've got all day.\n")
     exit()

    

# print("\nIt's your turn:" , random.choice(playerList))
playerIndex = 0
while True:
    WORDS = ["airplane", "boat", "baby", "Phone", "Toothbrush", "Hammer", "Shoelaces", "Flashlight", "Clown", "Mime", "Whale", "Kangaroo", "Monkey", "Rooster", "Cockroach", "Bartender", "Cow", "Bullfighter", "Yard sale", "Penguin"]
    PHRASES = ["Willy Wonka", "Buzz Lightyear", "Rod Stewart", "Lady Gaga", "Britney Spears", "Michael Jackson", "Doctor Evil"]
    word = random.choice(WORDS)
    correct = word
    jumble = ""
    
    print("\n", playerList[playerIndex], "It's your turn:") 
    print("\n The word / phrase to act out is:\n\n", word.title())
    
    guess = input("\n Who guessed this correctly? ")
    playerIndex = (playerIndex+1) % len(playerList)
    
    # print("\nWould you like to play again? Y or N")
    while True:
            answer = str(input('\nWould you like to play again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break



input("\n\nPress the enter key to exit")