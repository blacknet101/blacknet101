# Sorting a List Permanently with the sort() method
topic = "* Sorting a List Permanently with the sort() method"
print(topic)
cars = ['bmw', 'audi', 'toyota', 'honda']
print(f"Original List: {cars}\n")
    # sort() method will sort the list in alphabetical order
cars.sort()
print(cars)
    # adding 'reverse=True/False' will sort the list in reverse-alphabetical order
cars.sort(reverse=True)
print(cars)

# Sorting a list Temporarily with the sorted() Function
topic = "\n* Sorting a list Temporarily with the sorted() Function"
print(topic)
cars = ['bmw', 'audi', 'honda', 'toyota']
print(f"Here is the original list: {cars}")
print(f"\nHere is the sorted list: ")
print(sorted(cars))

# Printing a List in Reverse Order
topic = "\n* Printing a List in Reverse Order"
print(topic)
cars = ['bmw', 'honda', 'audi', 'tesla']
print(f"Original lists: {cars}")
cars.reverse()
print(f"Reversed Order: {cars}")

# Finding the Length of a List
topic = "\n* Finding the Length of a List"
print(topic)
cars = ['bmw', 'audi', 'honda', 'toyota']
print(len(cars))

# 3-8. Seeing the World.
topic = "\n3-8. Seeing the World."
print(topic)

places = ['japan', 'mexico', 'italy', 'france', 'germany']
print(f"Original List: {places}")
print(f"Sorted List: {sorted(places)}")
print(f"Original List: {places}")
print(f"Reversed Sorted List: {sorted(places, reverse=True)}")
print(f"Original List: {places}")
places.reverse()
print(f"Reversed List: {places}")
places.sort()
print(f"Sorted List: {places}")

# 3-9. Dinner Guests.
topic = "\n3-9. Dinner Guests."
print(topic)
guest = ['aaliyah', 'denzel washington', 'jennifer', 'king david', 'joe', 'lino']
print(len(guest))

# 3-10. Every Function.
topic = "\n3-10. Every Function."
print(topic)
del guest[1]
guest.append('jonathan')
guest.insert(3, 'jack')
print(guest)
