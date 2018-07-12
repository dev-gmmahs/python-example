# 5. 클래스

# 클래스는 설계도와 같은 개념
# self는 Java, C# 등에서 this 와 같음
class human:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("제 이름은 {}입니다.".format(self.name))

# 클래스를 통해 객체(인스턴스) 생성
h1 = human("홍길동")
h2 = human("홍길순")

# 생성된 객체는 각자 독립성을 가지고 있다
h1.print_name()
h2.print_name()




class life:
    def __init__(self):
        self.life = True

# 클래스 정의시 () 안에 다른 클래스 명을 추가하면 상속
# animal 클래스는 life 클래스를 상속한다
class animal(life):
    def __init__(self):
        # 부모(life)클래스의 __init__ 호출
        life.__init__(self)

    def hasLife(self):
        # 부모(life)클래스에 있는 속성
        return self.life

tiger = animal()
print("tiger 인스턴스의 life:", tiger.hasLife())

# 상속되어 만들어진 tiger 인스턴스는 부모(life), 자식(animal) 클래스 모두의 인스턴스
print("tiger 인스턴스는 life 클래스의 인스턴스?", isinstance(tiger, life))
print("tiger 인스턴스는 animal 클래스 인스턴스?", isinstance(tiger, animal))
