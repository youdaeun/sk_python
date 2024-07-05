scores = [80,99,100,70,50,30]
#append 추가한다.
#insert는 인덱스를 지원하는 함수, append는 인덱스를 지원하지 않는 함수이며,
#값을 추가하는 함수이다.

scores.append(110)
print(scores)#[80,99, 100, 70, 50, 30, 110]

scores.insert(2,80)
print(scores) # [80,99,80, 100, 80, 70, 50, 30, 110]

scores.remove(99) #값 99 삭제
print(scores) #[80, 80, 100, 70, 50, 30, 110]

del scores[1]   # 첫 번째 요소 삭제