parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

print("\n")
print(parrot[-1])
print(parrot[-14])

print("\n")
#using negative indexing
print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

#slicing
print(parrot[0:9])#slice from 0 to 8 i.e not including 9
print(parrot[:9])
print(parrot[3:5])
print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:])

print(parrot[-4:-2])
print(parrot[-14:-8])

print("\n")

#using step in slice
print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223:372:036,854:775,807"
seperators = number[1::4]
print(seperators)
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25::-1]
print(backwards)

slice1 = letters[-10:-13:-1]
print(slice1)
slice2 = letters[4::-1]
print(slice2)
slice3 = letters[:-9:-1]
print(slice3)
