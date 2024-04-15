#나와 상대방의 이름을 활용하여 사랑 점수 출력하는 계산기
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

name1_true_number = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")

name2_true_number = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

name_true_total = name1_true_number + name2_true_number


name1_love_number = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")

name2_love_number = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

name_love_total = name1_love_number + name2_love_number

love_score = str(name_true_total) + str(name_love_total)

love_score = int(love_score)

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")

combined_name = name1 + name2
lower_combined_name = combined_name.lower()

# true = lower_combined_name.count("t") + lower_combined_name.count("r") + lower_combined_name.count("u") + lower_combined_name.count("e")
t = lower_combined_name.count("t") 
r = lower_combined_name.count("r") 
u = lower_combined_name.count("u") 
e = lower_combined_name.count("e")

true = t + r + u + e

l = lower_combined_name.count("l") 
o = lower_combined_name.count("o") 
v = lower_combined_name.count("v") 
e = lower_combined_name.count("e")

love = l + o + v + e

total_score = str(true) + str(love)

total_score = int(total_score)

if (total_score < 10) or (total_score > 90):  #괄호는 가독성을 위해 쓴것이므로, 반드시 필요한게 아님
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (total_score >= 40) and (total_score <= 90):
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}.")