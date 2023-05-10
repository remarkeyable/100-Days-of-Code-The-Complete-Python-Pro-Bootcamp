from replit import clear

help = ''' ───────✧❁✧──────────────✧❁✧───────
   𝐆𝐞𝐭 𝐭𝐡𝐫𝐞𝐞 𝐨𝐟 𝐲𝐨𝐮𝐫 𝐬𝐲𝐦𝐛𝐨𝐥𝐬 ❌ 𝐨𝐫 🟢 𝐢𝐧 
   𝐚 𝐫𝐨𝐰 𝐨𝐧 𝐚 𝟑𝐱𝟑 𝐠𝐫𝐢𝐝, 𝐰𝐡𝐞𝐫𝐞 𝐞𝐚𝐜𝐡 𝐬𝐪𝐮𝐚𝐫𝐞 ⬜ 
   𝐢𝐬 𝐥𝐚𝐛𝐞𝐥𝐞𝐝 𝐰𝐢𝐭𝐡 𝐚 𝐮𝐧𝐢𝐪𝐮𝐞 𝐜𝐨𝐦𝐛𝐢𝐧𝐚𝐭𝐢𝐨𝐧 𝐨𝐟 𝐥𝐞𝐭𝐭𝐞𝐫𝐬 
   𝐚𝐧𝐝 𝐧𝐮𝐦𝐛𝐞𝐫𝐬 (𝐞.𝐠., 𝐚𝟏, 𝐛𝟐, 𝐜𝟑). 
   𝐏𝐥𝐚𝐲𝐞𝐫𝐬 𝐭𝐚𝐤𝐞 𝐭𝐮𝐫𝐧𝐬 𝐩𝐥𝐚𝐜𝐢𝐧𝐠 𝐭𝐡𝐞𝐢𝐫 𝐬𝐲𝐦𝐛𝐨𝐥𝐬 𝐨𝐧 
   𝐞𝐦𝐩𝐭𝐲 𝐬𝐪𝐮𝐚𝐫𝐞𝐬 𝐮𝐧𝐭𝐢𝐥 𝐨𝐧𝐞 𝐩𝐥𝐚𝐲𝐞𝐫 𝐬𝐮𝐜𝐜𝐞𝐞𝐝𝐬 
   𝐢𝐧 𝐠𝐞𝐭𝐭𝐢𝐧𝐠 𝐭𝐡𝐫𝐞𝐞 𝐢𝐧 𝐚 𝐫𝐨𝐰 𝐨𝐫 𝐚𝐥𝐥 𝐬𝐪𝐮𝐚𝐫𝐞𝐬 𝐚𝐫𝐞 
   𝐟𝐢𝐥𝐥𝐞𝐝, 𝐫𝐞𝐬𝐮𝐥𝐭𝐢𝐧𝐠 𝐢𝐧 𝐚 𝐭𝐢𝐞.
 ───────✧❁✧──────────────✧❁✧───────'''

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


# Will  clear the tictactoe board
def new_game():
    global moves
    moves = []
    for i in range(len(x)):
        x[i] = "⬜"
    return print(board())


