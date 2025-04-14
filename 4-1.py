import random
from jinja2.nodes import Break


def game_engine(count):
    win = False
    num = random.randint(1,100)
    print(num)
    for i in range(count):
        guess_num = int(input("Guess a number between 1 and 100: "))
        if num == guess_num:
            print(f"Congratulations! You guessed after {i+1} time!")
            win = True
            break
        else:
            if num > guess_num:
                print("Too low!")
            else:
                print("Too high!")
    print(f"Dap an dung la {num}")
    print("Cam on ban da tham gia")
    return win
def choose_level():
    print("Choose a level:(1-2-3)")
    print(" 1 se co 4 luot chon")
    print(" 2 se co 6 luot chon")
    print(" 3 se co 10 luot chon")
    while True:
        level = int(input("Choose a level: "))
        if 1<=level<=3:
            return 4 if level == 1 else 6 if level == 2 else 10
            break
        else:
            print("Ban nhap sai moi ban nhap lai: ")
if __name__ == '__main__':
    cou_plays = 0
    cou_wins = 0
    while True:
        cou_plays +=1
        count = choose_level()
        if game_engine(count):
            cou_wins += 1
        text = input("ban co muon choi lai ko n/N: ")
        if text == "n" or text == "N":
            break
    print(f"So lan ban da choi: {cou_plays}")
    print(f"So lan ban da thang: {cou_wins}")
