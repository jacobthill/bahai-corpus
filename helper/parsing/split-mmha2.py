import os, re

in_file = 'abdulbaha-mmha2.txt'

count = 1

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\(\d*\)", str(content))
	x.pop(0)

output = os.makedirs("output")

lanuguage = 'fa'
for i in x:
	# os.makedirs(os.path.dirname('output'), exist_ok=True)
	with open('output/abdulbaha-mmha2-{}-{}.txt'.format(count, lanuguage), 'w') as out_file:
		out_file.write(i)
		count += 1
