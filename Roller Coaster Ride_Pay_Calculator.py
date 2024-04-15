# Roller Coaster Ride 가능 여부와 Pay 에 대한 Calculator


# Multiple if문
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 #bill의 첫 가격 0을 선언해둔다.

if height > 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age<12:                        #Nested if/else(중첩 if/else) 첫 조건 통과한 것에만 두번째 조건을 걸고 싶을 때
    bill = 5 #사진 추가금액 시 bill 변수를 사용하기 위해 금액을 선언해둔다. bill += 5와 같틈
    print("Child tickets are &5.")
  elif age<=18:                  
    bill = 7 #12세 이상 18세 이하의 금액을 선언해둔다.
    print("Youth tickets are &7.")
  elif age >=45 and age <=55:   #Logical Operators(논리연산자) And를 사용하여 두가지 조건 모두 True일 경우 즉, 두가지 조건에 모두 부합할 경우에만 해당 코드를 출력하도록 함.     
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12 
    print("Adult tickets are &12.")
  wants_photo = input("Do you want a photo taken? Y or N. ") #들여쓰기 주의. 순서도 흐름 안에 있는 곳에 들여쓰기 해야함. 그렇지 않을경우 오류 발생.
  if wants_photo == "Y" or "y":
    bill += 3 #bill = bill + 3과 같음. 입력된 값이 해당되는 조건에 의해 bill변수의 값이 선정되었을 것임. 그것에 3을 더한 값이 새로운 bill변수가 되는 것.
# 주의할것. if문의 들여쓰기 위치 확인! 순서도의 흐름에 따라 들어갈 위치 확인할것.
# 또한 마지막 if문에 대한 동반 else문 작성할 필요 없음. 왜냐하면, N일경우 따로 수행해야할 condition(조건)이 없기 때문.

  print(f"Your final bill is &{bill}.") #들여쓰기 주의. 순서도 흐름에 맞는 if문 라인에 쓸것

else:
  print("Sorry, you have to grow taller before you can ride.")