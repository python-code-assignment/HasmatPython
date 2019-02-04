value=input("Enter numbers: ")
print value
list=[]
for num in value:
    if num%2==1:
        list.append(num*num)
print(list)
