'''
*000*000*
0*00*00*0
00*0*0*00
000***000
'''
l=int(input())
b=int(input())
for i in range(1,b+1):
    for j in range(1,l+1):
        if j==(l+1)//2 or j==i or j==(l+1)-i:
            print('*',end='')
        else:
            print('0',end='')
    print()

