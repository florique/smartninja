name = "wert"
name2 = int(input("Tippe eine Zahl ein: \n"))
name3 = 2.0
#comment

if name2 > 3 and name2 < 8:
    print ("yeah")
else:
    print ("nope")

# + - / *
# % modulo - Rest einer Divison

count = 10
while(count):
    print(count)
    count -= 1

    if count < 5:
        #break
        continue

    print ("continue text")

#print (range(0, 4, 2))
for item in range(0, 4, 2):
    print (item)