import re

in_file = 'lh3.txt'

count = 1

fa = [1, 143-203, 205-240]


with open(in_file, 'r') as f:
	content = f.read()
	# y = re.findall("\[\d*\]", str(content))
	# for i in y:
	#     print(i + '\n')
	x = re.split("\[\d*\]", str(content))
	x.pop(0)

for i in x:
	if count < 2:
		language = 'fa'
	elif count > 142 and count < 204:
		language = 'fa'
	elif count > 204 and count < 241:
		language = 'fa'
	else:
		language = 'ar'
	out_file = open('output/bahaullah-lh3-{}-{}.txt'.format(count, language), 'w')
	out_file.write(i)
	count += 1
f.close()
