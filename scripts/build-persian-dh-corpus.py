import os
from helper import *

def persian_dh_get_filenames(root_dir):
    # Gather all OpenArabic file names
    list_of_filenames = []
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in files:
            if "pdl.xml" in name:
                list_of_filenames.append(os.path.join(root, name))

    return list_of_filenames

in_directory = '/Users/jtim/Dropbox/Academic/sources/corpora/u-maryland-persian/PersDigUMD-PDL-1d9ec24/data'
directory = '/Users/jtim/Dropbox/Academic/sources/corpora/cleaned-persian-dh'
if not os.path.exists(directory):
    os.makedirs(directory)

filenames = persian_dh_get_filenames(in_directory)

for file in filenames:
    with open("{}/{}.txt".format(directory, file.split('/')[-1]), 'w') as out_file:
        out_file.write(text_from_xml(file))
