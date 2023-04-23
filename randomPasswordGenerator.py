#random password generator
import random
letterNumber = int(input("letters needed in your password: "))
symbolNumber = int(input("symbols needed in your passoword: "))
number = int(input("numbers needed in your password: "))

letters = []

def letter(letterNumber):
            letr = ""
            for x in range(letterNumber):
                temp  = random.randint(97, 122)
                letr += chr(temp)


            return  letr

def symbol(symbolNumber):
            letr = ""
            for x in range(symbolNumber):
                temp  = random.randint(33, 47)
                letr += chr(temp)


            return  letr

def Number(number):
            letr = ""
            for x in range(number):
              temp = random.randint(0, 10)
              str(temp)
              letters.append(temp)                


            return  letters

length = letterNumber + number + symbolNumber

# password = random.sample((Number(number)+ symbol(symbolNumber) + letter(letterNumber)), length )
passNum = Number(number)
passNum1 = "".join(str(x) for x in passNum)
password = random.sample((passNum1 + symbol(symbolNumber) + letter(letterNumber)), length ) #channge to random.shuffle since its is the rigt way
print(f'your password is { "".join(password)}')
