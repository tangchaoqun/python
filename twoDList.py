products=[]
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
