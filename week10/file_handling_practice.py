# Step 1: Create and write to the file
with open('mydata.txt', 'w') as f:
	f.write("I like reading books.\n")
	f.write("I enjoy coding.\n")
	f.write("I play basketball.\n")

# Step 2: Read from the file and print its contents
with open('mydata.txt', 'r') as f:
	print(f.read())

# Step 3: Append a new line to the file
with open('mydata.txt', 'a') as f:
	f.write("I am learning file handling in Python!\n")

# Step 4: Read from the file again and print its contents
with open('mydata.txt', 'r') as f:
	print(f.read())

