import string
import random

#pasword length
letter=int(input('Quantity of Alphabet= '))
special=int(input('Quantity of Special Charactor= '))
numerical=int(input('Quantity of number= '))

#password character type
alphebat = random.choices(string.ascii_letters,k=letter)
charactor = random.choices(string.punctuation,k=special)
number = random.choices(string.digits,k=numerical)
#pasword shuffling
#password=random.choices(string.ascii_letters,k=letter)+random.choices(string.digits,k=special)+random.choices(string.punctuation,k=special)
password = (alphebat + charactor + number)
password=''.join(password)
#password = random.shuffle(password)


#print password
print(f'Your length of password is {letter+numerical+special}')
print(f'Your pasword is {password}')

