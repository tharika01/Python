friends = ['tharika','Tanusri','Megha','Ananya','Skanda','Srushti']
print(friends)
length = len(friends)
print(length)
friends.reverse()
print(friends)
message = f"Hey,{friends[-1].title()}."
print(message)
message = f"Hey,{friends[-2].title()}."
print(message)
friends.append('Sudheep')
print(friends)
print("hey !!,{0}".format(friends[0]))

#inserting an element at a particular position
friends.insert(0,'prateek')
print(friends)

#deleting an item from the list
del friends[0]
print(friends)

#Using pop method
pop_ele = friends.pop()
print(pop_ele)
print(friends)
pop = friends.pop(2)
print("I love {0}".format(pop))
print(f"i love {pop.title()}.")

#Removing an item by value
friends.remove('Skanda')
print(friends)

#sorting the list
friends.sort()
print(friends)
friends.sort(reverse = True)
print(friends)
#friends.sorted(reverse = True)
print(sorted(friends))
#for i in range [5]:
 #   print("Hey !!{i}".format(friends[i]))
