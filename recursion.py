# find sum of digits of a number
import math


def sumOfDigits(n):
    numbers = str(n)
    sum = 0
    for items in numbers:
        sum += int(items)
    return sum


# using recursion

def ssoodigit(n):
    if n <= 0:
        return 0
    else:
        return n % 10 + ssoodigit(math.floor(n/10))


# nth power of a number using recursion

def nthPower(n, p):
    if p == 1:
        return n
    elif p == 0:
        return 1
    else:
        return n * nthPower(n, p-1)


# greatest common devisor using euclidean algorithm
def GCF(n1, n2):
    if n2 == 0:
        return n1
    else:
        return GCF(n2,  n1 % n2)


binaryCode = []
# decimal to binary


def decTobinary(n):

    if n == 0:
        pass
    else:
        re = n % 2
        decTobinary(int(n/2))
        binaryCode.append(re)

    return binaryCode


print(decTobinary(13))
