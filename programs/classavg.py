'''
WAP to find the class average of a subject 
in a class
'''

n=int(input("Enter Class Strength: "))
sum=0
#how I like
for i in range(0,n):
    marks=float(input("Enter marks: "))
    sum+=marks
avg=sum/n

print("Class Average:",format(avg,'.2f'))

#like sir did
sum=0
avg=0
i=0
while i!=n:
    marks=float(input("Enter marks: "))
    sum+=marks
    i+=1
avg=sum/n
print("Class Average:",format(avg,'.2f'))