def count_vowels():
    file=open('file.txt')
    content=file.read()
    vowels=list("AEIOUaeiou")
    count_vowels=0
    count_consonants=0
    for alpha in content:
        if alpha in vowels:
            count_vowels+=1
        else:
            count_consonants+=1
    
    print("Number of vowles are: ",count_vowels)
    print("Number of consonants are: ", count_consonants)

count_vowels()