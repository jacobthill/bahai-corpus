# -*- coding: utf-8 -*-
import re

in_file = "abdulbaha-mha2.txt"
# out_file = open("out-abdulbaha-mmha3.txt", "w")
alphabet = ['ا', 'ب', 'س', 'ن', 'ع', 'ق', 'م', 'ح', 'ر', 'ز',]
count = 0
pages = 0
i = 1
with open(in_file, "r") as f:
    lines = f.readlines()
    for line in lines:
        for i in alphabet:
            if re.search(i, line):
            # print(line)
                count += 1

            else:
                pages += 1
                print(line)
                break
            # line = "(1) {}".format(line)
            # out_file.write(line)
        # elif re.search(r'\d', line) and not re.search(r'_', line):
        #     print(line)
        #     i += 1
        #     pages += 1
        # else:
            # out_file.write(line)
# out_file.close()
print(count, pages)
