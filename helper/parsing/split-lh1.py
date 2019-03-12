import re

in_file = 'lh1.txt'

count = 1
language = 'ar'
with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\(\d*\)", str(content))
	x.pop(0)

for i in x:
	if count > 74:
		language = 'fa'
	out_file = open('bahaullah-lh1-{}-{}.txt'.format(count, language), 'w')
	out_file.write(i)
	count += 1
f.close()
