import os, re

in_file = 'abdulbaha-mha1.txt'

count = 1

fa = [59,60,63,64,65,66,67,68,69,70,71,72,73,75,76,77,78,79,80,81,82,83,84,85,
     86,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,108,109,
	 110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,
	 129,133]

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\[\d*\]", str(content))
	x.pop(0)
	print(len(x))

output = os.makedirs("output")

for i in x:
	if count in fa:
		language = 'fa'
	else:
		language = 'ar'
	# os.makedirs(os.path.dirname('output'), exist_ok=True)
	with open('output/abdulbaha-mha1-{}-{}.txt'.format(count, language), 'w') as out_file:
		out_file.write(i)
		count += 1
