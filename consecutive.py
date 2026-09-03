filename=input("Enter the file name:")
with open(filename,"r")as f:
	lines=f.readlines()
	for line in lines:
		if "1 1"in line:
			print(line.strip())
