# -*- coding: utf-8 -*-
import re

in_file = "abdulbaha-mmha3.txt"
out_file = open("out-abdulbaha-mmha3.txt", "w")
count = 0
pages = 0
i = 1
with open(in_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        if re.search(r'_', line):
            # print(line)
            count += 1
            line = "(1) {}".format(line)
            out_file.write(line)
        elif re.search(r'\d', line) and not re.search(r'_', line):
            print(line)
            i += 1
            pages += 1
        else:
            out_file.write(line)
out_file.close()
print(count, pages)
