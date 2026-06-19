def main():
    difficulty = input("Difficult or casual? ").strip().title()
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ").strip().title() 
    if not (players == "Multiplayer" or players == "Singel-player"):
        print("Enter a valid number of players")
        return
    
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Singel-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")


def recommend(game):
    print("You might like", game)

main()
