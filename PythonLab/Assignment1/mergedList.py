list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
list3=[]
i=0
l=len(list1)-1

while i<=l :
    if list1[i] and list2[l-i]:
       ele=list1[i]+list2[l-i]
    elif list1[i]:
       ele=list1[i]
    elif list2[l-i]:
       ele=list2[l-i]   

    list3.append(ele)
    i+=1
    
for ele in list3:
    print(ele,end=" ")   
   