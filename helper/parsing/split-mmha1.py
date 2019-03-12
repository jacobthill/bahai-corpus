import os, re

in_file = 'abdulbaha-mmha1.txt'

count = 1


ar = [3,4,5,9,19,27,38,42,61,78,90,121,122,137,141,143,146,150,151,157,158,159,165,172,175,181,198,199,214,234,235,237]

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\(\d*\)", str(content))
	x.pop(0)

output = os.makedirs("output")

for i in x:
	if count in ar:
		lanuguage = 'ar'
	else:
		lanuguage = 'fa'
	# os.makedirs(os.path.dirname('output'), exist_ok=True)
	with open('output/abdulbaha-mmha1-{}-{}.txt'.format(count, lanuguage), 'w') as out_file:
	    out_file.write(i)
	    count += 1
