'''
Tried making a new searching algorithm
Forget this :P
It just turned out to be linear search with with extra steps
'''

l=[1,4,5,2,99,76,24,32]
s=100
i=0;j=1
while i<len(l) and j<len(l):
    if l[i]==s:
        print("Found at index",i)
        break
    elif l[j]==s:
        print("FOund at index",j)
        break
    else:
        i+=2
        j+=2
else:
    print("Not found")