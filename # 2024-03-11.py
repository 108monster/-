# 2024-03-11 프로젝트





    # 로또 프로젝트

'''규칙
로또는 주 1회 간격으로 당첨자를 발표합니다. 
참여 횟수에 제한이 없어서, 한 사람이 한 회차에 여러 번 참여할 수도 있습니다. 
고를 수 있는 번호는 1부터 45까지 있는데요. 
주최측에서는 매주 6개의 '일반 당첨 번호'와 1개의 '보너스 번호'를 뽑습니다. 
그리고 참가자는 참여할 때마다 서로 다른 번호 6개를 선택합니다. 
당첨 액수는 아래 규칙에 따라 결정됩니다.

내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치: 10억 원
내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치: 5천만 원
내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치: 100만 원
내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치: 5만 원
내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치: 5천 원'''





'''로또 시뮬레이션 프로그램을 한 단계씩 완성해 나갑시다.

먼저 main.py 파일의 generate_numbers() 함수를 작성하세요. 
이 함수는 파라미터로 정수 n을 받습니다. 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑고, 
그 번호들이 담긴 리스트를 리턴합니다. 참고로 이 함수는 참가자의 번호를 뽑는 데에도 쓰이고, 
보너스를 포함한 당첨 번호 7개를 뽑는 데에도 쓰입니다.'''

# 서로 다른 번호를 어떻게 뽑아??

'''힌트 3
리스트에 중복된 값을 추가하지 않도록 주의해 주세요. 
리스트 안에 특정 요소가 있는지 확인하는 in 키워드를 잘 활용해 보세요.'''

import random

def generate_numbers(n):
    list = []
    i = 0
    while i < n:
        number = random.randint(1, 45)
        if number in list:
            pass
        list.append(number)
        i += 1
    return list

# 왜 내 list 변수가 사전이 된거야...
# 아하 리스트는 대괄호구나 ㅋㅋㅋㅋ
# 아 그리고 함수를 정의하면 보통 리턴을 해줘야지 안하니까 불린값이 나오네

'''def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers'''

# 이게 모범 답안이다 좀 더 깔끔하긴 하네





'''main.py 파일의 draw_winning_numbers() 함수를 작성하세요. 
이 함수는 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다. 
일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다. 
앞서 정의한 generate_numbers() 함수를 잘 활용하면, 
함수를 간결하게 작성할 수 있습니다.'''

def draw_winning_numbers():
    answer_list = generate_numbers(6)
    answer_list.sort()
    number = random.randint(1, 45)
    if number not in answer_list:
        answer_list.append(number)
    return answer_list

# 간단하게 완성

'''def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]'''

# 와 겁나 간단하게 짜네;;; 어떻게 이렇게 코드를 짜지?
# 리스트 슬라이싱을 이런 식으로 이용할 수 있다는 것을 배우자





'''main.py 파일의 count_matching_numbers() 함수를 작성하세요. 
이 함수는 참가자가 뽑은 6개의 번호 리스트와 당첨 번호 6개의 리스트 중 몇 개의 숫자가 일치하는지 알려 주는 함수입니다. 
파라미터로 리스트 numbers와 리스트 winning_numbers를 받고, 
두 리스트 사이에 겹치는 번호 개수를 리턴합니다.'''

def count_matching_numbers(numbers, winning_numbers):
    i = 0
    for n in numbers:
        if n in winning_numbers:
            i += 1
    return i

# 너무 간단하게 코드 작성 완료





'''check() 함수를 작성하세요.'''

def check(numbers, winning_numbers):
    front_number = count_matching_numbers(numbers, winning_numbers[:6])
    back_number = count_matching_numbers(numbers, winning_numbers[6:])
    if front_number == 6:
        return 1000000000
    elif front_number == 5:
        if back_number == 1:
            return 50000000
        else:
            return 1000000
    elif front_number == 4:
        return 50000
    elif front_number == 3:
        return 5000
    else:
        return 0
    
# 이것도 간단하게 완료
    
my = generate_numbers(6)    
win = draw_winning_numbers()
print(f"당신의 번호는\n{my}입니다.\n\n정답번호는\n{win}입니다.\n\n{check(my, win)}원 당첨되셨습니다.")

i = 0
list_1 = []
while i < 999:
    my = generate_numbers(6)    
    win = draw_winning_numbers()
    list_1.append(check(my, win))
    i += 1
print(list_1)

# 천번해도 100만원이 당첨이 안되네 ㅎㄷㄷ

i = 0
while True:
    my = generate_numbers(6)    
    win = draw_winning_numbers()
    if check(my, win) == 1000000000:
        print(i)
        break
    i += 1

# 평균적으로 10만번 로또를 사야 10억이 당첨될까 말까네
    
print(100000 * 5000)





    # 숫자야구 프로젝트

from random import randint


def generate_numbers():
    numbers = []
    i = 0
    while i < 3:
        num = randint(0,9)
        if num in numbers:
            continue
        numbers.append(num)
        i += 1
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    i = 1
    new_guess = []
    while i < 4:
        num = int(input(f"{i}번째 숫자를 입력하세요: "))  # input으로 받아들이는 모든 것은 문자열
        if 0 > num or num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue
        new_guess.append(num)
        i += 1
    return new_guess
    
    
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    i = 0
    while i < 3:
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1
        i += 1
    return strike_count, ball_count  # 두 값을 동시에 리턴하면 두개를 동시에 담을 수가 있다


answer = generate_numbers()
tries = 0

while True:
    guess = take_guess()
    s, b = get_score(guess, answer)
    print(f"{s}S {b}B")
    tries += 1
    if s == 3:
        print(f"축하합니다. {tries}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.")
        break  # 마지막에 break를 깜빡했네





    # reverse

# list에서만 쓸 수 있고 문자열에서는 쓸 수 없다
# 대신 len은 문자열에서도 쓸 수가 있다 