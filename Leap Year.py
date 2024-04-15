# 특정 연도가 윤년인지 확인하는 윤년 계산기 입니다.
year = int(input("Which year do you want to check? "))

if year%4==0:
  if year%100==0:
    if year%400==0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")