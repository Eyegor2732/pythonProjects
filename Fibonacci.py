def fibonacci_method(sequence_length):
    numbers_list = []

    i = 0
    while i < min(2, sequence_length):
        next_number = i
        numbers_list.append(next_number)
        i += 1

    while i < sequence_length:
        next_number = numbers_list[i-2] + numbers_list[i-1]
        numbers_list.append(next_number)
        i += 1

    return numbers_list


seq_length = 10
fibonacciSequence = fibonacci_method(seq_length)

print('First', seq_length, 'Fibonacci numbers list:', fibonacciSequence)

print('First', seq_length, 'Fibonacci numbers one by one:')
for item in fibonacciSequence:
    print(item)
