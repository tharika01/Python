with open("sample.txt","a") as append_file:
    for i in range(2,13):
        for j in range(1,13):
            print(f"{j:>2} times {i} is {i * j}",file=append_file)
        print("*"*20,file=append_file)
