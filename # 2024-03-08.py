# 2024-03-08





    # 팰린드롬 예제(is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴하고 팰린드롬이 아니면 False를 리턴합니다.)

# 1차 코드

'''def is_palindrome(word):
    if word == word.reverse(0:)
        return True
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))'''

# 이런 식으로 전체를 뒤집어서 판단하려고 했는데 그런 기능은 없나보다 리스트에만 있나보다...

'''def is_palindrome(word):
    i = 0
    while i < len(word) // 2:
        if word[i] == word[len(word) - i]:
            pass
        else:
            return False
    return True
    
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))'''

# 이게 왜 안되는 거지...?

'''def is_palindrome(word):
    for i in word:
        if i == len(word) - i - 1:  # 심지어 여기서 -1도 안함 물론 그게 코딩의 실수는 아니지만
            pass
        else:
            return False
    return True
    
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))'''

# 아니 이것도 왜 안돼!!!
# 타입이 문제라는 것 같은데...
# 아 지금 숫자랑 문자를 비교하고 있었네

word_100 = "왜안돼"
print(word_100[1])  # 아니 이거 되는데...

# 아 i 자체가 문자구나... 하...
# 모르겠다 솔루션 봐야겠다

# 솔루션

def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True 

# for 문은 맞았는데 역시나 i에 문자가 담기며 안되는 거였구나 웬만하면 숫자가 담기게 세팅하자
# 아 그리고 2로 버림나눗셈하는 것도 맞았는데...
# 이렇게 보니 그렇게 어렵지가 않은데 왜 못했을까 ㅠ





    # 모듈

# 모듈을 불러와서 import하는 것

# import numpy as np
# 이렇게 쓴다고 한다 근데 왜 안 불러와지지? 같은 폴더안에 없어서 그런가





    # 표준 라이브러리(맛보기)

import math  # math 수학 라이브러리
print(math.cos(math.pi))

import random  # random 램덤 숫자 뽑아내는 라이브러리
print(random.random())
print(random.randint(10, 30))
print(random.uniform(0, 1))

import os  # 운영체제 관련 라이브러리
print(os.getlogin())
print(os.getcwd())

import datetime  # 날짜 관련 라이브러리
some_day = datetime.datetime(2024, 3, 8, 3, 18, 59)
print(some_day)
now = datetime.datetime.now()
print(now)
print(now - some_day)
print(now.strftime("%Y %B %dth %a"))  # 포맷코드로 표현하는데 포맷코드가 너무 많다...

# 이제 슬슬 재밌어진다 ㅋㅋㅋ





    # input 함수

num = input("숫자를 입력하시오: ")  # 갑을 받아서 리턴함(항상 문자열로)
print(f"{num}을 입력하셨군요")





    # 숫자 맞히기 게임

'''프로그램을 실행하면 기회가 *번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:가 출력됩니다.
총 네 번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회가 줄어듭니다.
정답을 맞히면 축하합니다. *번 만에 숫자를 맞히셨습니다.가 출력되고 프로그램은 종료됩니다.
사용자가 입력한 수가 정답보다 작은 경우 Up이 출력되고, 입력한 수가 정답보다 큰 경우 Down이 출력됩니다.
정답이 틀렸으면 1번부터 다시 진행합니다.
만약 네 번의 기회를 모두 사용했는데도 답을 맞히지 못했으면, 아쉽습니다. 정답은 *입니다.가 출력되고 프로그램은 종료됩니다.'''
import random
i = 4
answer = random.randint(1, 20)
guess = int(input(f"기회가 {i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
while i > 1: 
    if guess > answer:
        print("DOWN")
        i -= 1
    elif guess < answer:
        print("UP")
        i -= 1
    else:
         print(f"축하합니다. {5 - i}번 만에 숫자를 맞히셨습니다.")
         break
    guess = int(input(f"기회가 {i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
if i == 1:
    print(f"아쉽습니다. 정답은 {answer}였습니다.")

# 와... 내가 만들었지만 진짜 잘 만들었다 ㅎㄷㄷ
    
    