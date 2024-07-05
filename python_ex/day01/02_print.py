name = input("이름을 입력하세요")
phone = input("번호를 입력하세요")
age = input("나이를 입력하세요")
print(name)
print(phone)
print(age)
print(name,"의 전화번호는",phone,"이고,","나이는",age,"입니다") ##다은의 전화번호는 29입니다

# print(type(name))#str 형
# print(type(phone))#str 형

#f-spring 방식을 가장 많이 사용된다.
print(f"내이름은 {name}이고 나이는{age}이며, 전화번호는 {phone}입니다")
