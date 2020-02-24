import os, re

in_file = 'out-abdulbaha-mmha3.txt'

count = 1

ar =[150,175,189,52,126,197]

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\(\d*\)", str(content))
	x.pop(0)
	print(len(x))

output = os.makedirs("output")

for i in x:
	if i in ar:
		language = 'ar'
	else:
		language = 'fa'
	# os.makedirs(os.path.dirname('output'), exist_ok=True)
	with open('output/abdulbaha-mmha3-{}-{}.txt'.format(count, language), 'w') as out_file:
		out_file.write(i)
		count += 1
