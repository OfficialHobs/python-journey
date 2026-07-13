print('press + for additon')
print('press - for subtraction')
print('press * for multiplication')
print('press / for division')
option = (input('select an operation: '))


if (option in ['+', '-', '*', '/']):
    num1 = float(input('enter first number: '))
    num2 = float(input('enter second number: '))

    if (option == '+'):
        result = num1 + num2
    elif (option == '-'):
        result = num1 - num2
    elif (option == '*'):
        result = num1 * num2
    elif (option == '/'):
        result = num1 / num2
    print('your answer is {}'.format(result))
else:
    print('invalid operation')

