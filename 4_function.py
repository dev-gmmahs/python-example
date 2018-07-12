# 4. 함수

# 함수 선언은 def 키워드로 선언한다
def sum(a, b):
    return a + b

print("sum(4, 5) 결과:", sum(4, 5))



# 함수 내에서 선언한 변수는 지역변수이므로
# 외부 변수와 별개로 사용 됨
a = 10
def scope():
    a = 20
    print("scope 함수 안:", a)
scope()
print("scope 함수 밖:", a)



# global 키워드를 통해 전역변수를 참조할 수 있다
def global_test():
    global a
    a = 20
    print("global_test 함수 안:", a)
global_test()
print("global_test 함수 밖:", a)
