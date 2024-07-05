#key와 value
menus = {"아메리카노":4000,"카페라떼":5000,"카페모카":6000}
print(menus)#{'아메리카노': 4000, '카페라떼': 5000, '카페모카': 6000}
print(menus["아메리카노"])#key값을 통한 value 구하기
print(menus.keys())
print(menus.values())
print(menus.items())

print("==========메뉴=========")
for name, price in menus.items():
    print(f"{name} : {price}원")
selected_menu = input("주문할 메뉴를 입력하세요")

price = menus.get(selected_menu, 0)
if price == 0:
    print("메뉴가 없습니다")
else:
    money = int(input("돈을 넣어주세요"))
    change = money - price
    if change >= 0:
        print(f"{selected_menu} 구매. 거스름돈 {change}원입니다")
    else:
        print("돈이 부족합니다")
