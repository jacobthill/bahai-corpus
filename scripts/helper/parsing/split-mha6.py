import os, re

in_file = '../abdulbaha-mha6.txt'

count = 1

ar = [1,4,5,34,51,52,68,69,70,71,72,73,74,75,83,92,94,150,166,184,185,212,213,
     216]

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
	with open('output/abdulbaha-mha6-{}-{}.txt'.format(count, language), 'w') as out_file:
		out_file.write(i)
		count += 1
