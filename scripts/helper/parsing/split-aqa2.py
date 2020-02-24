import re

in_file = 'aqa2.txt'

count = 1


fa = [68,69,70,71,98]

with open(in_file, 'r') as f:
	content = f.read()
	x = re.split("\(\d*\)", str(content))
	x.pop(0)

for i in x:
	if count in fa:
		lanuguage = 'fa'
	else:
		lanuguage = 'ar'
	out_file = open('bahaullah-aqa2-{}-{}.txt'.format(count, lanuguage), 'w')
	out_file.write(i)
	count += 1
f.close()
    
