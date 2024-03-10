# 2024-03-10





    # 파일 불러오기

'''with open('pile.txt', 'r') as p:'''
# 파일이 파이썬 파일과 같은 폴더에 있으면 그냥 파일명 + 확장자만
# 파일이 같은 폴더에 있지 않으면 경로를 다 써주어야함
# 'r'은 파일을 읽는다는 뜻 'w'는 파일을 쓰겠다는 뜻
# as p는 p라는 변수에 파일을 저장하겠다는 뜻
# for 문으로 사용하면 파일의 각 줄이 순서대로 리턴됨
# **** 그냥 프린트는 못함 ㅎㄷㄷ 형이 리스트도 아니도 사전도 아니고 문자열도 아니여서 ****





    # 화이트 스페이스를 다루는 법

# print()를 하면 자동으로 엔터가 쳐진다 \n
# input()을 하면 자동으로 엔터가 안쳐진다. 대신 사용자가 치게 된다
'''input("응애")
print("응")
input("야옹")'''
# 아까 텍스트파일을 불러와서 for 문으로 사용하면 자동으로 \n이 되는데
# 이걸 없애고 싶으면 p.strip()을 입력한다
# 그러면 앞뒤의(중간 제외)화이트 스페이스가 전부 사라진다
# 데이터 분석에서 정말 많이 쓴다





    # .split()

# 문자열을 리스트로 만들어 준다 찢어서
# 파라미터를 남기면 .split(",") 이걸 기준으로 찢어준다(", "이런식으로 스페이스를 없앨수도 있다)
# 파라미터를 안 남기면 그냥 화이트 스페이스를 기준으로 찢어준다
# split을 이용해서 리스트를 만들면 그 값은 항상 문자열로 저장된다

my_name = "Yoon, Minjoon"
my_name_list = my_name.split(", ")
print(my_name_list)

# split도 많이 쓰인다고 한다 데이터 분석에서





    # 파일 불러오기 예제(평균 매출 구하기)

'''with open("data/chicken.txt", "r") as sales:
    i = 0
    total_cash = 0
    for line in sales:
        day_sales = line.strip().split(": ")
        total_cash += int(day_sales[1])
        i += 1
print(total_cash / i)'''

# split한 day_sales 리스트의 1번 인덱스를 더할 때 int로 형변환을 해주었어야 했는데 놓쳤다





    # 파일 쓰기

'''write open("new_file.txt", "w") as p:
    p.write("우히우히히\n")
    p.write("방가방가")'''

# 이러면 new_file.txt 파일이 생기고 거기에 우히우히히를 입력한다
# 다만 write함수에는 엔터기능이 없으므로 \n을 쳐주었다
# "w"는 덮어쓰기가 기본으로 되어있어서 저 파일에 마지막 것을 덮어쓴다

'''write open("new_file.txt", "a") as p:
    p.write("우히우히히\n")
    p.write("방가방가")'''

# 차이점은 "a"로 되어있다는 점이다
# a는 append를 나타낸다 추가한다는 뜻이다
# 이러면 코드를 실행할 때마다 추가된다
# 물론 파일 자체가 없으면 파일을 만들고 한번만 적히게 된다





    # 단어장 만들기 예제

'''영어 강사 Coy는 학생들의 단어 암기를 위해 단어장 프로그램을 만들려고 합니다.
이 프로그램은 콘솔로 영어 단어와 한국어 뜻을 받고,
vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리하는데요.
사용자가 새로운 단어와 뜻을 입력할 때마다 vocabulary.txt에 작성되는 것입니다.
사용자는 반복적으로 단어와 뜻을 입력하는데, 단어나 뜻으로 q를 입력하는 순간 프로그램은 즉시 종료됩니다.
사용자가 q를 입력하고 나면 파일은 더 이상 바뀌지 않아야 합니다.'''

with open("c:/Users/yoons/OneDrive/문서/GitHub/desktop-tutorial/vocabulary.txt", "a") as p:
    while True:
        english = input("영어 단어를 입력하세요: ")
        if english == "q":
            break
        korean = input("한국어 뜻을 입력하세요: ")
        if korean == "q":
            break
        p.write(f"{english}: ")
        p.write(f"{korean}\n")

# 와 잘 만들었다 ㅋㅋㅋ 이제 진짜 실용적인 것들을 만들어서 좋다
# 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX
# 이런 오류가 떴었는데 이거는 이제 파일 경로를 복사 붙여넣기해서 그런거고
# \를 /로 바꾸기만 하면 해결된다
# 여기서 추가하면 좋은 점은 p.write를 2번 쓸게 아니라 한번만 쓰는 것이다
        
