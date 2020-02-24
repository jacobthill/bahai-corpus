import os, re

in_file = 'abdulbaha-mha8.txt'

with open(in_file, 'r') as f:
    content = f.read()
    # pattern = re.compile("\(\d*\)")
    # num = 1
    # for match in re.findall(pattern, content):
    for num in range(53,335):
        #     l = []
        m = "({})".format(num)
        #     for m in content:
        #         l.append(m)
        # content = content.strip(match)
        # content = content + "({})".format(num)
        # num+=1
        if m in content:
            print("({})".format(num+1))
        content = content.replace("({})".format(num), "({})".format(num-1))

	# os.makedirs(os.path.dirname('output'), exist_ok=True)
with open('abdulbaha-mha8-new.txt', 'w') as out_file:
	out_file.write(content)
