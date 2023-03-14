import random

user_ask_start = "Shall we begin (y/n)?"

WORDS = ["airplane", "boat", "baby", "Phone", "Toothbrush", "Hammer", "Shoelaces", "Flashlight", "Clown", "Mime", "Whale", "Kangaroo", "Monkey", "Rooster", "Cockroach", "Bartender", "Cow", "Bullfighter", "Yard sale", "Penguin"]
charades_version_list = ['PG', 'Adult']
playerList = []

# Welcoming user and listing version of Charades user wants to play.
print("\nWelcome Players! \n\nPlease select from the following list the version of Charades you would like to play by inputing the number associated with your choice.\n")
for i in charades_version_list:
     print(charades_version_list.index(i) +1, end=" ")
     print(" ", i)

# Player choose outcom.
answer = (input("\nWhats it going to be?:"))
match answer:
     case "1":
          print(f"\nGood Choice {charades_version_list[0]} it is!.")
     case "2":
          print(f"\nGood Choice {charades_version_list[1]} it is!.")     
          
# Start of game.
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

playerIndex = 0
while True:
    word = random.choice(WORDS)
    print(f"\n {playerList[playerIndex]}, it's your turn:")
    print(f"\n The word / phrase to act out is:\n\n {word.title()}")
    guess = input("\n Who guessed this correctly? ")
    playerIndex = (playerIndex+1) % len(playerList)


