# Organizing a List

# What is a List?
""""
A List is a collection of items in a particular order

INDEX positions start at 0, not 1
"""

bicycles = ['trek', 'cannondale', 'redline', 'sprecialized']
print(bicycles)
# print(bicycles[0])
# print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
print('\n')

message = f"My first bicycle was a {bicycles[0].title()}.\n"
print(message)

# 3-1 Names.
names = ['israel', 'aaliyah', 'esmeralda', 'nick']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
print('\n')

# 3-2 Greetings.
print(f"Hi {names[0].title()}, hope you have a good day today!")
print(f"Hi {names[1].title()}, hope you have an amazing day today!")
print(f"Hi {names[2].title()}, hope you have a blessed day today!")
print(f"Hi {names[-1].title()}, hope you have a good bro!")

# 3-3 Your Own List
vehicles = ['honda', 'ferrari', 'mustang', 'camero']
print(f"I currently own a {vehicles[0]} Accord, one of the best car's I've owned.")
print(f"I would like to own a {vehicles[2]} or a {vehicles[-1]} one day.")
print(f"However, my dream car is to have a {vehicles[1]}\n")

# Modifying Elements in a List
topic = "MODIFYING ELEMENTS IN A LIST"
print(topic.title())
bikes = ['trek', 'cannondale', 'redline', 'specialized']
print(bikes)
bikes[0] = 'ducati'
print(bikes)
print("\n")

# Adding Elements to a List
topic = "adding elements to a list"
print(topic.title())
# APPENDING an item to the list, adds it to the end of the list
bikes = ['trek', 'cannondale', 'redline', 'specialized']
print(bikes)
bikes.append('ducati')
print(bikes)
print("\n")
empty = []
empty.append('honda')
empty.append('trek')
empty.append('cannondale')
empty.append('redline')
empty.append('suzuki')
print(empty)
print("\n")

# Inserting Elements to a list
topic = "inserting elements to a list"
print(topic.title())
bikes = ['honda', 'yamaha', 'suzuki']
bikes.insert(0, 'ducati')
bikes.append('trek')
print(bikes)
print("\n")

# Removing Elements from a List
topic = "removing elements from a list"
print(topic.title())
bikes = ['trek', 'cannondale', 'redline', 'specialized']
print(f"This is the original list: {bikes}")
del bikes[0]
print(f"This is the list once an element has been removed: {bikes}")
dreams = f"I've always dreamed of owning a {bikes[1]} motorcycle!"
print(dreams)
print("\n")

# Removing using the pop() method
bikes = ['trek', 'cannondale', 'redline', 'specialized']
print(f"Original list: {bikes}")
popped_bike = bikes.pop()
print(f"modified: {bikes}")
print(f"popped: {popped_bike}")
last_owned = bikes.pop(2)
print(bikes)
print(f"The last bike that I owned was a {last_owned.title()}.\n")

# Removing an Item by Value
topic = "removing an item by value"
print(topic.title())
bikes = ['honda', 'yamaha', 'suzuki', 'ducati']
print(bikes)
bikes.remove('ducati')
print(bikes)
print('\n')
bikes = ['honda', 'yamaha', 'suzuki', 'ducati']
print(bikes)
too_expensive = 'ducati'
bikes.remove(too_expensive)
print(bikes)
print(f"A {too_expensive.title()} is too expensive for me.\n")

# 3-4 Guest List
topic = "3-4. guest list. inviting guest to dinner"
print(topic.title())
dinner_list = ['denzel washington', 'king david', 'dodgers']
inv1 = f"Hi {dinner_list[0]}, I'd like to invite you to dinner tonight."
inv2 = f"{dinner_list[1]}, it would be an honor to have you over for dinner tonight."
inv3 = f"{dinner_list[-1]}, you better make it to dinner tonight!"
print(inv1)
print(inv2)
print(inv3)
flake = f"Unfortunately, the {dinner_list[-1]} won't be joining us tonight."
print(flake)
dinner_list.remove('dodgers')
print(dinner_list)
print("\n")

# 3-5 Changing Guest List
topic = "3-5. changing guest list."
print(topic.title())
dinner_list.append('joe')
add = f"Hey {dinner_list[-1].title()}, care to join us for dinner tonight? {dinner_list[0].title()} and {dinner_list[1].title()} will also be joining us."
print(add)
print(dinner_list)
message = f"Hey {dinner_list[0].title()}, {dinner_list[1].title()}, {dinner_list[-1].title()} I reserved a bigger table, will see who else can make it tonight.\n"
print(message)

# 3-6 More Guest.
topic = "3-6. more guests."
guest_list = f"Guest List: {dinner_list}"
print(topic.title())
print(guest_list)
dinner_list.insert(0, 'aaliyah')
dinner_list.insert(2, 'jennifer')
dinner_list.append('lino')
print(f"Updated Guest Lists: {dinner_list}")
print(f"Hi {dinner_list[0].title()}, make sure to make it to dinner on time! I have a surprise!")
print(f"My lovely sister {dinner_list[2].title()}, I'm having a formal dinner, hope you can make it.")
print(f"Hi {dinner_list[-1].title()}, come over tonight. We're having a few guest over for dinner.\n")

print("Unfortunately the dinner table didn't make it on time and I can only have two guest over tonight.\n")

# 3-7 Shrinking Guest List
topic = "3-7. shinkring guest list"
print(topic.title())
print(f"Guest List: {dinner_list}.")
dinner_list.pop(1)
dinner_list.pop(2)
dinner_list.pop(2)
dinner_list.pop(2)
print(f"Updated Lists: {dinner_list}")
print(f"Hey {dinner_list[0].title()} and {dinner_list[-1].title()}, excited to see you both at dinner tonight.")
del dinner_list[-1]
del dinner_list[0]
print(dinner_list)


"""
cars = ['bmw', 'audi', 'toyota', 'crysler']
print(cars)

cars.reverse()
print(cars)
print(len(cars))
"""
"""
# 3-8 Seeing the World

locations = ['chicago', 'middle east', 'canada', 'mexico']
print(locations)

print(sorted(locations))
print(locations)

locations.reverse()
print(locations)
print('\n')
# 3-9 Dinner Guest

# 3-10 Every Function

countries = ['el salvador', 'africa', 'israel', 'europe']
languages = ['espanol', 'english', 'french', 'korean']
cities = ['la dalles', 'los angeles', 'dallas', 'portland']
print(countries)
print(languages)
print(cities)

print(sorted(countries))
print(sorted(languages))
print(sorted(cities))

print('\n')

# Avoiding Index Errors when Working with Lists

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle[-1])

"""
