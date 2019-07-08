import os, re

in_file = '../abdulbaha-mmha4.txt'

count = 1

ar = [78]

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\(\d*\)", str(content))
	x.pop(0)
	print(len(x))

output = os.makedirs("output")

for i in x:
	if count in ar:
		language = 'ar'
	else:
		language = 'fa'
	# os.makedirs(os.path.dirname('output'), exist_ok=True)
	with open('output/abdulbaha-mmha4-{}-{}.txt'.format(count, language), 'w') as out_file:
		out_file.write(i)
		count += 1
