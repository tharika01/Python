age = 20
print("I am " + str(age) +" years old")
print("I am {0} years old".format(age))
print("There are {0} days in {1} , {2}, {3} ,{4},{5} ,{6}, and {7}"
      .format(31,"Jan","March","May","Jul","Aug","Oct","Dec"))
print("There are {0} days in Jan,March,May,Jul,Aug,Oct,Dec".format(31))
print("Jan :{2}, Feb :{0} ,March :{2},April :{1},May :{2},June :{1},July :{2},Aug: {2},Sept: {1},Oct: {2},Nov: {1},Dec: {2}"
      .format(28,30,31))
print()
print("""Jan :{2}
Feb :{0}
March :{2}
April :{1}
May :{2}
June :{1}
July :{2}
Aug: {2}
Sept: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28,30,31))
