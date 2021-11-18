book_title =  ['great', 'expectations','the', 'adventures', 'of', 
'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

#create an empty dict
my_dict = {}
#word = 'wix'

#loop through the list to build dictionary
for word in book_title:
    if word not in my_dict:
        my_dict[word] = 1
    else:
        my_dict[word] += 1
print(my_dict)


#Example two
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for keys in cast:
    print(keys)

print("\n")

#Get keys and values
for key, value in cast.items():
    print("{} {}".format(key, value))

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key, value in basket_items.items():

    #if the key is in the list of fruits, add to fruit_count.
    if key in fruits:
        fruit_count = fruit_count + value

    #if the key is not in the list, then add to the not_fruit_count
    else:
        not_fruit_count = not_fruit_count + value

print("There are {} fruits and {} not fruits".format(fruit_count, not_fruit_count))
