scores = [80, 99,100, 70, 50,30, 40, 10,33,77]
         # 0   1   2   3   4  5
numbers = scores[2:5]
print(numbers) #[100, 70, 50] 2:5는 인덱스 2포함 5아래 

numbers = scores[2::2] # 시작점과 스텝의 의미
print(numbers)

numbers = scores[1:-1]
print(numbers)