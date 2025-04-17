# 0,1, 1, 2, 3, 5, 8, 13 ,21,34,45,89
j=[0,1,1]
i=3
while 3<=i<100:
    j.append(j[i-1]+j[i-2])
    i+=1
number=int(input("enter number of fibonnaci sequence :"))
print(j[number-1]) 
