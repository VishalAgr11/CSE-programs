n= int(input("Enter size of list"))
l=[]
totalL=0
totalR=0

print ("enter numbers")
for i in range(0, n):
    e=( int(input()))
    l.append(e)
ele=1 
check=1
while (ele<n-1) :
    
       totalL = sum(l[0:ele])   
       totalR = sum(l[ele+1:])

       if (totalR==totalL):
          print ("Found the element -  ",l[ele])
          check=0

       ele= ele+1        
if (check==1):
    print("Not found")