# Will check if a player already win
def check_winner():
    global p1_score
    global p2_score
    if x[0] == "❌" and x[1] == "❌" and x[2] == "❌":
        # will track the scores of each players
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[0] == "🟢" and x[1] == "🟢" and x[2] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player2} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p2_score} ░ {player2} : {p2_score}")
    elif x[3] == "❌" and x[4] == "❌" and x[5] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[3] == "🟢" and x[4] == "🟢" and x[5] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player2} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p2_score} ░ {player2} : {p2_score}")
    elif x[6] == "❌" and x[7] == "❌" and x[8] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[6] == "🟢" and x[7] == "🟢" and x[8] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player2} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p2_score} ░ {player2} : {p2_score}")
    elif x[0] == "❌" and x[3] == "❌" and x[6] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[0] == "🟢" and x[3] == "🟢" and x[6] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player2} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[1] == "❌" and x[4] == "❌" and x[7] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[1] == "🟢" and x[4] == "🟢" and x[7] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player2} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[2] == "❌" and x[5] == "❌" and x[8] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[2] == "🟢" and x[5] == "🟢" and x[8] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player2} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[0] == "❌" and x[4] == "❌" and x[8] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[0] == "🟢" and x[4] == "🟢" and x[8] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player2} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[2] == "❌" and x[4] == "❌" and x[6] == "❌":
        p1_score += 1
        new_game()
        return print(f"{player1} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif x[2] == "🟢" and x[4] == "🟢" and x[6] == "🟢":
        p2_score += 1
        new_game()
        return print(f"{player2} ＷIＮ ！！！ ⸜(｡˃ ᵕ ˂ )⸝♡\n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}")
    elif len(moves) >= 9:
        print(f"ＧＡＭＥ ＥＮＤＥＤ． ＩＴ＇Ｓ Ａ ＴＩＥ \n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score} ")
        clear()
        new_game()


# Will add the move to the board given by player 1
def player_1():
    p1move = input(f"{player1}'s turn:").lower()
    if p1move == "a1" and x[0] == "⬜":
        x[0] = "❌"
        moves.append(p1move)
        print(board())
        check_winner()
    elif p1move == "a2" and x[3] == "⬜":
        x[3] = "❌"
        moves.append(p1move)
        print(board())
        check_winner()
    elif p1move == "a3" and x[6] == "⬜":
        x[6] = "❌"
        moves.append(p1move)
        print(board())
        check_winner()
    elif p1move == "b1" and x[1] == "⬜":
        x[1] = "❌"
        moves.append(p1move)
        print(board())
        check_winner()
    elif p1move == "b2" and x[4] == "⬜":
        x[4] = "❌"
        moves.append(p1move)
        print(board())
        check_winner()
    elif p1move == "b3" and x[7] == "⬜":
        x[7] = "❌"
        moves.append(p1move)
        print(board())
        check_winner()
    elif p1move == "c1" and x[2] == "⬜":
        x[2] = "❌"
        moves.append(p1move)
        print(board())
        check_winner()
    elif p1move == "c2" and x[5] == "⬜":
        x[5] = "❌"
        moves.append(p1move)
        print(board())
        check_winner()
    elif p1move == "c3" and x[8] == "⬜":
        x[8] = "❌"
        moves.append(p1move)
        print(board())
        check_winner()
    elif p1move == "exit":
        print(f"Game ended ~ \n【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score}  ")

    else:
        print("Either wrong input or board is already occupied. Please double check & try again")
        player_1()


# Will add the move to the board given by player 2
def player_2():
    global on
    p2move = input(f"{player2}'s turn:").lower()
    if p2move == "a1" and x[0] == "⬜":
        x[0] = "🟢"
        moves.append(p2move)
        print(board())
        check_winner()
    elif p2move == "a2" and x[3] == "⬜":
        x[3] = "🟢"
        moves.append(p2move)
        print(board())
        check_winner()
    elif p2move == "a3" and x[6] == "⬜":
        x[6] = "🟢"
        moves.append(p2move)
        print(board())
        check_winner()
    elif p2move == "b1" and x[1] == "⬜":
        x[1] = "🟢"
        moves.append(p2move)
        print(board())
        check_winner()
    elif p2move == "b2" and x[4] == "⬜":
        x[4] = "🟢"
        moves.append(p2move)
        print(board())
        check_winner()
    elif p2move == "b3" and x[7] == "⬜":
        x[7] = "🟢"
        moves.append(p2move)
        print(board())
        check_winner()
    elif p2move == "c1" and x[2] == "⬜":
        x[2] = "🟢"
        moves.append(p2move)
        print(board())
        check_winner()
    elif p2move == "c2" and x[5] == "⬜":
        x[5] = "🟢"
        moves.append(p2move)
        print(board())
        check_winner()
    elif p2move == "c3" and x[8] == "⬜":
        x[8] = "🟢"
        moves.append(p2move)
        print(board())
        check_winner()
    elif p2move == "exit":
        print(f"EXITED GAME ~ \n 【ＳＣＯＲＥＳ】{player1} : {p1_score} ░ {player2} : {p2_score} ")
        on = False
    else:
        print("Either wrong input or board is already occupied. Please double check & try again")
        player_2()


on = True
print(
    f" 【𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙏𝙄𝘾 𝙏𝘼𝘾 𝙏𝙊𝙀 ❕❕  ପ(๑•ᴗ•๑)ଓ ♡】\n\n {help}\n\n【𝐓𝐈𝐏： 𝐓𝐲𝐩𝐞 𝐄𝐗𝐈𝐓 𝐢𝐟 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐞𝐧𝐝 𝐭𝐡𝐞 𝐠𝐚𝐦𝐞.】")

player1 = input("\n  Please enter Player 1 Name: ").upper()
player2 = input("  Please enter Player 2 Name: ").upper()

print(board())
print(f"{player1} is ❌ while {player2}  is 🟢")
while on:
    player_1()
    player_2()
