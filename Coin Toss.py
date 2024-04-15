#random module을 사용한 random 동전 던지기
import random

print("Welcome to the virtual coin program.")
start = input('If you want to start a game, Type "Start". ').lower()

if start == "start":
 toss = random.randint(0,1)
 if toss == 0:
   print("Tails")
 else:
   print("Heads")
else:
  print("Okay. See you next time.")
