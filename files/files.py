#jabber = open("/Users/tharika/Desktop/Python/Python-pgms/files/sample.txt","r")

#for line in jabber:
#    print(line)
#jabber.close()

with open("sample.txt","r") as jabber:
    for line in jabber:
        if "JAB" in line:
            print(line,end = " ")
