
# import section10
# section10.price(3) # 3명이서 영화 보러 갔을 때 가격
# section10.price_morning(4)
# section10.price_soldier(5)

# import section10 as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


from section10 import *
# price(3)
# price_morning(4)
# price_soldier(5)

import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
