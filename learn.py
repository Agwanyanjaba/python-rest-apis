import requests
thislist = [
    "mango", "Pine", "Apple", "Guava", "orange", "kiwi", "melon", "mango"
]
print(thislist)

print(thislist.index("Pine"))

print(thislist[1:4])

#loop through a list
for x in thislist:
  print(x)


#Check if an Item is in the list
if "kiwi" in thislist:
  print("Yes \"KIWI\" is in the list")


#Length of List
print(len(thislist))


thislist.append("Avocado")

print(thislist)

#Insert an item as the third position:

thislist.insert(2,"Bananas")
print(thislist)


#Build tuple from list
for y in thislist:
  tupleList = list(y)

print(tupleList)


#Return the number of times the value 5 appears in the tuple:
thisTuple = (1,3,2,5,2,9,7,8,3,4,5,2)

#loop through the tuple
for x in thisTuple:
  print(x)
  
print("The length of the tuple is:",len(thisTuple))

#Return the frequesncy of an item in tuple

print("2 Appears in the tuple",thisTuple.count(2),"times")

#return a specific index of an item in a tuple

citiesTuple = ("Kigali","Nairobi","Kampala","Lagos","Kinsasha")

print("The Nairobi City index is:",citiesTuple.index("Nairobi"))

#In Python sets are written with curly brackets.
movieSet = {"Gotham","F9","Lucifer","Die Hard","Ozak"}

print("The movies are:", movieSet)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# dictionaries are written with curly brackets,
# and they have keys and values.

thisDict = {"Name":"Wycliffe", "Height":5.95, "Hobby":"Driving"},{"Name":"Jane", "Height":6.95, "Hobby":"Teaching" }, {"Name":"Mary",
  "Height":5.95, "Hobby":"Travelling"}

print(thisDict)

#if ..else
a = 3
b = 5
if a > b:
  print("A")
else:
  print("B")

#if else short hand

#print("A") if a>b else print("B")


#functions
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
#print output of the number of people in space
print(data['number'])

print(data)
