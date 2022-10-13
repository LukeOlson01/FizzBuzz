x = 1
while x < 101:
    number = True
    if x % 15 == 0:
        print('FizzBuzz')
        number = False
    if x % 3 == 0:
        print('Fizz')
        number = False
    if x % 5 == 0:
        print('Buzz')
        number = False
    if number == True:
        print(x)
    x += 1
