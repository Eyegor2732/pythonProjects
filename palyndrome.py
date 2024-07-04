def reverse_phrase(some_string):
    strx = some_string.split()
    strx.reverse()

    str_output = ""
    for item in strx:
        str_output = str_output + " " + item

    return str_output.strip()


mystring = "I'd like to say hello to the whole world!"

print(reverse_phrase(mystring))
