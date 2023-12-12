tuple=(2,4,5,10,23,25,25,12,23,21)

def find_more_than_avg(tuple):
    sum=0
    count=0
    for i in tuple:
        sum+=i
    avg=sum/len(tuple)
    
    for i in range(len(tuple)):
        if(tuple[i]>avg):
            count+=1
    
    return (count/len(tuple))*100

def generate_frequency(tuple):
    list=[]
    for i in range(0,26):
        c=tuple.count(i)
        list.append(c)
    print(list)
    
def sort_freq(tuple):
    list1=list(tuple)
    list1.sort()
    print(list1)
    
sort_freq(tuple)
generate_frequency(tuple)
print(find_more_than_avg(tuple))