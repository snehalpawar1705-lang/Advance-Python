f1 = open("python.txt","r")
lines = f1.readlines()
f1.close()
print("Total no. of lines in python.txt: ",len(lines))
print("Contents of line:",lines)

two_lines = lines[:2]
print("First two lines:")
for i in two_lines:
    print(i)

f2 = open("Output.txt","w")
f2.writelines(two_lines)
print("\n First two lines from python.txt are written in file Output.txt")