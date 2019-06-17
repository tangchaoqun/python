data=[]
with open('list.txt','r') as f:
	for line in f:
		data.append(line.strip())
print(data)

