
f = open('add_rank.sql', 'w')
x = open('northwind.rank', 'r')
lines = x.readlines()
for line in lines:
	tablename = line.split('-')[0]
	line = line.split('-')[1]
	id = line.split(' ')[0]
	value = line.split(':')[1]
	value = value.split('\n')[0]
	f.write("update %s set rank = %s where id = %s;\n"%(tablename, value, id))

f.close()
x.close()