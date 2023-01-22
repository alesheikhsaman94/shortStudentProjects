def myfunc(number):
    if number % 2 ==0:
        print(f"{number} is even")
    elif number % 2 == 1:
        print(f"{number} is odd")

while True:
    number = int(input("please enter a number: "))
    myfunc(number)