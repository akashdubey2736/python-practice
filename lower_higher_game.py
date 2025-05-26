import random

players=[{"name":"Sachin",
          "country":"India",
          "century":100,
          "matches":463},
         {"name":"Virat",
          "country":"India",
          "century":105,
          "matches":300},
         {"name":"Ponting",
          "country":"Australia",
          "century":80,
          "matches":450},
         {"name":"Gilchrist",
          "country":"Australia",
          "century": 50,
          "matches":500},
         {"name":"Peterson",
          "country":"England",
          "century":20,
          "matches":250}]


def player_compare(player1,player2):
    global player1_matches, player2_matches
    for player in players:
        if player["name"]==player1["name"]:
            player1_matches=player["matches"]
        if player["name"]==player2["name"]:
            player2_matches=player["matches"]
    if player1_matches > player2_matches:
        return player1["name"]
    else:
        return player2["name"]

game_continue=True

print("Welcome to the lower/higher game!")
while game_continue:
    player1=random.choice(players)
    player2=random.choice(players)
    while player1["name"]==player2["name"]:
        player2=random.choice(players)

    print(player1["name"])
    print(player2["name"])

    choice=input("Guess the player from above two, who has played more matches?")
    result=player_compare(player1,player2)
    if choice==result:
        print("Your choice is correct. Continue playing..")
    else:
        print("Oops, your choice is wrong. Game Over!!")
        game_continue=False