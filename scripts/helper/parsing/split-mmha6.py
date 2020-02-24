import os, re

in_file = '../abdulbaha-mmha6.txt'

count = 1

ar = [1,4,9,47,54,57,63,70,71,76,93,113,117,122,148,149,150,151,155,173,187,200,
     205,214,231,236,240,252,267,277,285,287,288,308,309,328,331,348,381,418,
	 431,432,458,462,470,479,482,502,528,541,555,560,597,624,632,643,646]

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
	with open('output/abdulbaha-mmha6-{}-{}.txt'.format(count, language), 'w') as out_file:
		out_file.write(i)
		count += 1
