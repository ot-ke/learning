Q = int(input("Введите целое число да подлиннее: "))

#1234for 1234

s=0
while Q>0:
    a=Q%10
    s=s+a
    Q=Q//10
print(s)

#a=Q//1000
#a2=Q%1000
#print(a, a2)
#a3=a2%100
#a2=a2//100
#print(a2, a3)
#a4=a3%10
#a3=a3//10
#print(a3, a4)
#print(a4)

#print(a+a2+a3+a4)