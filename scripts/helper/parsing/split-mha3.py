import os, re

in_file = '../abdulbaha-mha3.txt'

count = 1

ar = [39, 43, 48, 51, 53, 54, 55, 56, 57, 71, 72, 73, 76, 77, 84, 90, 93, 101, 109, 124, 141, 173, 177, 222, 223]

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\[\d*\]", str(content))
	x.pop(0)
	print(len(x))

output = os.makedirs("output")

for i in x:
	if count in ar:
		language = 'ar'
	else:
		language = 'fa'
	# os.makedirs(os.path.dirname('output'), exist_ok=True)
	with open('output/abdulbaha-mha3-{}-{}.txt'.format(count, language), 'w') as out_file:
		out_file.write(i)
		count += 1
