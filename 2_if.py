# 2. 조건문 if 사용법

a = 10
b = 12
if a is b:
    print("a와 b는 같습니다")
else:
    print("a와 b는 다릅니다")



str1 = "안녕"
str2 = "안녕"
# is 또는 == 
if str1 is str2:
    print("str1와 str2는 같습니다")
else:
    print("str1와 str2는 다릅니다")



user_id = "asd1234"
user_password = ""
if not (user_id and user_password):
    print("아이디와 패스워드 모두 입력해주세요!")



new_id = "a123"
if len(new_id) < 6:
    print("아이디는 6자리 이상으로 해주세요!")
