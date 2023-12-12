input_file="input.txt"
output_file="output.txt"

with open(input_file,"r") as inf,open(output_file,"w") as ouf:
    
    for line in inf:
        if line.strip() and line.lstrip()[0].islower():
            ouf.write(line)
            
print(f"lines copied to {output_file}")