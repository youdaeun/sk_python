#Faker를 객체를 불러오기 위해 선언
from faker import Faker

#Faker 함수는 내부적으로 랜덤이 있다
#랜덤적으로 자신이 가지고 있는 사전파일 형태를 이용
#임의적으로 데이터들을 테스트하고자 할때 사용자의 데이터를 마음대로 가져오면 안된다.

fake = Faker('ko_KR') #한글버전으로 데이터를 만들 수 있다.

for i in range(10):
    name = fake.name()#이게 무슨 네임일까
    phone_number = fake.phone_number()
    print(f"이름 : {name} 전화번호 : {phone_number}")

    