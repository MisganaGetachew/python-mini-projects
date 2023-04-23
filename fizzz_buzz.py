# fizz_buzz interview question
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizzBuzz"
    elif input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"
    else:
        return input


while 123:
    number = float(input("insert a number: "))
    print(fizz_buzz(number))
