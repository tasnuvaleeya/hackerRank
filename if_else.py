
def easy_problem(n):
    if n % 2 != 0:
        print('Weird')
    elif (n % 2 == 0 and n in range(2, 5)) or (n % 2 == 0 and n > 20):
        print('Not Weird')
    elif n % 2 == 0 and n in range(6, 20):
        print('Weird')
    else:
        print('Not valid')
print(easy_problem(8))
