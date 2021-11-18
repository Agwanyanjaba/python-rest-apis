from keyword import iskeyword

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

#format with string
maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))


print('hello'.isidentifier(), iskeyword('hello'))
space_string = " "
print(space_string.isspace())


lower_case = "test Lower case"
print(lower_case.islower())