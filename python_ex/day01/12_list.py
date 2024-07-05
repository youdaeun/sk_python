def print_menu():
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")

friends = []

while True:
    print_menu()
    menu = int(input("메뉴를 선택해주세요 : "))
    
    if menu == 1:
        print(friends)
    
    elif menu == 2:
        name = input("추가할 이름을 입력하세요: ")
        friends.append(name)
    
    elif menu == 3:
        del_name = input("삭제할 이름을 입력하세요: ")
        if del_name in friends:
            friends.remove(del_name)
        else:
            print("삭제할 이름이 없습니다.")
    
    elif menu == 4:
        change_name = input("변경할 이름을 입력하세요: ")
        if change_name in friends:
            index = friends.index(change_name)
            new_name = input("새로운 이름을 입력하세요: ")
            friends[index] = new_name
        else:
            print("이름이 발견되지 않았습니다.")
    
    elif menu == 9:
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")
