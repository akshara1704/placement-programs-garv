def swap_case(s):

    s=list(s)
    z=[]
    a=""
    for i in range(0,len(s)):
        if s[i].isupper():
            z.append(s[i].lower())
        elif s[i].lower():
            z.append(s[i].upper())
    for i in z:
        a=a+i
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)