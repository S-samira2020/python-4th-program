#squares = [value**2 for value in range(1,11)]
#print(squares)
# 4.3
for numbers in range(1,21):
    print(numbers)
print()
# 4.4
numbers = list(range(1,10000000))
print(numbers)
print()
# 4.5
numbers = list(range(1,10000000))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print()
# 4.6
for numbers in range(1,21,2):
    print(numbers)
print()
# 4.7
for numbers in range(3,31,3):
    print(numbers)
print()
# 4.8
cubes = []
for numbers in range(1,11):
    cube = numbers ** 3
    cubes.append(cube)
for cube in cubes:
    print(cube)
print()
# 4.9
cubes = [numbers ** 3 for numbers in range(1,11)]
print(cubes)