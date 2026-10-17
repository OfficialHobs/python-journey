num1 = int(input('enter first number: '))
num2 = int(input('enter second nmuber: '))
operation = input('enter a valid operator: ')

if operation == '+':
    result = num1 + num2
    print('result = {} '.format(result) )
elif operation == '-':
    result = num1 - num2
    print('result = {} '.format(result) )
elif operation == '*':
    result = num1 * num2
    print('result = {} '.format(result) )
elif operation == '/':
    result = num1 / num2
    print('result = {} '.format(result) )