import math
from collections import Counter


def tuple_6():   # Use a breakpoint in the code line below to debug your script.
    game = tuple(("LOL", "Valorant", "PUBG", "CSGO", "Minecraft", "FIFA ONLINE 4"))
    print(game)
    (*riot, fps1, fps2, mojang, garena) = game
    fps = fps1, fps2
    print("riot: ", riot)
    print("FPS: ", fps)
    print("mojang: ", mojang)
    print("Garena: ", garena) # Press Ctrl+F8 to toggle the breakpoint.
    x = list(game)
    x.append("Valorant")
    game = tuple(x)
    print(game)
    index = game.index("CSGO")
    print(index)
    count = game.count("Valorant")
    print(count)

def set_6():
    number = {5,7,7,3,9,3,12,1,2}
    print(number)
    print(f"Gia tri lon nhat la: {max(number)}")
    print(f"Gia tri nho nhat la: {min(number)}")
    text = int(input("Moi ban nhap gia tri : "))
    if text not in number:
        print("So ko ton tai trong chuoi!")
    else:
        print("So ton tai!")
    A, B = {1, 3, 5}, {1, 2, 3}
    print('Union using union():', A.union(B))
    x = A.intersection(B)
    if len(x) >= 1:
        print(f"Co phan tu chung do la {x} ")
    else:
        print("Ko co phan tu chung")
def set_6_1():
    number = [5,7,7,3,9,3,12,1,2]
    number_count = {}
    for i in number:
        number_count[i] = number.count(i)
        if number_count[i] == 1:
            print(f" So unique la {i} ")
    print(number_count)
def set_6_2():
    A, B = {1, 3, 5}, {1, 2, 3}
    print('Symmetric Difference using symmetric_difference():', A.symmetric_difference(B))
def dic_6():
    a = ["Tho", 20, "UEH"]
    b = ["Loc", 21, "Van Lang"]
    general = dict(zip(a, b))
    print(general)
    dict1 = {'Ten': 10, 'Twenty': 20, }
    dict2 = {'Thirty': 30, 'Fourty': 40,}
    dicts = {**dict1, **dict2}
    print(dicts)
    event = {
        "Name":{
            "ID001": "Chien thang dien bien phu",
            "ID002": "Giai phong mien nam"
        },
        "meansured":{
            "History":"7/5/1954",
            "Memory": "50 nam"
        }
    }
    print(f"Ngay chien thang dien bien phu {event["meansured"]["History"]}")
    dict3 = ["Tho", "Loc"]
    default = {"IT": "developer", "salary": 9000 }
    init = dict.fromkeys(dict3, default)
    print(init)
    country_capitals = {
        "Germany": "Berlin",
        "Canada": "Ottawa",
        "England": "London",
        "France": "Paris"
    }
    keys = ["Germany", "England"]
    new_dict = {k:country_capitals[k] for k in keys}
    print(new_dict)
    new_dict = {k: country_capitals[k] for k in country_capitals.keys() - keys}
    print(new_dict)
    exists = dict.values(default)
    if "developer" in exists:
        print("IT co ton tai trong dict")
    country_capitals["VietName"] = country_capitals.pop("France")
    country_capitals["VietName"] = "Ha Noi"
    print(country_capitals)
    mark = {
    'Physics': 8,
    'Math': 10,
    'history': 6
    }
    print(min(mark, key=mark.get))
    employees= {
        1001:{"name":"Alice", "department":"Engineering","salary":75000},
        1002:{"name":"Bob", "department":"Sales","salary":50000},
        1003:{"name": "Charlie", "department": "Engineering", "salary": 80000},
        1004: {"name": "Dave", "department": "Markerting", "salary": 60000}
    }
    employees[1004]["salary"] = 1000000
    print(employees)
    text = ("Ngày 30/4 không đơn thuần là con số trên lịch sử. Đó là cảm xúc nghẹn ngào của người lính già khi lần đầu đặt chân lên mảnh đất Sài Gòn sau ba mươi năm xa cách. "
            "Là tiếng khóc nức nở của người mẹ trước bàn thờ liệt sĩ. Là khoảnh khắc triệu trái tim cùng đập chung nhịp khi lá cờ đỏ sao vàng tung bay trên nóc Dinh Độc Lập - nơi từng được mệnh danh là "
            "Chiến thắng ấy không chỉ đo bằng súng đạn, mà bằng cả biển người với trái tim nồng nàn yêu nước.")
    char = Counter(text)
    print(char)
def dict_6_2(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
def dict_6_3():
    value = int(input("Moi ban nhap 1 so:"))
    dicts = {}
    key =1
    for i in range(value):
        if dict_6_2(i):
            dicts[key] = i
            key += 1
    print(dicts)
if __name__ == '__main__':
    dict_6_3()