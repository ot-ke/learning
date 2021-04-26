list=[]
list1=[]
a=0
print(list, list1)

while a!="quit":
    a=input("Введите значение: ")
    list1=[a]
    list=list+list1

    list_true=list[:len(list)-1]
print(list_true)