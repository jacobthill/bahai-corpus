import glob, os
from lxml import etree
from numpy import asarray

def build_corpus(path_to_parent_dir, authors, languages):
    # Gather all file names
    file_names = []
    for author in authors:
        os.chdir(path_to_parent_dir)
        for language in languages:
            file_names.extend(glob.glob('{}/text/*{}.txt'.format(author, language)))

    return file_names

def easy_parallize(function, sequence):
    # Multiprocessing
    from multiprocessing import Pool
    pool = Pool(processes=8)

    result = pool.map(function, sequence)
    cleaned = [x for x in result if not x is None]
    cleaned = asarray(cleaned)
    pool.close()
    pool.join()
    return cleaned

def open_arabic_clean_files(file):
    # Remove html, structural markings, etc. from Open Arabic texts
    directory = '/Users/jtim/Dropbox/Academic/sources/corpora/cleaned-open-arabic'
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

def open_arabic_get_filenames(root_dir):
    # Gather all OpenArabic file names
    list_of_filenames = []
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for name in dirs:
            if name == "arc":
                pass # ignore archived version of works
            else:
                for name in files:
                    if ".mARkdown" in name: # prioritize mARkdown works
                        list_of_filenames.append(os.path.join(root, name))
                    elif ".completed" in name: # then completed works
                        list_of_filenames.append(os.path.join(root, name))
                    elif ".inProgress" in name: # then inProgress works
                        list_of_filenames.append(os.path.join(root, name))
                    elif "ara1" in name:
                        if "Shamela" in name: # then arbitrarily choose Shamela works
                            list_of_filenames.append(os.path.join(root, name))

    return list_of_filenames

def process(text):
    # Final processing steps
    char = 1611 # replace all diacritics
    for i in range(20):
        text = text.replace(chr(char), "") # decimal
        char += 1
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace('"', '')
    text = text.replace(":", "")
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("{", "")
    text = text.replace("}", "")
    text = text.replace("؛", "")
    text = text.replace(";", "")
    text = text.replace("؟", "")
    text = text.replace("!", "")
    text = text.replace("ء", "")
    text = text.replace("«", "")
    text = text.replace("»", "") 
    text = text.replace(chr(46), " .") # period
    text = text.replace(chr(46), "") # period
    text = text.replace(chr(10), "") # period
    text = text.replace(chr(1548), " ,") # comma
    text = text.replace(chr(1548), "") # comma
    text = text.replace(chr(44), "") # comma
    text = text.replace(chr(10), "") # data link escape
    text = text.replace(chr(12), "") # formfeed
    text = text.replace(chr(8236), "") # pop directional formatting
    text = text.replace(chr(8235), "") # right-to-left embedding
    text = text.replace(chr(9), "") # character tabulation
    text = text.replace(chr(42), "") # asterisk
    text = text.replace(u'\u200c',' ') # half space
    text = text.replace(u'\u200d',' ') # zero width joiner
    # replace all diacritics, remove garbage values, and normalize charcters
    text = text.replace(chr(1600), "") # tatweel
    text = text.replace(chr(1705), chr(1603)) # kaf
    text = text.replace(chr(1609), chr(1610)) # ya
    text = text.replace(chr(1740), chr(1610)) # ya
    text = text.replace(chr(1574), chr(1610)) # ya
    text = text.strip("")
    return text

def text_from_xml(file):
    # Extract text from xml object
    text = ""
    parser = etree.XMLParser(ns_clean=True)
    tree = etree.parse(file, parser)
    root = tree.getroot()
    for element in root[1].iter():
        if element.text:
            text += element.text + "\n"

    return text
