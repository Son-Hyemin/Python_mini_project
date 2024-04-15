print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size=="S":
  bill = 15  #bill += 15 로 입력해도 무방.
  if add_pepperoni=="Y":
    bill += 2
elif size=="M":
  bill = 20
  if add_pepperoni=="Y":
    bill +=3
else:
  bill = 25
  if add_pepperoni=="Y":
    bill +=3

if extra_cheese == "Y":
  bill +=1

print(f"Your final bill is: &{bill}.")


bill = 0
if size=="S":
  bill = 15  #bill += 15 로 입력해도 무방.

elif size=="M":
  bill = 20

else:       #else문이 필수가 아니기 때문에, 명확히 보고싶다면 elif size =="L"로 써도 됨.
  bill = 25

if add_pepperoni=="Y":
  if size=="S":
    bill +=2
  else:
    bill +=3


if extra_cheese == "Y":
  bill +=1

print(f"Your final bill is: &{bill}.")