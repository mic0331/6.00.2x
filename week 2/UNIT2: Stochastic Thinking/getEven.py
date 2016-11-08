import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    number = random.randint(0, 99)

    while number % 2 != 0:
        number = random.randint(0, 99)
    return number

print(genEven())


# There are many good answers to this problem, some easier than others :)
def genEven():
    return random.randrange(0, 100, 2)

def genEven():
    return random.choice(range(0, 100, 2))

def genEven():
    return int(random.random() * 50)*2

def genEven():
    return random.choice(range(0, 50))*2

def genEven():
    x = random.randint(0, 98)
    while x % 2 != 0:
        x = random.randint(0, 98)
    return x