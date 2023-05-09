from replit import clear

x = ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]
moves = []
p1_score = 0
p2_score = 0


def board():
    board = (f''' 
       a   b   c
    1 |{x[0]}|{x[1]}|{x[2]}|
    2 |{x[3]}|{x[4]}|{x[5]}|
    3 |{x[6]}|{x[7]}|{x[8]}|
    ''')
    return board


def check_board():
    if "⬜" not in x:
        return


def new_game():
    for i in range(len(x)):
        x[i] = "⬜"
    return print(board())



def check_winner():
    global p1_score
    global p2_score
    if x[0] == "❌" and x[1] == "❌" and x[2] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[0] == "🟢" and x[1] == "🟢" and x[2] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p2_score} ░ {player2} : {p2_score}")
    elif x[3] == "❌" and x[4] == "❌" and x[5] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[3] == "🟢" and x[4] == "🟢" and x[5] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p2_score} ░ {player2} : {p2_score}")
    elif x[6] == "❌" and x[7] == "❌" and x[8] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[6] == "🟢" and x[7] == "🟢" and x[8] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p2_score} ░ {player2} : {p2_score}")
    elif x[0] == "❌" and x[3] == "❌" and x[6] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[0] == "🟢" and x[3] == "🟢" and x[6] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[1] == "❌" and x[4] == "❌" and x[7] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[1] == "🟢" and x[4] == "🟢" and x[7] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[2] == "❌" and x[5] == "❌" and x[8] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[2] == "🟢" and x[5] == "🟢" and x[8] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[0] == "❌" and x[4] == "❌" and x[8] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[0] == "🟢" and x[4] == "🟢" and x[8] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[2] == "❌" and x[4] == "❌" and x[6] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[2] == "🟢" and x[4] == "🟢" and x[6] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")


def player_1():

    p1move = input(f"{player1}'s turn:").lower()
    if p1move == "a1" and x[0] == "⬜":
        x[0] = "❌"
        print(board())
        check_winner()
        moves.append(p1move)
    elif p1move == "a2" and x[3] == "⬜":
        x[3] = "❌"
        print(board())
        check_winner()
        moves.append(p1move)
    elif p1move == "a3" and x[6] == "⬜":
        x[6] = "❌"
        print(board())
        check_winner()
        moves.append(p1move)
    elif p1move == "b1" and x[1] == "⬜":
        x[1] = "❌"
        print(board())
        check_winner()
        moves.append(p1move)
    elif p1move == "b2" and x[4] == "⬜":
        x[4] = "❌"
        print(board())
        check_winner()
        moves.append(p1move)
    elif p1move == "b3" and x[7] == "⬜":
        x[7] = "❌"
        print(board())
        check_winner()
        moves.append(p1move)
    elif p1move == "c1" and x[2] == "⬜":
        x[2] = "❌"
        print(board())
        check_winner()
        moves.append(p1move)
    elif p1move == "c2" and x[5] == "⬜":
        x[5] = "❌"
        print(board())
        check_winner()
        moves.append(p1move)
    elif p1move == "c3" and x[8] == "⬜":
        x[8] = "❌"
        print(board())
        check_winner()
        moves.append(p1move)
    elif p1move == "exit":
        print("Game ended ~ \n FINAL SCORES ")

    else:
        print("Either wrong input or board is already occupied. Please double check & try again")
        player_1()


def player_2():
    global on
    p2move = input(f"{player2}'s turn:").lower()
    if p2move == "a1" and x[0] == "⬜":
        x[0] = "🟢"
        print(board())
        check_winner()
        moves.append(p2move)
    elif p2move == "a2" and x[3] == "⬜":
        x[3] = "🟢"
        print(board())
        check_winner()
        moves.append(p2move)
    elif p2move == "a3" and x[6] == "⬜":
        x[6] = "🟢"
        print(board())
        check_winner()
        moves.append(p2move)
    elif p2move == "b1" and x[1] == "⬜":
        x[1] = "🟢"
        print(board())
        check_winner()
        moves.append(p2move)
    elif p2move == "b2" and x[4] == "⬜":
        x[4] = "🟢"
        print(board())
        check_winner()
        moves.append(p2move)
    elif p2move == "b3" and x[4] == "⬜":
        x[7] = "🟢"
        print(board())
        check_winner()
        moves.append(p2move)
    elif p2move == "c1" and x[2] == "⬜":
        x[2] = "🟢"
        print(board())
        check_winner()
        moves.append(p2move)
    elif p2move == "c2" and x[5] == "⬜":
        x[5] = "🟢"
        print(board())
        check_winner()
        moves.append(p2move)
    elif p2move == "c3" and x[8] == "⬜":
        x[8] = "🟢"
        print(board())
        check_winner()
        moves.append(p2move)
    elif p2move == "exit":
        print(f"EXITED GAME ~ \n 【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score} ")
        on = False
    else:
        print("Either wrong input or board is already occupied. Please double check & try again")
        player_2()



on = True
print("𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙏𝙄𝘾 𝙏𝘼𝘾 𝙏𝙊𝙀 !  ପ(๑•ᴗ•๑)ଓ ♡\n\n𝙏𝙄𝙋： Type EXIT if you want to end the game")



player1 = input("\nPlease enter Player 1 Name: ").upper()
player2 = input("Please enter Player 2 Name: ").upper()

print(board())
print(f"{player1} is ❌ while {player2}  is 🟢")
while on:
    player_1()
    player_2()
    if len(moves) == 8:
        print(f"ＧＡＭＥ ＥＮＤＥＤ． ＩＴ＇Ｓ Ａ ＴＩＥ \n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score} ")
        clear()
        new_game()
        moves = []
