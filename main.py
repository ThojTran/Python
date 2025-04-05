# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def ex01():
    a = eval(input("Enter your nb "))
    b = eval(input("Enter your nb "))
    c = eval(input("Enter your nb "))
    perimeter = a + b + c
    print(f"Perimenter is {perimeter} ")

def ex02():
    length = eval(input("Enter your nb: "))
    width = eval(input("Enter your nb: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(area + "," + perimeter)

def ex03():
    r = eval(input("Enter your nb: "))
    pi = 3.14
    area = pi * r * r
    c = 2 * pi * r
    print(f"{area} , {c}")

def ex04():
    x = eval(input("Enter your nb: "))
    1
    print(y)

def ex05():
    import math
    x1 = 2
    y1 = 2
    x2 = 6
    y2 = 10
    m = (y2-y1)/(x2-x1)
    eu = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"{m} , {eu}")

def ex07():
    for x in range(-10,10):
        y = x ** 2 + 6 * x + 9
        if y == 0:
            print(x)

def ex08():
    a = 'python'
    b = 'dragon'
    print(len(a) != len(b))

def ex09():
    a = 'on'
    if a in "python" or 'dragon':
        print(True)

def ex10():
    a = 'jargon'
    if a in "python" or 'dragon':
        print(True)

def ex11():
    a = eval(input("Nhap so tuoi: "))
    if a % 2 == 0:
        print("Tuoi so chan")
    else:
        print("Tuoi so le")

def ex12():
    a = int(input("Nhap 1 so bat ky"))
    if a % 7 ==0:
        print("So chia het cho 7")
    else:
        print("Not")
def ex13():
    a = int(input("Nhap 1 so bat ky"))
    b = a % 10
    if b % 3 == 0:
        print("Chia het cho 3")
    else:
        print("Ko")


def ex14():
    num = random.randint(1, 9)  # Random number between 1 and 9
    print(num)
    guess = int(input("Doan 1 so bat ky 1-9: "))
    while num != guess:
        print(f"Wrong, {num}")
        guess = int(input("Doan 1 so bat ky 1-9: "))  # Prompt for new guess
    print("You are genius!")  # Correct guess

def ex15():
    for i in range(11):
        print(i)

def ex16():
    a = int(input("Nhap so: "))
    
if __name__ == '__main__':
    ex14()