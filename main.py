"""""שאלה 4"""


def printNumbers(start, end, Disappeared):
    if end <= 0:
        if start != end - 1:
            if start != Disappeared:
                print(start)
            return printNumbers(start - 1, end, Disappeared)

    if end > 0:
        if start != end + 1:
            if start != Disappeared:
                print(start)
            return printNumbers(start + 1, end, Disappeared)


# printNumbers(-3, 7,-1 )

""""שאלה 1"""


def factorSum(number):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if number <= 1:
        return 0

    sum_factors = 0
    factors_list = []

    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            sum_factors += i
            factors_list.append(i)

    print("Sum of prime factors:", sum_factors)
    print("Prime factors list:", factors_list)


# factorSum(221)

""""שאלה 2"""


def onlyPositive(f1):
    g = onlyPositive(f1)


    print(g(-2))
def f1(x):
    if x < 0:
        x *= -1
    return x



""""שאלה 3"""
def interceptPoint(line1, line2):
    a1, b1 = line1
    a2, b2 = line2
    tx = a1 - a2
    if tx == 0:
        return None
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return x, y

print(interceptPoint((5, 4), (5, 4)))
"""""שאלה 5"""
def listProduct(list1,list2):
    new_list=[]
    for i in range(0,len(list1)):
        temp=list1[i]
        for j in range(0,temp):
            new_list.append(list2[i])

    print(new_list)

listProduct([1,5,10],[4,5,9])
"""שאלה 6"""
def analyze(list):
    counter=0
    for i in range(len(list)):
        if list[i]>=85:
            counter+=1
    return counter
# print(analyze([90,44,86,85.1,94,3,22,85]))


