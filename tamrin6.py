
myList = []
num= int(input("how many numbers do you want to sum?"))
while True:
    n = (input("insert a number(put = to exit):"))
    if n == "=":
        break
    myList.append(int(n))
print(myList)
summ=0
for i in myList:
    summ+=i
    print (summ)
#or: Summ = sum (myList)
# print(Summ)
counter = 0
while counter<num:
    print ("faride")
    counter+=1




