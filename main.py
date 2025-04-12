# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def num():
    for i in range(10):
        print(i+1)
def total():
    nums = int(input(" Enter your num: "))
    for i in range(nums):
        t = i + (i +1)
        print(t)
def sum():
    even = 0
    odd = 0
    nums = int(input(" Enter your num: "))
    for i in range(nums):
        if i %2 ==0:
            even +=i
        else:
            odd +=i
    print(even)
    print(odd)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sum()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
