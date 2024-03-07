# 2024-03-07





    # 사전

dictionary = {
    "호랑이 다리": 4,
    "사람 다리": 2,
    "거미 다리": 8,
    "개미 다리": 6
}  # key - value라고 부른다 안에 있는 녀석들은

print(type(dictionary))  # 자료형은 dict이다

print(dictionary["개미 다리"]) 
print(dictionary["사람 다리"]) 

dictionary["다리미"] = 999999  # 이런 식으로 추가하기
print(dictionary["다리미"])

print(dictionary.values())
print(dictionary.keys())  # 리스트에서 부터 사전까지 명령어가 너무 많아서 머리가 아파온다... 그냥 계속 보면서 익숙해져야지 외울 수는 없겠다

if "거미 다리" in dictionary.keys():  # 이런 식으로도 활용 가능
    print("거리 다리 맛있어요")

for key in dictionary:  # .keys()랑 같은게 아니라 그냥 변수명을 key라고 지정했을 뿐이다
    print(key)

for key, value in dictionary.items():
    print(key, value)

# .keys() .values() .items()
    




    # 사전 뒤집기 예제(사전을 뒤집는 함수를 만들어라)

# 결국 만든 코드

def reverse_dict(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict

vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

print("영-한 단어장\n{}\n".format(vocab))

reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))

# \n은 원래 작성되어 있었는데 아마 엔터의 기능을 하는 듯하다
# 처음에는 사전에 담겨져있는 요소들을 하나씩 뽑아서 넣으려고 했다
# 그 다음에는 사전의 key를 다른 사전의 value에 넣으려고 했다
# 결국에는 .items()을 이용해서 한번에 뽑아 냈는데 이것도 s랑 ()를 안써서 오류가 2번이나 났다...
# 별로 어려운 예제는 아닌 것 같은데 너무 많이 해맸다.....





    # 투표 예제(몇 표인지 집계)

'''votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

i = 0
j = 0
k = 0

vote_counter = {'김영자': i, '강승기': j, '최만수': k}

for name in votes:

print(vote_counter)'''

# 아니 리스트에 변수를 어떻게 넣지? 안 배운것 같은데

# 솔루션을 봤다... 아니 이럴 때 사전을 쓰는구나 하... 너무 내가 못해 ㅠ





    # 이건 뭐지...?

first = [1, 2, 4, 6, 7]

second = first
second[4] = 500
print(first)

third = list(first)
third[4] = 50000000
print(first)

# 왜 이런지는 모르겠다 그냥 외우자... 리스트는 연동된다고 생각하자 사실 연동되는 거는 아니지만
# 그리고 리스트의 값을 연동시키지 않고 복사하려면 list() 항수를 사용하자





    # 문자열도 리스트처럼... 쓸 수 있다

apple = "apple"

print(apple[0])
print(apple[3])
print(apple[:4])
print(apple[2:])
print(apple[1:3])

# 아 맞다 슬라이싱할때 끝부분은 포함하지 않는 거였지 까먹었었다

print(len(apple))

# 이런 것도 되네 ㅎㄷㄷ
# for 반복문도 된다고 한다 
# 리스트도 + 연산자로 연결할 수 있다고 한다
# 웬만하면 거의 성질이 같다고 볼 수가 있다
# 차이점은 리스트는 중간만 딱 수정이 가능한데 문자열은 그런게 안된다는 것이다 





    # 자릿수 합 구하기

def sum_digit(num):
    i = 0
    total = 0
    while i < len(str(num)):
        total += int(str(num)[i])
        i += 1
    return total

total = 0
for i in range(1, 1001):  # 1부터 1000까지 하고 싶으면 range(1, 1001)으로 가야한다...
    total += sum_digit(i)
    
print(total)





    # 주민번호 가리기

def mask_security_number(security_number):
    if len(security_number) == 14:
        return security_number[0: 10] + "****"  # 슬라이싱을 이상하게 했다 (1, 11) 이렇게...
    else:
        return security_number[0: 9] + "****"  # 그리고 리턴하는게 깔끔한데 함수내에서 print를 하게 정의했다


print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))





      # 팰린드롬(is_palindrome은 파라미터 word가 팰린드롬이면 True를 리턴하고 팰린드롬이 아니면 False를 리턴합니다.)

# 1차 코드

def is_palindrome(word):
    if word == word.reverse(0:)
        return True
    else:
        return False

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

# 이런 식으로 전체를 뒤집어서 판단하려고 했는데 그런 기능은 없나보다 리스트에만 있나보다...



