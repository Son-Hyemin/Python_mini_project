
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip = bill*(tip_percentage/100)

people = float(input("How many people to split the bill? "))
each_pay= round((bill+tip)/people,2)
each_pay = "{:.2f}".format(each_pay) #:.2f형식을 이용하여 문자열을 만든 뒤 format()function에 each_pay전달함.이는 float인 each_pay를 문자열로 바꿔준 것이고 :.2f로 인해 문자열은 소수점 이하 둘째자리까지의 특정 형식을 취함.
result = f"Each person should pay: ${each_pay}"
print(result)
