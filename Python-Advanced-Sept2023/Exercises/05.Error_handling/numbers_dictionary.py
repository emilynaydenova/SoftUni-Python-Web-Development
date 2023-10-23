# Handle some errors that may occur in the code
numbers_dictionary = {}

# check for	passing non-integer type to the variable number
while (key := input()) != "Search":
    try:
        number = int(input())
    except ValueError:
        print('The variable number must be an integer')
    else:
        numbers_dictionary[key] = number


#  searching for a non-existent number
while (key := input()) != "Remove":
    try:
        print(numbers_dictionary[key])
    except KeyError:
        print('Number does not exist in dictionary')


# removing a non-existent number
while (key := input()) != "End":
    try:
        del numbers_dictionary[key]
    except KeyError:
        print('Number does not exist in dictionary')

print(numbers_dictionary)


"""
numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    number = int(input())
    numbers_dictionary[number_as_string] = number

line = input()

while line != "Remove":
    searched = line
    print(numbers_dictionary[searched])

line = input()

while line != "End":
    searched = line
    del numbers_dictionary[searched]

print(numbers_dictionary)

"""
