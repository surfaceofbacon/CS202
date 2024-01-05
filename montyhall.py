import random
results = []
while len(results) < 1000:
    random_int_index = 2
    doors = {}
    possible_objects = ['Goat', 'Goat', 'Car']
    for i in range(1, 4):
        index = random.randint(0, random_int_index)
        doors[i] = possible_objects[index]
        possible_objects.pop(index)
        random_int_index -= 1
    if doors[1] == 'Car':
        results.append('Goat')
    else:
        results.append('Car')
Goats = results.count('Goat')
Cars = results.count('Car')
print(f'won the car {Cars / 1000 * 100}% of the time')
print(f'won the goat {Goats / 1000 * 100}% of the time')