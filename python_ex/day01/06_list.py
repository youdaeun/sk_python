surnames = ['ngnicky', 'kim', 'Lee']
ages = [23,24,25] 

#enumerate 사용
for position, surname in enumerate(surnames): 
    age = ages[position]
    print(surname, age)

#zip 사용
#데이터가 2,3개 정도 있는데 묶어서 출력하고 싶을 때 사용
for surname, age in zip(surnames,ages):
    print(surname,age)
