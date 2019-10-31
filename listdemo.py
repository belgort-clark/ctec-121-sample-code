
cars = []
boats = ['Sail', 'Moose', 'Tug']

# append
cars.append("Chevy")

# extend
cars.extend(boats)

# insert
cars.insert(0, "Bruce")

# remove
cars.remove("Chevy")

# pop
last = cars.pop(-1)

# index
where = cars.index("Moose")

# count'
print(cars.count('Tug'))

# sort
cars.sort()
cars.sort(reverse=True)

# reverse

del cars[0]
