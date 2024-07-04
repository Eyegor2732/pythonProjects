def factorial_method(number):
    factorial = number

    if number > 1:
        i = number
        while i > 1:
            factorial = factorial * (i-1)
            i -= 1
    elif number < 0:
        factorial = 'Impossible to calculate factorial for: ' + str(number) + '. The number should be greater or equal 0.'
    else:
        factorial = 1

    return factorial


f_number = 5
print(factorial_method(f_number))