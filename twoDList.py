import os # Operating System

# Read CSV
def read_file(filename):
	products=[]
	with open (filename,'r',encoding='utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue # Salta
			name,price=line.strip().split(',')
			products.append([name,price])
	print(products)
	return products


# Input
def user_input(products):
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
	return products

#Output
def print_products(products):
	for p in products:
		print(p[0],"'s price is",p[1])

#WiteFile
def write_file(filename,products):
	with open (filename,'w',encoding='utf-8') as f:
		f.write('商品,价格\n')
		for p in products:
			f.write(p[0]+','+p[1]+'\n')

#Check
if os.path.isfile('products.csv'): 
	print('Come On, Baby! I find it！')
	products=read_file('products.csv')
else:
	print("Non Capisco!")

products=user_input(products)
print_products(products)
write_file('products.csv',products)
