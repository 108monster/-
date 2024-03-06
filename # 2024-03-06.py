# 2024-03-06

    



    # 여러가지 리스트 함수들

my_list = [1, 2, 3]

print(len(my_list))  # 리스트에 몇개가 들어있는지를 나타낸다

my_list.append(588)  # 리스트에 추가한다
print(my_list)

my_list.insert(0, 1004) #리스트의 원하는 부분에 삽입한다
print(my_list)

del my_list[2]  # 리스트에 2번 인덱스를 삭제한다
print(my_list)

my_new_list = sorted(my_list, reverse = True)  # 리스트를 정렬한다. reverse = True를 쓰면 거꾸로 정렬된다. 근데 방금 ture라고 써서 오류남;;;
print(my_new_list)

my_list.sort()  # 이렇게 쓰면 그냥 리스트가 정렬된다. sorted와 마찬가지로 안에 reverse = True를 쓰면 거꾸로 정렬된다

# 정리
# append, insert, sort는 .을 쓰고 그 뒤에 쓴다 .append() .insert() .sort()라고 외우자 마치 .format()과 비슷한 것 같다
# del은 그냥 뒤에 리스트와 인덱스를 쓰면 된다
# sorted()는 리턴 처럼 값을 출력 대체한다기 보단 그냥 바꿔놓기만 한다. 그래서 그것을 지정연산자로 담거나 print하여야 한다
# len() 몇개가 들어있나





    # 리스트 예제(하나씩 출려해보시오)

greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

# 나의 코드

num = 0
while num <= 6:
    print(greetings[num])
    num += 1

# 고친 코드
    
num = 0
while num < len(greetings):
    print(greetings[num])
    num += 1

# 이러면 더 안정적이다 더 추가되어도 문제가 없으니까






    # return 복습!!!(갑자기 생각이 안난다...)

# return은 함수가 아니다 def랑 비슷한 종류(?)이다. 
# 그리고 리스트의 sorted와 마찬가지로 그 값을 출력하지는 않는다. 다만 리스트의 sorted는 함수다.





    # 단위 바꾸기 예제(리스트에 있는 값의 단위를 화씨에서 섭씨로 바꾸어야한다)

# 원래는 하나의 리스트를 가지고 차근차근 그 내용물을 바꾸려고 했었는데
# 대체하는 깔끔한 명령어가 없고 삭제했다가 다시 추가해야하니까 귀찮아서 새로운 리스트를 하나 더 만들어야겠다
    
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: {}".format(temperature_list))

new_temperature_list = []
index = 0

while index < len(temperature_list):
    new_temperature_list.append(fahrenheit_to_celsius(temperature_list[index]))
    index += 1
print("섭씨 온도 리스트: {}".format(new_temperature_list))

# 아니... 이거 뭔데 리스트의 값이 다 소수야;;;
# 모르겠어서 솔루션을 봤다

# 내가 놓친것 round() 라는 연산자가 있었는데 놓쳤다...

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: {}".format(temperature_list))

new_temperature_list = []
index = 0

while index < len(temperature_list):
    new_temperature_list.append(round(fahrenheit_to_celsius(temperature_list[index]), 1))
    index += 1
print("섭씨 온도 리스트: {}".format(new_temperature_list))

# 그리고 대체하는 것은 지정연산자로 해주면 되는데 그것도 놓쳤다





    # 환전 서비스(리스트의 가격은 원인데 달라와 엔화로 환전하기)(환율은 1달러에 1,000원, 그리고 1,000엔에 8달러)

def krw_to_usd(krw):
    return krw / 1000 


def usd_to_jpy(usd):
    return usd * 1000 / 8


prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))

i_1 = 0
while i_1 < len(prices):  
    prices[i_1] = round(krw_to_usd(prices[i_1]), 1)
    i_1 += 1

print("미국 화폐: " + str(prices))

i_2 = 0
while i_2 < len(prices):  
    prices[i_2] = round(usd_to_jpy(prices[i_2]), 1)
    i_2 += 1

print("일본 화폐: " + str(prices))

# 오 이번에는 문자열과 리스트를 동시에 출력하고 싶어서 리스트를 str로 문자열로 변환해 주고 + 연산자를 이용해서 할 수 있구나
# 이제 return의 용도를 정화하게 알겠다. return은 값을 동네방네 떠들고 싶지 않을 때 이용하는 거다. 
# 뒤에서 조용이 처리하고 싶을 때. 왜냐하면 print로 하게 되면 출력이 되어버리니까





    # 리스트 전체 복습 예제

'''리스트 함수를 활용하여 아래의 지시 사항을 따르세요.

numbers라는 빈 리스트를 만들고 리스트를 출력한다.
append를 이용해서 numbers에 1, 7, 3, 6, 5, 2, 13, 14를 순서대로 추가한다. 그 후 리스트를 출력한다.
numbers 리스트의 원소들 중 홀수는 모두 제거한다. 그 후 다시 리스트를 출력한다.
numbers 리스트의 인덱스 0 자리에 20이라는 수를 삽입한 후 출력한다.
numbers 리스트를 정렬한 후 출력한다.'''

