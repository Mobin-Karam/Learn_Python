print('$$$$>>> Welcome to Calculator Sir <<<$$$')


def plus(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def equal(num1, num2):
    return num1 == num2


while True:
    expression = input("*** Enter your expression ***:\n >>> ")

    numbers_operators = []

    result = 0

    # data  1-2+3*3/3*2
    # data [(('1', '+', '2'), '-', (('2', '*', '3'), '/', '3'))]

    # for index, operator in enumerate(input_numbers.split(' ')):
    #     if operator.isdigit():
    #         number1 += [int(operator)]
    #     elif operator == '*':
    #
    # input_numbers.split()
    # for index, operator in enumerate(input_numbers):
    #     if operator == "*":
    #         operators.append({"operator": operator, 'index': index})
    #     elif operator == "/":
    #         operators.append({'operator': operator, 'index': index})
    #     elif operator == "+":
    #         operators.append({'operator': operator, 'index': index})
    #     elif operator == "-":
    #         operators.append({'operator': operator, 'index': index})
    # for index, operator in enumerate(operators):
    #     if operator['operator'] == '*':
    #         operators[index]['operator'] = '*'

    # elif operator.isdigit():
    #     if operator_plus:
    #         result = plus(result, int(operator))
    #     elif operator_subtract:
    #         result = subtract(result, int(operator))
    #     elif operator_multiply:
    #         result = multiply(result, int(operator))
    #     elif operator_divide:
    #         result = divide(result, int(operator))
    #     else:
    #         result = int(operator)
    #
    # else:
    #     print("Invalid operator")
    #     break
