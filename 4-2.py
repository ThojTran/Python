import random

def game_taixiu(player, bet_game):
    win = False
    total = random.randint(1,6) + random.randint(1,6)
    while True:
        text = input("Chọn tài hoặc xỉu hoặc 5: ")
        if text == "tai" or text == "xiu" or text == "5":
            break
    if total == 5:
        if text == "5":
            print(total)
            print('You big win!')
            win = True
            player += bet_game *3
        else:
            print(total)
            player -= bet_game
    elif total > 5 and text == "tai":
            print(total)
            print('You win!')
            player += bet_game
            win = True
    elif total < 5 and text == "xiu":
            print(total)
            print('You win!')
            player += bet_game
            win = True
    else:
        print(total)
        print('You lose!')
        player -= bet_game
    return player,win
def start_game():
    while True:
        bet_game = int(input("Bet game(1 lần/ 10000): "))
        if bet_game >= 10000:
            break
        else:
            print("Bạn đã nhập sai mời nhập lại")
    return bet_game
if __name__ == '__main__':
    cost_player = 100000
    cou_wins = 0
    cou_games = 0
    while True:
        print(f"Số tiền bạn đang có {cost_player}")
        if cost_player < 10000:
            print("Bạn không có đủ số dư")
            break
        bet_amount = start_game()
        cost_player,win = game_taixiu(cost_player, bet_amount)
        cou_games +=1
        if win:
            cou_wins += 1
        a = input("Bạn có muốn chơi tiếp (n/N): ")
        if a == "n" or a == "N":
            print('Bye!')
            break
        print(f"Số lượt chơi {cou_games} va số lượt thắng {cou_wins}")
    print("Cam on ban da choi")
