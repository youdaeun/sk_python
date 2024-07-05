#리스트 방식으로 초기화하겠습니다.
#names = []
names= ['홍길동','유선재','김혜윤']
print(names)
print(type(names))
#리스트 방식이나 어떤 형태에 대해 순서대로 반복적으로 뽑을때
for name in names:
    print(name)

print(len(names))#길이
for i in range(3):
    print(i)

for name in range(len(names)):
    print(names[name])
    
for i in range(len(names)):
    print(f"{i+1}번째 : {names[i]}")

for i, name in enumerate(names):
    print(f"{i+1}번째 : {name}")