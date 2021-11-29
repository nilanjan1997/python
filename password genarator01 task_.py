import random
import string
print('////Genarate The Password Dude//// %')
length = int(input('\nGive me a range dude: '))
small = string.ascii_lowercase
caps = string.ascii_uppercase
numbers = string.digits
symbol= string.punctuation
add = small + caps + numbers + symbol
genarate= random.sample(add, length)
passward = "".join(genarate)
print(passward)