name=input("enter string=")
l1=list(name)
l1.reverse()
l2=list(name)
if l1==l2:
    print("the string is palindrome")
else:
    print("not palidrome")
