#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for i in range(nr_letters):
  password += random.choice(letters)
for i in range(nr_numbers):
  password += random.choice(numbers)
for i in range(nr_symbols):
  password += random.choice(symbols)
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password2 = ""
for j in range(0, 1000):
  rand = random.randint(0,2)
  if (nr_letters == 0 and nr_numbers == 0 and nr_symbols == 0):
    break
  elif rand == 0 and nr_letters != 0:
    password2 += random.choice(letters)
    nr_letters -= 1
  elif rand == 1 and nr_numbers != 0:
    password2 += random.choice(numbers)
    nr_numbers -= 1
  elif rand == 2 and nr_symbols != 0:
    password2 += random.choice(symbols)
    nr_symbols -= 1
print(password2)
password_list=list(password)
random.shuffle(password_list)
password3 = ""
for char in password_list:
  password3 += char
print(password3)