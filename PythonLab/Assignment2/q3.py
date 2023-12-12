num_passengers=int(input("Enter number of passengers:"))
source=str(input("Enter Source:"))
src=source[0]+source[1]+source[2]
destination=str(input("Enter Destination:"))
dst=destination[0]+destination[1]+destination[2]
air_line="AI"
full_list=[]
ans=[]
for i in range(num_passengers):
    curr=""
    curr=curr+air_line+":"+src+":"+dst+":"+str(101+i)
    full_list.append(curr)
if num_passengers<5:
    print(full_list)
else:
    for i in range(num_passengers-5,num_passengers):
        ans.append(full_list[i])
    print(ans)