# cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
# for city in cities:
#     print(city)
# print("Done!")

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)-1):
    cities[index] = cities[index].title()

print(cities)

multiples = [n for n in range(1, 31) if n % 5 == 0] 
 
print(multiples) 

for i in range(5, 31, 5):
    print(i)
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
     usernames.append(name.lower().replace(' ', '_'))
print(usernames)


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in range(len(names)):
    usernames.append(names[name].lower().replace(' ', '_'))

print(usernames)