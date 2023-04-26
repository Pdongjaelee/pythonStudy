class Unit:
    def __init__(self):
        print("Unit 생성자")
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() # 2개 이상의 부모 클래스를 다중 상속을 받을 때는 순서상에 맨 마지막에 상속받는 클래스는 init 함수가 호출된다.
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()


