scores = [80,99,100,70,50,30]
print(f"제거 하기 전{scores}")

# 최소, 최댓값 제거 
scores.remove(max(scores))#scores안에서 최고값을 선택하여 지우기
print(scores) # [80, 99, 70, 50, 30]
scores.remove(min(scores))
print(scores) #[80, 99, 70, 50]

