x=int(input("Enter the lower limit: "))
y=int(input("Enter the upper limit: "))
ans=-1
for i in range(x,y+1):
    if i%3==0 and i%5==0 and i>9 and i<100:
        ans=i
        
print("The maximum number with the condition satisfied is: ",ans)   