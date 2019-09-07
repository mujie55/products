products = []
with open('products.csv', 'r')as f:
	for line in f:
		name,price= line.strip().split(',')
		products.append([name, price])
		
print(products)
while True:
	name = input('请输入商品名称:')
	if name == 'q':
		break
	price = input('请输入商品价格:')
	products.append([name, price])
print(products)

for product in products:
	print(product[0], '的价格是:', product[1])

with open('products.csv', 'w')as f:
	f.write('商品,名称\n')
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')