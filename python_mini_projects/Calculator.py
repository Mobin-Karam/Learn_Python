print('$$$$>>> Welcome to Calculator Sir <<<$$$')

while True:
    expression = input(
        "*** Enter your expression Or y for (Yes) and n for (No) to continue. \n  *** >>> ").strip()
    numbers = ''
    numbers_operators = []
    # Continue Calculator

    continue_calculator = False
    # while True:
    #     if expression.isalpha():
    #         if expression == 'y':
    #             numbers = ''
    #             numbers_operators = []
    #             break
    #         elif expression == 'n':
    #             continue_calculator = True
    #             break
    #         else:
    #             print('*** You need to enter a valid y/n. ***')
    #             break
    #     elif expression.strip() == '':
    #         print('*** You need to enter a valid y/n. it\'s Another alphabet. ***')
    #         break
    #     elif expression.strip().isdigit():
    #         print('*** You need to enter a valid y/n. it\'s numbers. ***')
    #         break
    #     else:
    #         print('*** You need to enter a valid y/n. ***')
    #         break
    # if continue_calculator:
    #     break

    # Separate Char to Numbers And Operators
    for index, char in enumerate(expression):
        if char == '-':
            numbers += '-'
        elif char.isdigit() or char == '.':
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
            multiply = 0
            if type(float(num1)) == float and type(float(num2)) == float:
                multiply = float(num1) * float(num2)
            elif type(float(num1)) == float:
                multiply = float(num1) * int(num2)
            elif type(float(num2)) == float:
                multiply = float(num2) * int(num1)
            elif type(float(num1)) != float and type(float(num2)) != float:
                multiply = int(num1) * int(num2)

            return f'{multiply}'
        elif operator == '/':
            division = float(num1) / float(num2)
            if division - int(division) == 0:
                return f'{int(division)}'
            else:
                return division
        elif operator == '+':
            plus = 0
            if type(float(num1)) == float and type(float(num2)) == float:
                plus = float(num1) + float(num2)
            elif type(float(num1)) == float:
                plus = float(num1) + int(num2)
            elif type(float(num2)) == float:
                plus = float(num2) + int(num1)
            elif type(float(num1)) != float and type(float(num2)) != float:
                plus = int(num1) + int(num2)
            return f'{plus}'
        elif operator == '-':
            minus = 0
            if type(float(num1)) == float and type(float(num2)) == float:
                minus = float(num1) - float(num2)
            elif type(float(num1)) == float:
                minus = float(num1) - int(num2)
            elif type(float(num2)) == float:
                minus = float(num2) - int(num1)
            elif type(float(num1)) != float and type(float(num2)) != float:
                minus = int(num1) - int(num2)
            return f'{minus}'
        return None


    # Calculator Logic
    def calculator(stop_num, nums_operators, operator):
        while stop_num <= len(nums_operators) - 1:
            item = nums_operators[stop_num]
            if item == operator:
                operation_output = operation(nums_operators[stop_num - 1], nums_operators[stop_num + 1],
                                             operator)
                nums_operators.remove(nums_operators[stop_num + 1])
                nums_operators.remove(item)
                # print(f'{item} -> {operation_output}')
                nums_operators[stop_num - 1] = operation_output
                stop_num = 0
                # print(numbers_operators)
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

# data input  >  1+2*22+44/2-3+54*7
# data output >
