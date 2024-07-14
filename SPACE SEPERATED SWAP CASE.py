a=input("enter string= ")
a.replace(" ","")
l=[]
for i in range(0,len(a)):
    if a[i].isupper():
        l.append(a[i].lower())
    if a[i].islower():s
        l.append(a[i].upper())
b=""
for i in l:
    b=b+i
print(b)