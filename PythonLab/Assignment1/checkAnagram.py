def check_anagram(str1,str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if(len(str1)!=len(str2)):
        return False
    for x in str1:
        if x not in str2:
            return False
    for i in range(0,len(str1)):
        if(str1[i]==str2[i]):
            return False
    return True



print(check_anagram("eat", "tea"))  
print(check_anagram("backward", "drawback"))  
print(check_anagram("Reductions", "discounter"))  
print(check_anagram("About","table"))