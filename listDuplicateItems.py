def find_duplicates(some_list):
    some_list.sort()
    some_set = set()
    found_duplicate = False

    i = 0
    while i < len(some_list)-1:
        if some_list[i] == some_list[i+1]:
            if not found_duplicate:
                print('Duplicates:')
                found_duplicate = True

            # print(some_list[i])
            some_set.add(some_list[i])
        i += 1

    if not found_duplicate:
        print('No duplicates found.')

    if len(some_set) != 0:
        print(some_set)

        def find_duplicates(some_list):
            some_list.sort()
            some_set = set()
            found_duplicate = False

            i = 0
            while i < len(some_list) - 1:
                if some_list[i] == some_list[i + 1]:
                    if not found_duplicate:
                        print('Duplicates:')
                        found_duplicate = True

                    # print(some_list[i])
                    some_set.add(some_list[i])
                i += 1

            if not found_duplicate:
                print('No duplicates found.')

            if len(some_set) != 0:
                print(some_set)


def find_duplicates_simple(some_list):
    some_list.sort()
    some_set = set()

    i = 0
    while i < len(some_list)-1:
        if some_list[i] == some_list[i+1]:
            some_set.add(some_list[i])
        i += 1

    return some_set


s_list = [1, 3, 2, 3, 3, 4, 5, 1]

find_duplicates(s_list)

print('============================')

simple_list = find_duplicates_simple(s_list)

if len(simple_list) == 0:
    print('No duplicates found.')
else:
    print('Duplicates:')
    print(simple_list)