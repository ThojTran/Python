import random
from random import choice


def menu():
    print("-------------------------------MENU-------------------------------------")
    print("1. In ra danh sách vừa tạo.")
    print("2. In đảo ngược danh sách.")
    print("3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).")
    print("4. tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.")
    print("5. Dếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.")
    print("6. In ra vị trí các phần tử là số nguyên tố.")
    print("7. tìm các số duy nhất (không trùng lặp) trong danh sách.")
    print("8. liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.")
    print("9. In ra các đoạn con trong danh sách giảm liên tiếp.")
    text = int(input("Enter your nuber: "))
    return text
def rand_list():
    ls = list()
    for i in range(n):
        i = random.randint(1,100)
        ls.append(i)
    print(ls)
    return ls
def task1(count):
    print("Danh sach hien")
if __name__ == "__main__":
    n = int(input("Nhap so phan tu mang muon tao: "))
    my_list = rand_list()
    while True:
        choice = menu()
        if choice == 1:
            break
        




