# Read CSV
products=[]
with open ('products.csv','r',encoding='utf-8') as f:
	for line in f:
		if '商品,价格' in line:
			continue # Salta
		name,price=line.strip().split(',')
		products.append([name,price])
print(products)

# Input
while True:
	name=input("Please insert product's name:")
	if name=="q":
		break
	price=input("Please insert price:")
	# p=[]
	# p.append(name)
	# p.append(price)
	# p=[name,price]
	products.append([name,price])
print(products)

#Output
for p in products:
	print(p[0],"'s price is",p[1])

with open ('products.csv','w',encoding='utf-8') as f:
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0]+','+p[1]+'\n')

