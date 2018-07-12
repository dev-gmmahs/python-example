# 1. 변수 선언 및 사용

# name 변수에 "홍길동" 문자열 대입
name = "홍길동"

# age 변수에 정수 10 대입
age = 10

# height 변수에 150.24 실수 대입
height = 150.24

# family 변수에 리스트 저장
family = ["엄마", "아빠", "누나"]

# score 변수에 딕셔너리 저장
score = {
    "국어": 98,
    "수학": 100,
    "영어": 82
}

# hands 변수에 튜플 저장
# 튜플은 값을 변경할 수 없습니다.
hands = (3, 7)



# ========== 출력하기 ========== #

# 쉼표로 구분하여 문자열, 변수 등을 출력할 수 있습니다
print("제 이름은", name, "이고, 나이는", age, "입니다.")

# 문자열의 format 메소드를 사용하여 간편하게 포맷이나 위치를 지정할 수 있습니다.
print("제 키는 {}cm 입니다.".format(height))

# end="" 는 print 후 어떤 글자를 출력할지 정할 수 있습니다.
# 기본값으로는 \n(개행) 문자입니다
print("그리고 저의 가족 구성원은 ", end="")
# 리스트나 튜플은 반복가능한 객체이므로 for문에서 사용할 수 있습니다.
for f in family:
    print(f, end=" ")
# len() 함수는 해당 객체의 길이를 반환합니다
print("이고 총 {}명 입니다.".format(len(family)))

# 딕셔너리.keys() 메소드는 해당 딕셔너리의 키 리스트를 반환합니다.
print("저의 이번 시험 성적은,")
for k in score.keys():
    print("{}점수: {}점".format(k, score[k]))
print("입니다.")

# 튜플이나 리스트는 인덱스를 통해 접근하여 사용할 수 있습니다.
print("마지막으로 저는 왼손과 오른손을 {}:{} 만큼 씁니다.".format(hands[0], hands[1]))
