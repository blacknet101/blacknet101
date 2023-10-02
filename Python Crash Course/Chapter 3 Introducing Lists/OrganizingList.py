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
print("\n")

# Sorting a list Temporarily with the sorted() Function
topic = "* Sorting a list Temporarily with the sorted() Function"
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
