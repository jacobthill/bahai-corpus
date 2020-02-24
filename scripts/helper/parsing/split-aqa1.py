import re

in_file = 'aqa1.txt'

count = 1

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\(\d*\)", str(content))
	x.pop(0)

for i in x:
	# if count = 1:
	# 	language = 'fa'
	# else:
	# 	lanuguage = 'ar'
	out_file = open('bahaullah-aqa1-{}-ar.txt'.format(count), 'w')
	out_file.write(i)
	count += 1
f.close()
    
