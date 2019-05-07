import os, re

in_file = 'abdulbaha-mha2.txt'

count = 1

ar = [14,17,23,24,35,36,37,38,41,42,47,48,49,50,51,53,56,57,58,59,60,61,65,66,
     67,71,81,82,83,86,87,88,89,90,91,94,96,97,98,99,100,101,103,106,107,109,
     110,111,112]

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\[\d*\]", str(content))
	x.pop(0)
	print(len(x))

output = os.makedirs("output")

for i in x:
	if i in ar:
		language = 'ar'
	else:
		language = 'fa'
	# os.makedirs(os.path.dirname('output'), exist_ok=True)
	with open('output/abdulbaha-mha2-{}-{}.txt'.format(count, language), 'w') as out_file:
		out_file.write(i)
		count += 1
