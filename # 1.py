# 2024/3/3 공부

  # 숫자열은 정수 & 정수 계산만 정수로 출력

# 덧셈
print(3 + 8)
print(3.0 + 7.0)
print(6.2 + 9)

# 뺄셈
print(3 - 9)

# 곱셈
print(3 * 9.0)

# 나머지
print(4 % 6.0)

#버림 나눗셈
print(3 // 4)
print(100 // 3)

# 거듭제곱
print(2 ** 4)

# 반올림
print(round(2.3337))
print(round(3.2224), 2)

# 나눗셈(항상 소수)
print(2 / 3)
print(3 / 1)

  # 문자열

print("안녕")
print("'안녕'")
#print(""안녕"")
print("안녕" * 4)
#print("안녕" * 4.0)
print("안녕" + "하쇼")
print("4" + "45")
print("'사과는'   " + '"맛있다"')

  #형변환(그냥 상식적으로 하면 오류 안 난다)

print(int(2.0))
print(int(2.924)) #그냥 버린다
print(float(2))
print(float(3))
print(int("2"))
#print(int("2.0"))
print(float("2"))
print(float("2.3"))
print(str(3) + str(4))
#print(int("초코바"))

  #변수(논리적인 형변환이면 오류는 안 나는 듯)

a = 1
b = 2.0
c = "3"

print("안녕" + str(a) + str(b) + c)
print(a + b + int(c))
print(a + int(b) + int(c))
print(a + int(b) + float(c))

  #.format(노가다 방지, 결국에는 문자열이 됨)

age = 32
luck = 777

print("나이는 {}살이고 행운력은 {}이다.".format(age, luck))
print("나이는 {}살이고 행운력은 {}이다." . format(age * 2, luck))

gogogo = "나이는 {}살이고 행운력은 {}이다."

print(gogogo.format(age, luck + 1))

print("{0}은 {1}이다.".format(age, luck))
print("{1}은 {0}이다.".format(age, luck))
print("{1}은 {0:.4f}이다.".format(age, luck))

# 재미있는 부분 0:.4f (0 = 순서) (: = 속성) (.4f = 소수점 4째 자리 까지)

  # 포매팅의 3가지 방법(포매팅은 전부 큰따옴표 안에서)

name = "갑돌이"
num = 1

# 1. %s $d
print("%s는 %d이다." % (name, num))

# 2. "dadadad" . format
print("{}는 {}이다." . format(name, num))

# 3. f"dadadad"
print(f"{name}은 {num}이다.")
 