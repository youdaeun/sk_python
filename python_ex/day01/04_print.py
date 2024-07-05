#형에 대해서는 문자열 형태로 출력이 되기 때문에 그냥 입력했다.
#다만, 숫자만 들어가야하는 경우가 있다.
#따라서 형변환을 해야한다. 이때 숫자만할때는 처음 input할때 int로 형변환을 한다.

#example 
a = int(input("국어 점수 : "))
b = int(input("영어 점수 : "))
c = int(input("수학 점수 : "))

print(type(a))
score = a + b + c
print(f"시험 종합 성적은 300점 만점의 {score}")