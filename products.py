import os # operating system 作业系统
#读取档案
products = []
if os.path.isfile('products.csv'): #检查档案在不在
	print('有这个档案！')
	with open('products.csv', 'r')as f:
		for line in f:
			if '商品,名称' in line:
				continue #继续
			name,price= line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到档案！')

#让使用者输入
while True:
	name = input('请输入商品名称:')
	if name == 'q':
		break
	price = input('请输入商品价格:')
	products.append([name, price])
print(products)

#印出所有购买记录
for product in products:
	print(product[0], '的价格是:', product[1])

#写入档案
with open('products.csv', 'w')as f:
	f.write('商品,名称\n')
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')