'''영어 단어를 입력하세요: mom 
한국어 뜻을 입력하세요: 엄마
영어 단어를 입력하세요: dad
한국어 뜻을 입력하세요: 아빠
영어 단어를 입력하세요: love
한국어 뜻을 입력하세요: 사랑하다
영어 단어를 입력하세요: guilt
한국어 뜻을 입력하세요: 죄를 짓다
영어 단어를 입력하세요: q'''

# 콘솔에서는 이런 식으로 나오고

'''mom: 엄마
dad: 아빠
love: 사랑하다
guilt: 죄를 짓다'''

# 메모장에는 이렇게 나온다





    # 만든 단어장을 활용하여 퀴즈내기 예제

with open("c:/Users/yoons/OneDrive/문서/GitHub/desktop-tutorial/vocabulary.txt", "r") as p:
    for line in p:
        splited_list = line.strip().split(": ")
        answer = input(f"{splited_list[0]}: ")
        if answer == splited_list[1]:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {splited_list[1]}입니다.")

'''영어 단어를 입력하세요: happy
한국어 뜻을 입력하세요: 행복하다
영어 단어를 입력하세요: shy 
한국어 뜻을 입력하세요: 부끄럽다
영어 단어를 입력하세요: q
happy: 행복하다
아쉽습니다. 정답은 행복하다
입니다.
shy:'''

# 뭐야 왜이래 뭔가 화이트 스페이스 문제 같으니까 위 코드에 strip을 추가했다

'''영어 단어를 입력하세요: replay
한국어 뜻을 입력하세요: 다시보기
영어 단어를 입력하세요: banana
한국어 뜻을 입력하세요: 바나나
영어 단어를 입력하세요: alone
한국어 뜻을 입력하세요: 혼자
영어 단어를 입력하세요: lonely
한국어 뜻을 입력하세요: 외로운
영어 단어를 입력하세요: sad
한국어 뜻을 입력하세요: 슬픈
영어 단어를 입력하세요: lava
한국어 뜻을 입력하세요: 용암
영어 단어를 입력하세요: q
happy: 행복하다
맞았습니다!
shy: 부끄럽다
맞았습니다!
replay: 다시봅기
아쉽습니다. 정답은 다시보기입니다.
banana: 바나나
맞았습니다!
alone: 혼자
맞았습니다!
lonely: 외루운
아쉽습니다. 정답은 외로운입니다.
sad: 새드
아쉽습니다. 정답은 슬픈입니다.
lava: 용암
맞았습니다!'''

# 완성!!!





    # 고급 단어장 예제

'''지난 실습 과제에서 단어장 퀴즈 프로그램을 만들었는데요.
학생들이 문제의 순서가 매번 똑같아서 재미가 없다고 합니다.
이번에는 random 모듈과 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 문제를 내도록 프로그램을 바꿔 보세요.
같은 단어를 여러 번 물어봐도 괜찮고,
프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행됩니다.'''

# 흠... 랜덤은 이용할 수 있을것 같은데 사전을 어떻게 이용하지?
# 근데 랜덤을 사용하려면 사전을 쓰기는 해야겠다
# 사전은 잘 모르는데;;; 까먹었는데
# 사전 부분을 다시 보고 와야겠다

'''# 사전(2024/03/07)

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

# .keys() .values() .items()'''

# (dictionary["다리미"] = 999999) 우선 이렇게 사전으로 다 옮긴다 for로
# 그 다음 value[key] == input인지 확인으로 정답 판별
# 랜덤은 흠... 사전에도 인덱싱이 있다면 해볼만 한것 같은데

'''with open("c:/Users/yoons/OneDrive/문서/GitHub/desktop-tutorial/vocabulary.txt", "r") as p:
    dic = {}
    for line in p:
        splited_list = line.strip().split(": ")
        dic[splited_list[0]] == splited_list[1]
    import random  # import 하고 :가 있었나? 기억이 안나네
    while True:
        i = randint(1, len(dic))'''

# 아 모르겠다. 사전이랑 랜덤을 어떻게 엮어야 될지 모르겠다

    
    
    
    
    # 솔루션
        
# 음... 사전은 사전대로 만들고 사전에서 keys들만 뽑아서 거기다가 인덱스를 붙인다
# 그러면 랜덤으로 처리 가능. 근데 궁금한게....
        
vocab = {
    "호랑이": "어흥",
    "고양이": "야옹"
}
keys = list(vocab.keys())
print(type(keys))
print(vocab.keys())

# 아 여기서 리스트로 바꿔주는 이유가 다 있구나
# 난 키만 뽑아내면 그게 리스트가 되는 줄 알았는데 그게 아니라
# dict_keys(['호랑이', '고양이'])라는 type이 되는 거구나

# 아무튼 이런 식으로 만들면 나오긴 할 거다

 


