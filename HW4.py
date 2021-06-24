import random


def dec(func):
    for i in range(7):
        func()

@dec
def func1():
    arg = random.randint(0,101)
    print(f'Ваше случайное число - {arg}')
    