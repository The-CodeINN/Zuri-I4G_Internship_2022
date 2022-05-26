from audioop import reverse


name = "richard "

# print(f"My name is {name.title().rstrip()}")


# for places in sorted(places_in_the_world[:-3]):
#     print(places)


number = list(range(1, 4))
# print(number)

squares = []

for i in range(1, 11):
    square = i**2
    squares.append(square)

cubes = [value ** 3 for value in range(1, 11)]
# print(cubes)

nums = (1,2,3,4)

places_in_the_world = ['nigeria', 'ghana',
                       'cameroun', 'djibouti', 'madagascar']

for places in places_in_the_world:
    if places == "nigeria":
        print(places.title())
    else:
      print(places.upper())