import os # operating system 作业系统
#读取档案
def read_file(filename):#读取一个文件
	products = []# 设立一个空清单
	with open(filename, 'r')as f:#打开这个文件
		for line in f:#逐行吧这个文件读出来 每一行为line
			if '商品,名称' in line:#如果 商品和名称在这样行里面，包括这个逗号
				continue #继续 ，，把商品，名称剔除
			name,price = line.strip().split(',')#在每一行读取到的line里面操作  strip是去掉空格键 split','意思是以逗号来作为切割 遇到逗号就切一刀
			products.append([name, price])#把切好的name price 存在products里面
	return products# 回转 存入在products里面
			
#让使用者输入
def user_input(products):
	while True:
		name = input('请输入商品名称:')
		if name == 'q':
			break
		price = input('请输入商品价格:')
		products.append([name, price])
	print(products)#这里印出的清单中每一行的商品名称间的逗号 只是两个字符串间的串联而已
	return products


#印出所有购买记录
def print_products(products):
	for product in products:
		print(product[0], '的价格是:', product[1])

#写入档案
def write_file(filename, products):
	with open(filename, 'w')as f:
		f.write('商品,名称\n')
		for product in products:
			f.write(product[0] + ',' + product[1] + '\n')#对应到行9 这里在写入商品和名称的时候 也写入了逗号 逗号在excel里面的表现就是把商品和名称分别在两列里面表现出来 所以在读取到空清单中时 需要去除 


def main():
	filename = 'products.csv'#这里的这个文件名可以改动成你想要读取的档案
	if os.path.isfile(filename):#检查档案在不在
		print('找到档案了！')
		products = read_file(filename)
	else:
		print('找不到档案！')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)
main()