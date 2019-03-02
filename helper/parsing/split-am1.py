import re

in_file = 'am1.txt'

count = 1

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\(\)", str(content))
	x.pop(0)

for i in x:
	out_file = open('bahaullah-am1-{}-ar.txt'.format(count), 'w')
	out_file.write(i)
	count += 1
f.close()
    
