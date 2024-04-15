#random으로 계산할 사람 뽑기
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(
    ",")  #input으로 입력된 이름이 split(",")에 의해 나눠지며 이름 리스트에 포함됨.

import random

num_items = len(names)
random_num_items = random.randint(0, num_items - 1)
#인덱스는 전체 항목의 수보다 하나 작음. 인덱스는 0에서부터 시작하기 때문.
who_will_pay = names[random_num_items]
print(who_will_pay + " is going to by the meal today!")
