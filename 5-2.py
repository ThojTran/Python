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
def task1():
    print(f"Danh sach hien dang co {my_list}")
def task2():
    reversed = my_list[::-1]
    print(f"Danh sach dao nguoc la {reversed}")
def task3():
    sort = sorted(my_list)
    print(f"Danh sach da duoc sap xep {sort}")
def task4():
    max = my_list[0]
    vtm = 0
    for i in range(len(my_list)):
        if my_list[i]>max:
            max = my_list[i]
            vtm = i
        elif(my_list == max):
            vtm = i
    print(f"Phan tu lon nhat la {max}")
    print(f"Phan tu lon nhat cuoi cung la {vtm+1}")
def task5():
    X= int(input("Moi ban nhap số để đếm số lượng: "))
    vtm = 0
    for i in range(len(my_list)):
        if my_list[i] == X:
            vtm = i
            print(f"Các vị trí xuất hiện {vtm+1}")  
def task6():
    vtm = 0
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            vtm = i
            print(f"Vị trí {vtm +1} là số nguyên tố \n")
def task7():   
    for i in my_list:
        if my_list.count(i) == 1:
            print(f"So ko trung la {i}")
def task8():
    check = set()
    for i in my_list:
        if i not in check:
            print(f"Số {i} ở vị trí xuất hiện {my_list.count(i)}")
            check.add(i)
def task9():
    result = []
    check = [my_list[0]]
    for i in range(1,len(my_list)):
        if my_list[i] < my_list[i-1]:
            check.append(my_list[i])
    if len(check) > 2:
        result.append(check)
    if result:
        print(f"Đoạn giảm liên tiếp {result}")
    else:
        print("Ko có nào liên tiếp")
if __name__ == "__main__":
    n = int(input("Nhap so phan tu mang muon tao: "))
    my_list = rand_list()
    while True:
        choice = menu()
        if choice == 1:
            task1()
            break
        if choice == 2:
            task2()
            break
        if choice == 3:
            task3()
            break
        if choice == 4:
            task4()
            break
        if choice == 5:
            task5()
            break
        if choice == 6:
            task6()
            break
        if choice == 7:
            task7()
            break
        if choice == 8:
            task8()
            break
        if choice == 9:
            task9()
            break
        
        
        




