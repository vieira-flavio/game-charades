import random
playerList = []
print("\n Welcome to Charades!!!\n")
userAsk = str(input("Shall we begin (y/n)? "))
if userAsk == "y" :
    # Players = input("Insert Players\n")
    userNun=int(input("Number of players?\n> "))
    while len(playerList) != userNun:
        userNames=input("Please input name of player number {}/{}\n> ".format(len(playerList)+1, userNun))
        playerList.append(userNames)
    # random.shuffle(playerList)
    # print("\nRandomizing list..:",playerList)
# print("\nIt's your turn:" , random.choice(playerList))
playerIndex = 0
    
while True:
    WORDS = ["airplane", "boat", "baby", "Phone", "Toothbrush", "Hammer", "Shoelaces", "Flashlight", "Clown", "Mime", "Whale", "Kangaroo", "Monkey", "Rooster", "Cockroach", "Bartender", "Cow", "Bullfighter", "Yard sale", "Penguin"]
    PHRASES = ["Willy Wonka", "Buzz Lightyear", "Rod Stewart", "Lady Gaga", "Britney Spears", "Michael Jackson", "Doctor Evil"]
    word = random.choice(WORDS)
    correct = word
    jumble = ""
    print("\nIt's your turn:" ) 
    print(playerList[playerIndex])
    print("\nThe word / phrase to act out is:\n\n", word.title())
    
    guess = input("\nWho guessed this correctly? ")
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