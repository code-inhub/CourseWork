input_file="file.txt"
count =0
with open(input_file,"r") as inf:
    file_contents = inf.read()
    count = len(file_contents)/2
    file_content = file_contents[:int(count)]    
    half_next = file_contents[int(count):]
    half_next = half_next.rstrip("\n")

with open(input_file,"w") as outf:
    outf.write(half_next)
    outf.write(file_content)    