# 3. 반복문

i = 0
while i < 5:
    print("while 반복", i)
    i += 1


# 0 ~ 9
for data in range(10):
    print("for_1 반복", data)


# 5 ~ 10
for data in range(5, 11):
    print("for_2 반복", data)


# 0 ~ 10, 2씩 증가하면서
for data in range(0, 11, 2):
    print("for_3 반복", data)


# 반복 가능한 객체는 for 문에서 사용 가능
for data in ["a", 32, "안녕", [1, 2, 3]]:
    print("for_4 반복", data)


# 튜플도 반복가능한 객체
for data in (1, 2, 3):
    print("for_5 반복", data)

