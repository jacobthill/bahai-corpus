import re

in_file = 'lh2.txt'

count = 1

fa = [1,12,13,14,27,28,30,31,33,35,36,39,42,43,46,47,48,52,53,54,56,
	  58,59,64,69,70,77,80,84,85,86,87,88,91,95,101,103,104,105,110,
	  112,114,115,116,117,118,119,138,139,140,141,142,144,145]


with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\[\d*\]", str(content))
	x.pop(0)

for i in x:
	if count in fa:
		language = 'fa'
	else:
		lanuguage = 'ar'
	out_file = open('bahaullah-lh2-{}-{}.txt'.format(count, language), 'w')
	out_file.write(i)
	count += 1
f.close()
    
