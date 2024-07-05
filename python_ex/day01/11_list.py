STUDENTS = 5
list = []
count = 0

for i in range(STUDENTS):
    value = int(input("성적을 입력하세요"))
    list.append(value)

print(max(list))
print(min(list))

print(f"성적평균 = {sum(list)/len(list)}")


#80점 이상의 성적의 학생수를 카운트할때
for score in list:
    if score >=80:
        count+=1

print(f"80점 이상 {count}명이다")