data=[]
with open('list.txt','r') as f:
	for line in f:
		data.append(line.strip())
# data=[line.strip() for line in f]
print(data)

