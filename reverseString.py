def reverse_string_function(some_string):
    string_reverse = ""
    i = 0

    while i < len(some_string) - 1:
        string_reverse = some_string[i] + string_reverse
        i += 1

    return string_reverse


input_string = input('Please enter your string: ')

print(reverse_string_function(input_string))