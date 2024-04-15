# 알맞는 길을 찾아 보물찾기 하는 게임입니다.
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

choose_road = input(
    'You\'re on the road. Where do you want to go?. Type "Left" or "Right" or "Across the street". \n'
).lower()

if choose_road == "across the street":
  choose_mountain = input(
      'You\'ve come to the mountain. There is a house in the mountain top. \nType "Climbing" to climb the mountain. Type "Motorcycle" to climb on a motorcycle. Type "Wait" to wait for a Jeep car. \n'
  ).lower()

  if choose_mountain == "wait":
    choose_door = input(
        'You arrived at the top of the mountain house unharmed. \nThere are three doors. One is "Black", one is "Red", and one is "White". \nWhich color will you choose? \n'
    ).lower()

    if choose_door == "black":
      print("It's a Black Hole room. \n[Game Over]")
    elif choose_door == "red":
      print(
          "You found the treasure! This room is full of treasures. \n[[[You Win]]]"
      )
    elif choose_door == "white":
      print("It's a room full of fire. \n[Game Over]")
    else:
      print("You chose the door that doesn't exist. \n[Game Over]")

  elif choose_mountain == "motorcycle":
    print("The wheels of your motorcycle are missing. \n[Game Over]")

  elif choose_mountain == "climbing":
    print("You get attacked by a fierce tiger. \n[Game Over]")

  else:
    print("You're trapped in deep darkness. \n[Game Over]")

elif choose_road == "left":
  print("You suddenly fell into a sinkhole. \n[Game Over]")

elif choose_road == "right":
  print("You tripped over a stone. \n[Game Over]")

else:
  print("There's no road. \n[Game Over]")
