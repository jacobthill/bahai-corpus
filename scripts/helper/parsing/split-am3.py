import re

in_file = 'am3.txt'

count = 1

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\(\d*\(", str(content))
	x.pop(0)

for i in x:
	if count > 146:
		language = "fa"
	else:
		language = "ar"
	out_file = open('bahaullah-am3-{}-{}.txt'.format(count, language), 'w')
	out_file.write(i)
	count += 1
f.close()
    
