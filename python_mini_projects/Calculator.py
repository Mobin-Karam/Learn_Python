print('$$$$>>> Welcome to Calculator Sir <<<$$$')

while True:
    expression = input("*** Enter your expression ***:\n >>> ").strip()
    numbers = ''
    numbers_operators = []

    # Separate Char to Numbers And Operators
    for index, char in enumerate(expression):
        if char.isdigit():
            numbers += char
        else:
            numbers_operators.append(numbers)
            numbers = ''
            numbers_operators.append(char)
    if numbers:
        numbers_operators.append(numbers)
        numbers = ''


    # Operator insert
    def operation(num1, num2, operator):
        if operator == '*':
            return f'{num1 * num2}'
        elif operator == '/':
            return f'{num1 / num2}'
        elif operator == '+':
            return f'{num1 + num2}'
        elif operator == '-':
            return f'{num1 - num2}'
        return None


    # Calculator Logic
    def calculator(stop_num, nums_operators, operator):
        while stop_num <= len(nums_operators) - 1:
            item = nums_operators[stop_num]
            if item == operator:
                operation_output = operation(int(nums_operators[stop_num - 1]), int(nums_operators[stop_num + 1]),
                                             operator)
                nums_operators.remove(nums_operators[stop_num + 1])
                nums_operators.remove(item)
                # print(f'{item} -> {operation_output}')
                nums_operators[stop_num - 1] = operation_output
                stop_num = 0
            else:
                # Add one to loop again in line to reach length of the list ...
                stop_num += 1


    stop_number = 0
    calculator(stop_number, numbers_operators, '*')
    calculator(stop_number, numbers_operators, '/')
    calculator(stop_number, numbers_operators, '+')
    calculator(stop_number, numbers_operators, '-')

    # Result =>
    print(f'>>> {expression} = {numbers_operators[0]}')

    # Continue Calculator
    continue_calculator = False
    while True:
        off_calculator = input('*** Enter y/n if want continue calculator?! ***:\n >>> ').strip().lower()
        if off_calculator.isalpha():
            if off_calculator == 'y':
                numbers = ''
                numbers_operators = []
                break
            elif off_calculator == 'n':
                continue_calculator = True
                break
        elif off_calculator.strip() == '':
            print('*** You need to enter a valid y/n. it\'s empty. ***')
            continue
        elif off_calculator.strip().isdigit():
            print('*** You need to enter a valid y/n. it\'s numbers. ***')
            continue
        else:
            print('*** You need to enter a valid y/n. ***')
            continue
    if continue_calculator:
        break

# data input  >  1+2*22+44/2-3+54*7
# data output >
