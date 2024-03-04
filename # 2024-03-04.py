# 2024-03-04 공부

 

  

  # 진리값

# 참과 거짓이 있다.
# and는 둘 다 참이여야 참이 된다.
# or은 둘 중 하나면 참이면 참이 된다,
# not은 뒤집기 

print(True and False)

# 크다 > 작다
# 같거나 크다 >= 같거나 작다
# 같다 == 같다
# 같지 않다 != 같지 않다

  
  
  
  
  # type 함수 & def 함수

print(type(1))
print(type(1.0))
print(type("으악"))
print(type(print))

# def 함수(): !!들여쓰기!! 정의하기

def go():
    print("우끼끼")

go()

print(type(go))





  # 잡다한 것들

# 나중에 가면 input함수가 있는 걸로 아는데 그때 def를 이용해서 재미있는 것을 만들 수 있겠다

# 엥 뭐지... int(2.5)는 오류나는 거 아니였나?

print(int(2.5)) 

# 왜 버리지?????.......         ***아 원래 버리는 거였네***





  # 지정 연산자

num_1 = 3

num_1 = num_1 + 7

print(num_1)

# 이건 그냥 외우는 수 밖에 없다

# 더 간단한 방법!!!!

c = 10

c += 3

print(c)

print("여기에요.")

# 이런게 있다는 건 많이 쓴다는 뜻이겠지?





  # return 문......

# return 문에는 두가지 기능이 있다 
# 1. 함수 입력값을 통해 값을 되돌려주는 것
# 2. 끝내기(데드 코드 유발)
# + 참고로 함수를 정의할 때 굳이 input을 안써도 될 듯 x로 변수를 고정할 수 있으니

def print_bump(x):
    print(x + x)

def return_bump(x):
    return x + x
    print("get out!")

print_bump(3)

return_bump(4)

# return은 값을 대체하기만 했지 그것을 출력하지는 않는다.

print(return_bump(5))

# return이 살짝 복잡한 개념인 것 같으니까 그냥 익숙해지자

print(print_bump(6))

# 살짝 알겠다. print는 값을 대체하지는 않는다. return은 그것을 사용한 함수 자체의 형을 숫자로 바꾼다
# 함수 자체를 print 하고 싶을 때 사용한다.





  # def에 변수 여러개 설정과 옵셔널 파라미터(고정값)

# def에 변수 여러개 설정

def three_no(x, y, z):
    print(x)
    print(y)
    print(z)

three_no("할머니", 1, 10.22)

# 고정값 설정

def three_yes(x, y, z = "고정되었다"):
    print(x)
    print(y)
    print(z)

three_yes("할아버지", 22923)

# def 함수 정의할 때 꼭 클론을 써야한다.
# 고정값은 항상 마지막에 있어야 한다.





  # 로컬 변수

# 함수 내에서 정의한 변수는 글로벌하게 사용할 수 없다. 정의되지 않은 변수라고 오류난다.





  # 상수

# 상수는 대문자로 쓰고 수정하지 않는다.





  # ***PET8 규칙***

# 상수 대문자 + 여러 단어 _로 이어서 쓰기 + 이름은 항상 의미 있게
# 들여쓰기는 스페이스 4번 + 함수 정의 위아래 2칸 띄기
# (사실 지금 쓰는 그대로)괄호 바로 안은 스페이스 하지마라 + 바로 앞도         mm(1)
# 쉼표 지금 쓰는 그대로
# 코멘트 띄어쓰기 2번  # 띄어쓰기 1번





