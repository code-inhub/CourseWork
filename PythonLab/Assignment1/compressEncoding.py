s = input("Enter the string: ")
char = s[0]
count = 1

for i in range(1, len(s)):
    if s[i] == char:
        count += 1
    else:
        print(count, char, sep="", end="")
        char = s[i]
        count = 1

print(count, char, sep="") 