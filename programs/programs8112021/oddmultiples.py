'''
WAP to print some odd multiples of a odd number
'''
n=int(input("Enter an odd number"))
for i in range(n+1,(n+101)):
    if i%2!=0 and i%n==0:
        print(i)
