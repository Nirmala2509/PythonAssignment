#Write a program to count the lines in a file “demo.txt”

with open("demo.txt", "w") as f:
    f.write("This is line one.\n")
    f.write("This is line two.\n")
    f.write("This is line three.\n")

# SRead and count the lines
line_count=0
with open("demo.txt", "r") as f:
    #print(f.read())
    for line in f:
       
        line_count=line_count+1
print(f"Total number of lines: {line_count}")    
   



