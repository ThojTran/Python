# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

# def num():
#     for i in range(10):
#         print(i+1)
# def total():
#     nums = int(input(" Enter your num: "))
#     for i in range(nums):
#         t = i + (i +1)
#         print(t)
# def sum():
#     even = 0
#     odd = 0
#     nums = int(input(" Enter your num: "))
#     for i in range(nums):
#         if i %2 ==0:
#             even +=i
#         else:
#             odd +=i
#     print(even)
#     print(odd)
# def vowel():
#     a = ["a","e","o","u","i"]
#     text= input("Enter your name: ")
#     k = 0
#     for i in text:
#         if i in a:
#             k += 1
#     print(" So luong lap lai vowel la : ", k)
# def count():
#     text = input("Enter the words: ")
#     a = ["1","2","3","4","5","6","7","8","9"]
#     k = 0
#     for i in text:
#         if i in a:
#             k +=1
#     print("Count a number in text is ",k)
def game_engine(count):
    num = random.randint(1,100)
    for i in range(count):
        guess_num = int(input("Guess a number between 1 and 100: "))
        if num == guess_num:
            print(f"Congratulations! You guessed after {i+1} time!")
            break
        else:
            if num > guess_num:
                print("Too low!")
            else:
                print("Too high!")
    print(f"Dap an dung la {num}")
    print("Cam on ban da tham gia")
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
    count = choose_level()
    game_engine(count)
    while True:
        text = input("ban co muon choi lai ko n/N: ")
        if text == "n" or text == "N":
            break
        else:
            count = choose_level()
            game_engine(count)
        