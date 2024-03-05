# 2024-03-05





  # 거스름돈 계산하기 예제

# 나의 코드


'''def calculate_change(payment, cost):
    (payment - cost) / 500000 = fifty_thousand
    (payment - cost) % 500000 = except_fifty_thousand
    except_fifty_thousand / 100000 = ten_thousand
    except_fifty_thousand % 100000 = except_ten_thousand
    except_ten_thousand / 50000 = five_thousand
    except_ten_thousand % 50000 = except_five_thousand
    except_five_thousand / 10000 = one_thousand
    print("50000원 지폐: {}장" . format(fifty_thousand))
    print("10000원 지폐: {}장" . format(ten_thousand))
    print("5000원 지폐: {}장" . format(five_thousand))
    print("1000원 지폐: {}장" . format(one_thousand))'''


# 오류 : 우선 지정연산자? 이거를 잘못 썼다. 순서가 바뀌어야한다.
# 오류 : 그리고 버림 나눗셈을 해야한다. 그렇지 않으면 1.34장 이딴 식으로 나온다....
    
# 고친 코드 
    

def calculate_change(payment, cost):
    
    fifty_thousand = (payment - cost) // 50000
    except_fifty_thousand = (payment - cost) % 50000
    
    ten_thousand = except_fifty_thousand // 10000
    except_ten_thousand = except_fifty_thousand % 10000
    
    five_thousand = except_ten_thousand // 5000
    except_five_thousand = except_ten_thousand % 5000
    
    one_thousand = except_five_thousand // 1000
    
    print("50000원 지폐: {}장" . format(fifty_thousand))
    print("10000원 지폐: {}장" . format(ten_thousand))
    print("5000원 지폐: {}장" . format(five_thousand))
    print("1000원 지폐: {}장" . format(one_thousand))


# 화이트 스페이스를 내 멋대로 사용해 보았다. 더 보기 좋은 것 같은데...
    




  # while 반복문 

# 한마디로 표현해서 만약 ~ 하다면 ~ 해라를 반복하는 것이다.
# 만약을 담당하는 부분은 불린값으로 나타내져야 된다
    




  # if 문
    
# 엄청 간단하다... 그냥 문지가 역할을 할 뿐인 것 같다
# elif는 그냥 2개였던 선택지를 엄청나게 늘릴 수 있게 도와주는 역할이다





  # wile if 예제
    
# while문과 if문을 활용하여, 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요

# 나의 코드
    
'''x = 1
while x <= 100:
    if x % 8 = 0:
        if x % 12 = 0:
        else:
            print(x)
    else:
    x += 1'''
 
# 같다를 판단하는 연산자는 =이 아니라 ==여서 고쳤다

'''x = 1
while x <= 100:
    if x % 8 == 0:
        if x % 12 == 0:
        else:
            print(x)
    else:
    x += 1'''

# 왜 안되는 지 모르겠다 
# IndentationError: expected an indented block after 'if' statement on line 95라고 한다
# 비워져 있으면 안되나 보다 싶어서 새로운 작전을 짰다

x = 1
y = 1
while x <= 100:
    if x % 8 == 0:
        if x % 12 == 0:
            y = 3
        else:
            print(x)
    else:
        y = 3
    x += 1

# 아니 비워져 있어도 되야하는 거 아닌가

# 알아냈다 비우고 싶으면 pass를 쓰면 된다!!
    




  # 약수 출력 예제(정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 코드를 작성해 보세요.)
    
num_2 = 1
num_3 = 0
while num_2 <= 120:
    if 120 % num_2 == 0:
        print(num_2)
        num_3 += 1
    else:
        pass
    num_2 += 1
print("120의 약수는 총 {}개입니다.".format(num_3))





  #은행 예제
'''1988년 쌍문동에 사는 택이는 바둑 대회 우승 상금으로 5,000만 원을 받았습니다.

이 돈을 어떻게 할지 고민하던 택이는, 이웃인 동일 아저씨와 미란 아주머니의 의견 중 하나를 선택하려 합니다.

동일 아저씨 의견
> 원금에 붙은 이자에 다시 이자가 붙는 연복리 예금에 넣기


 <연복리 예금 상품 정보>

 원금: 50,000,000 원
 연 이율: 12%
 1년 뒤 은행 잔고: 50,000,000 * (1 + 12%) = 56,000,000 원
 2년 뒤 은행 잔고: 50,000,000 * (1 + 12%) * (1 + 12%) = 62,720,000 원
 ...
미란 아주머니 의견
> 아파트 가치 상승을 고려하여 당시 매매가 5000만 원인 은마 아파트 사기

2016년 기준 은마아파트의 매매가는 11억 원인데요. 1988년 은행에 5,000만 원을 넣었을 경우 2016년에는 얼마가 있을지 계산하여,

은행에 저축해 둔 금액이 더 크면, *원 차이로 동일 아저씨 말씀이 맞습니다.를 출력하고
은마아파트의 가격이 더 크면, *원 차이로 미란 아주머니 말씀이 맞습니다.를 출력하는 코드를 작성해 보세요.'''

# 나의 코드

'''year = 1988
money = 50000000

while year < 2016:
    year += 1
    money = 50000000 * (112/100)

if money > 1100000000:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(money - 1100000000))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(1100000000 - money))'''

# 완전 잘못되었다. 돈에다가 돈을 곱한걸 업데이트 해야하는데 상수를 박아버렸다...

# 고친 코드
    
year = 1988
money = 50000000

while year < 2016:
    year += 1
    money = money * (112/100)

if money > 1100000000:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(money - 1100000000))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(1100000000 - money))

# 새로운 문제가 발생했다. 돈이 소수점으로 길게 간다. 이럴 때는 :.0f 로 해결하면 되는 걸로 알고 있다.
    
year = 1988
money = 50000000

while year < 2016:
    year += 1
    money = money * (112/100)

if money > 1100000000:
    print("{:.0f}원 차이로 동일 아저씨 말씀이 맞습니다.".format(money - 1100000000))
else:
    print("{:.0f}원 차이로 미란 아주머니 말씀이 맞습니다.".format(1100000000 - money))





  # 파보나치 예제(피보나치 수열의 첫 50개 항을 차례대로 출력하는 코드를 작성해 보세요.)
    
bucket_1 = 1
bucket_2 = 1
trial = 1

while trial <= 25:
    print(bucket_1)
    print(bucket_2)
    bucket_1 += bucket_2
    bucket_2 += bucket_1
    trial += 1





  # 구구단 만들기 예제

left = 1
right = 1

while left <= 9:
    while right <= 9:
        print(f"{left} * {right} = {left * right}")
        right += 1
    left += 1
    right = 1
    
# 한번에 클리어!! 이번에는 포맷을 색다른 걸로 써봤다 여러가지 연습할 겸
    




  # while과 if와 같이 쓸 수 있는 여러가지 명령어들
    
# break : while의 루프를 박살 내고 나올 수 있다
# continue : while의 루프를 박살 내지는 않지만 그 이후에 있는 것들을 무시하고 바로 다시 루프로 들어간다
    




    # 리스트와 인덱스
    
poketmon = ["피카츄", "라이츄", "파이리", "꼬부기", "버터플", "야도란", "피죤투", "또가스"]

index = 7

while index >= -8:
    print(poketmon[index])
    index -= 1

# 개념이 어렵지 않다. 이제 이런 걸 이용해서 빅데이터를 만드나 보다
    
# 리스트 슬라이싱
    
print(poketmon[0:3])
print(poketmon[3:])

# 리스트와 지정 연산자

poketmon[2] = "포켓몬 너무 싫어"
print(poketmon)