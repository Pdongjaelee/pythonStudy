###section8 클래스


## 클래스

# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린"
# hp = 40
# damage = 5
#
# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))
#
# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
#
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( \
#         name, location, damage))
#
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

from  random import *

#일반 유닛
class Unit:
    def __init__(self, name, hp, speed): #def가 함수
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location, self.speed))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)


# 클래스 외부에서 내가 원하는 변수에 대해서 확장할 수 있다. 확장된 변수는 내가 확장한 객체에 대해서만 적용되고 기존에 있던 다른 객체에는 적용 안된다.
# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wrath1 = Unit("레이스", 80, 5)

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
# 레이스 유닛 추가
# wrath2 = Unit("빼앗은 레이스", 80, 5)
# wrath2.clocking = True
#
# if wrath1.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wrath2.name))


## __init__ 파이썬의 생성자, 함수에 정의된 값들은 똑같이 작성해야 객체를 만들 수 있다.


## 멤버 변수
# 위에 self.name, self.hp, self.damage 가 멤버변수가 된다.


## 메소드
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
              .format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가.
    seize_developed = False # 시즈모드 개발여부
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.set_seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.set_seize_mode() == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
#
# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


## 상속


## 다중 상속

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃/ 탱크 등을 수송. 공격 x

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyavleAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, flying_speed) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): #메소드 오버라이딩 -> 일반 유닛의 move()를 공중 유닛에서 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 레이스
class Wraith(FlyavleAttackUnit):
    def __init__(self):
        FlyavleAttackUnit.__init__("레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True: # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else: # 클로킴 모드 해제 -> 모드 설정
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")
# 실제 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음

# 게임 종료
game_over()



# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyavleAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")


## 메소드 오버라이딩

# 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)
#
# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
# battlecruiser = FlyavleAttackUnit("배틀크루저", 500, 25, 3)
#
# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")


## pass
#건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 일단 넘어가는 것, 일단 함수를 완성된 것처럼 보이게 한다.

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")




## super

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0)
#         self.location = location