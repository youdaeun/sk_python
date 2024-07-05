import re
text = "오늘은 2024년 5월 6일입니다"
pattern = re.compile(r"\d+")#\d는 특수문자
matches = pattern.findall(text)
print(matches) #['2024','5','6']


pattern = re.compile(r"\\d+")#\d는 숫자
text = "오늘은 2024년 5월 6일입니다"
matches = pattern.findall(text)
print(matches) #['2024','5','6']