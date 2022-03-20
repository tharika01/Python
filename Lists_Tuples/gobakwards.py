data = [ 104,101,4,105,308,103,5,107,100,306,106,102,108]
min = 100
max = 200
for index in range(len(data)-1, -1,-1):
    if data[index] < min or data[index] > max:
        print(index ,data)
        del data[index]
print(data)

for index, value in enumerate(reversed(data)):
    print(index, value)
