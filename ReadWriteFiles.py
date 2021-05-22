f = open(r"C:\Users\Alicia\Documents\myfile.txt", 'w')  # opening a file
f.write("Hello R") # writing to file
5
f.close()

# reading file
f = open(r'C:\Users\Alicia\Documents\myfile.txt')
for line in f:
    print(line)
f.close()
