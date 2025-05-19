s = [input() for _ in range(3)]
for i, v in enumerate(s):
    if v not in ['Fizz', 'Buzz', 'FizzBuzz']:
        result = int(v) + (3 - i)
        if result % 3 == 0 and result % 5 == 0:
            print('FizzBuzz')
        elif result % 3 == 0:
            print('Fizz')
        elif result % 5 == 0:
            print('Buzz')
        else:
            print(result)
        break