# 나의 코드

numbers = []
print(numbers)

numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)

print(numbers)

i = 0
while i < len(numbers):
    if numbers[i] % 2 != 0:
        del numbers[i]
    else:
        pass
    i += 1
print(numbers)

numbers.insert(0, 20)
print(numbers)

numbers.sort()
print(numbers)

# 솔루션을 보니까 지웠을 때는 인덱스를 + 1안하는 방법으로 한다...
# 왜 이 생각을 못했을까...
# 그리고 else: pass를 안하고 그냥 else 자체를 안쓰는 거 같다. 근데 이건 취향이니까 괜찮을 것 같다.

# 지금 까지 공부한 내용으로 리스트에서 특정 객체를 판별하는 코드를 짜면 이런 식으로 나온다고 한다.

'''# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 12))'''

# 이 생각은 못했는데 정말 코딩은 어려운거 같다...

# 그러나 이런 식의 기능은 정말로 많이 필요로 해서 이미 파이썬에 내장되어 있다고 한다

test_1 = ["로봇", "동물"]

if "동물" in test_1:
    print("식물")

# 직관적이라서 좋다
    
test_2 = [["호랑이", "여우"], 300, "고릴라"]  # 리스트안의 리스트

print(test_2[0])

print(test_2[0][0])

# 아까 위에 .append() .insert() .sort()가 있었는데 .reverse() .index() .remove()도 있다(진짜 겁나 많네;;; 내일 복습해야겠다 적당히 많아야지;;;)

test_2.reverse()

print(test_2)
print(test_2.index(300))

# .index 앞에 리스트가 있어야 한다 방금 그거 실수해서 오류 하나 냄

test_2.remove("고릴라")

print(test_2)

# 그냥 지금 한번 정리해야겠다

'''
01. 리스트 슬라이싱 list[1:3]                     (자르기)
02. 리스트 지정연산자 list[2] = "love"            (대체하기)
03. 리스트의 요소 개수 len(list)                  (개수 파악)
04. 리스트에서 삭제 del list[1]                   (삭제하기)(인덱스 기반)
05. 리스트 정렬(리턴) sorted(list)                (정렬하기)
06. 리스트 정렬 list.sort()                       (정렬하기)
07. 리스트에 추가 list.append("love")             (추가하기)
08. 리스트에 추가 list.insert(0. "love")          (삽입하기)(어디에가 먼저 나와야 한다)
09. 리스트에서 삭제 list.remove("love")           (삭제하기)(요소 기반)
10. 리스트 뒤집기 list.reverse                    (뒤집기)(reverse = True랑 다름)
11. 리스트 겁색 list.index(300)                   (인덱스 찾기)
''' 

# 모아놓고 보니까 너무 많다... 이걸 다 외운다 보다는 그냥 계속 보면서 익숙해지는게 맞는 거 같다.





    # for 문

for i in [1,2,3]:
    print(i)

# while이랑 비슷하지만 살짝 다른 반복문
    
for i in range(10):
    print(i)

for i in range(3, 10):
    print(i)

for i in range(3, 10, 2):
    print(i)

# 이렇게 3가지 형식으로 사용가능한 range함수와 같이 쓰면 시너지 효과가 있다
    




    # range 예제(numbers의 인덱스와 원소를 출력)

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

x = 0
for i in numbers:
    print(f"{x} {i}")
    x += 1

# 간단하게 작성완료
    
# 모범답안...

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

for i in range(len(numbers)):  # 인덱스를 하나씩 불러는 for 문을 만들었네
    print(i, numbers[i])  # 그리고 변수라서 굳이 저렇게 format 형식을 사용할 필요가 없었네...





    # 거듭제곱 예제

for i in range(11):
    print(f"2^{i} = {2 ** i}")  # 간단하게 만들었다





    # 구구단 예제(대신 for 문을 이용한)

for i_1 in range(1, 10):
    for i_2 in range(1, 10):
        print(f"{i_1} * {i_2} = {i_1 * i_2}")  # 간단하네





    # 피타고라스 예제(a + b + c = 400을 만족하는 abc에 대하여 a * b * c는? 단 a < b < c)

# 어련다... 
        
# 결국 못 풀었다...
        
for a in range(1, 400):
    for b in range(1, 400):
        if a ** 2 + b ** 2 == (400 - a -b) ** 2 and a < b < 400 - a - b:
            print(a * b * (400 - a - b))

# 솔루션은 이거란다
# 결국에 for 문을 겹쳐서 쓰면 구구단 같은 문제를 쉽게 풀 수 있다는 것을 배웠다
        
