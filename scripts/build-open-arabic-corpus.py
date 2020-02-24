import os
from helper import *
from multiprocessing import *

def open_arabic_get_filenames(root_dir):
    # Gather all OpenArabic file names
    list_of_filenames = []
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in dirs:
            if name.startswith('11') or name.startswith('12') or name.startswith('13'):
                for name in files:
                    if not name.startswith('.'):
                        if ".md" in name:
                            pass
                        elif ".yml" in name:
                            pass
                        # elif ".mARkdown" in name: # prioritize mARkdown works
                        #     list_of_filenames.append(os.path.join(root, name))
                        # elif ".completed" in name: # then completed works
                        #     list_of_filenames.append(os.path.join(root, name))
                        # elif ".inProgress" in name: # then inProgress works
                        #     list_of_filenames.append(os.path.join(root, name))
                        # elif "Shamela" in name: # then arbitrarily choose Shamela works
                        #         list_of_filenames.append(os.path.join(root, name))
                        else:
                            list_of_filenames.append(os.path.join(root, name))
    print(list_of_filenames)
    return list_of_filenames

def open_arabic_clean_files(file):
    # Remove html, structural markings, etc. from Open Arabic texts
    directory = '/Users/jtim/Dropbox/Academic/sources/corpora/open-iti-1100-1399-clean'
    if not os.path.exists(directory):
        os.makedirs(directory)
    list_of_junk_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                               'n','o','p','q','r','s','t','u','v','w','x','y','z',
                               '0','1','2','3','4','5','6','7','8','9','<','>','/',
                               '=','|','~','#','-',':']

    with open("{}/{}.txt".format(directory, file.split('/')[-1]), 'w') as out_file:
        with open(file, 'r') as f:
            contents = f.read()
            for char in contents:
                if char.lower() in  list_of_junk_characters:
                    pass
                else:
                    out_file.write(char)

# Get Open Arabic corpus
twelfth_c = open_arabic_get_filenames("/Users/jtim/Dropbox/Academic/sources/corpora/open-arabic-1200AH/data")
thirteenth_c = open_arabic_get_filenames("/Users/jtim/Dropbox/Academic/sources/corpora/open-arabic-1300AH/data")
fourteenth_c = open_arabic_get_filenames("/Users/jtim/Dropbox/Academic/sources/corpora/open-arabic-1400AH/data")
# murtada_ansari = open_arabic_get_filenames("/Users/jtim/Dropbox/Academic/sources/corpora/open-iti/data/1281MurtadaAnsari")
combined_filenames = twelfth_c + thirteenth_c + fourteenth_c

for file in combined_filenames:
    open_arabic_clean_files(file)

# easy_parallize(open_arabic_clean_files, combined_filenames)
