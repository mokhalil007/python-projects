import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

character_number = input("enter number of characters for your password : ")

while True:
  try:
    character_number = int(character_number)
    if character_number < 6:
      print("at least it should be equal or above 6 ")
      character_number = input("lets try again : ")
    else:
      break
  except:
    print("please only enter a number in here! ")
    character_number = input("try again : ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part_one = round(character_number * (30 / 100))
part_two = round(character_number * (20 / 100))

password = []

for i in range(part_one):
  password.append(s1[i])
  password.append(s2[i])

for i in range(part_two):
  password.append(s3[i])
  password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:])

print(password)
