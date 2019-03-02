import csv
import re

from os import listdir
from os.path import isfile, join

published_volumes = {
                    'aiab': 'مناجاة مَجْمُوعَةُ أذكارٍ وَأدْعِيَةٍ مِنْ آثارِ حضرة بهاءالله',
                    'am1': 'ادعيه مباركه، جلد ١',
                    'am2': 'ادعيه مباركه، جلد ٢',
                    'am3': 'ادعيه مباركه، جلد ٣',
                    'amtm': 'مجموعة الواح مباركة طبعة مصر',
                    'anbka': 'مجموعه اى از الواح جمال اقدس ابهى كه بعد از كتاب اقدس نازل شده',
                    'aqa1': 'آثار قلم اعلى، جلد ١',
                    'aqa2': 'آثار قلم اعلى، جلد ٢',
                    'aqa3': 'آثار قلم اعلى، جلد ٣',
                    'lh1': 'لئالئ الحكمة، جلد ١',
                    'lh3': 'لئالئ الحكمة، جلد ٣',
                    'lkshmi': 'لوح خطاب به شيخ محمد تقي اصفهاني',
                    'st': 'oceanoflights.org'
}

def to_str(bytes_or_str):
    '''Takes bytes or string and returns string'''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str

    return value  # Instance of str

file_path = '../data/bahaullah/text'
text_files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

stripped_files = [re.sub("bahaullah-", "", f) for f in text_files]

source_abbrevation = re.compile(r"^[^-]*")

with open('../tablets.csv', mode='w') as csv_file:
    field_names = ['Author', 'Source', 'File Name', 'Name', 'Incipit']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)

    writer.writeheader()
    count = 1
    for file in stripped_files:
        source = re.search(source_abbrevation, file).group(0)

        with open('{}/bahaullah-{}'.format(file_path, file), 'rb') as f:
            count += 1
            contents = to_str(f.read())
            contents = contents.replace('\u200c', '')
            contents = contents.replace('\u202c', '').split()

            incipit_list = contents[0:19]
            incipit_string = ' '.join(incipit_list)
        writer.writerow({"Author": "Bahá'u'lláh", "Source": published_volumes.get(source),
                       "File Name": 'bahaullah-{}'.format(file), "Name": "", "Incipit": incipit_string})
csv_file.close()
