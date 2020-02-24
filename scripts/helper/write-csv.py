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
                    'bkw05': 'oceanoflights.org',
                    'bkw06': 'oceanoflights.org',
                    'bkw07': 'oceanoflights.org',
                    'bkw08': 'oceanoflights.org',
                    'bkw09': 'oceanoflights.org',
                    'bkw10': 'oceanoflights.org',
                    'bkw11': 'oceanoflights.org',
                    'bkw12_1': 'oceanoflights.org',
                    'bkw12_2': 'oceanoflights.org',
                    'bkw15': 'oceanoflights.org',
                    'bkw16': 'oceanoflights.org',
                    'bkw17': 'oceanoflights.org',
                    'bkw18': 'oceanoflights.org',
                    'bkw19': 'oceanoflights.org',
                    'bkw21': 'oceanoflights.org',
                    'bkw23': 'oceanoflights.org',
                    'bkw24': 'oceanoflights.org',
                    'bkw25': 'oceanoflights.org',
                    'bkw27': 'oceanoflights.org',
                    'bkw28': 'oceanoflights.org',
                    'bkw29': 'oceanoflights.org',
                    'lh1': 'لئالئ الحكمة، جلد ١',
                    'lh3': 'لئالئ الحكمة، جلد ٣',
                    'lkshmi': 'لوح خطاب به شيخ محمد تقي اصفهاني',
                    'mha1': '۱ مكاتيب حضرت عبدالبهاء جلد',
                    'mha2': '۲ مكاتيب حضرت عبدالبهاء جلد',
                    'mha3': '۳ مكاتيب حضرت عبدالبهاء جلد',
                    'mha4': '۴ مكاتيب حضرت عبدالبهاء جلد',
                    'mha5': '۵ مكاتيب حضرت عبدالبهاء جلد',
                    'mha6': '۶ مكاتيب حضرت عبدالبهاء جلد',
                    'mha7': '۷ مكاتيب حضرت عبدالبهاء جلد',
                    'mha8': '۸ مكاتيب حضرت عبدالبهاء جلد',
                    'mmha1': '۱ منتخباتى از مكاتيب حضرت عبدالبهاء جلد',
                    'mmha2': '۲ منتخباتى از مكاتيب حضرت عبدالبهاء جلد',
                    'mmha3': '۳ منتخباتى از مكاتيب حضرت عبدالبهاء جلد',
                    'mmha4': '۴ منتخباتى از مكاتيب حضرت عبدالبهاء جلد',
                    'mmha5': '۵ منتخباتى از مكاتيب حضرت عبدالبهاء جلد',
                    'mmha6': '۶ منتخباتى از مكاتيب حضرت عبدالبهاء جلد',
                    'mufavidat': 'مفاوضات',
                    'monajat': 'مجموعه مناجاتها حضرت عبدالبهاء',
                    'st': 'oceanoflights.org',
                    'tv': 'تذكرة الوفاء',

}

def to_str(bytes_or_str):
    '''Takes bytes or string and returns string'''
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str

    return value  # Instance of str

# Contains all of the normalization logic
def normalize_carachters(text):
    char = 1611
    for i in range(20):
        text = text.replace(chr(char), "") # decimal
        char += 1
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("﴾", "")
    text = text.replace("﴿", "")
    text = text.replace('"', '')
    text = text.replace(":", "")
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace(chr(46), " .") # period
    text = text.replace(chr(46), "") # period
    text = text.replace(chr(10), "") # period
    text = text.replace(chr(1548), " ,") # comma
    text = text.replace(chr(1548), "") # comma
    text = text.replace(chr(44), "") # comma
    text = text.replace(chr(12), "") # formfeed
    text = text.replace(chr(8236), "") # pop directional formatting
    text = text.replace(chr(8235), "") # right-to-left embedding
    text = text.replace(chr(12), "") # formfeed
    text = text.replace(chr(9), "") # character tabulation
    text = text.replace(chr(42), "") # asterisk
    text = text.replace(chr(1600), "") # tatweel
    text = text.replace(chr(1705), chr(1603)) # kaf
    text = text.replace(chr(1609), chr(1610)) # ya
    text = text.replace(chr(1740), chr(1610)) # ya
    text = text.replace(chr(1574), chr(1610)) # ya
    text = text.strip("")
    return text

### Baha'u'llah
file_path = '../data/bahaullah/text'
text_files = [f for f in listdir(file_path) if not f.startswith('.') and isfile(join(file_path, f))]

stripped_files = [re.sub("bahaullah-", "", f) for f in text_files]

source_abbrevation = re.compile(r"^[^-]*")

with open('../bahaullah-tablets.csv', mode='w') as csv_file:
    field_names = ['Author', 'Source', 'File Name', 'Name', 'Incipit']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)

    writer.writeheader()
    count = 1
    for file in stripped_files:
        source = re.search(source_abbrevation, file).group(0)

        with open('{}/bahaullah-{}'.format(file_path, file), 'rb') as f:
            count += 1
            contents = to_str(f.read())
            contents = normalize_carachters(contents).split()

            incipit_list = contents[0:19]
            incipit_string = ' '.join(incipit_list)
        writer.writerow({"Author": "Bahá'u'lláh", "Source": published_volumes.get(source),
                       "File Name": 'bahaullah-{}'.format(file), "Name": "", "Incipit": incipit_string})
csv_file.close()


### ABdul-Baha
file_path = '../data/abdulbaha/text'
text_files = [f for f in listdir(file_path) if not f.startswith('.') and isfile(join(file_path, f))]

stripped_files = [re.sub("abdulbaha-", "", f) for f in text_files]

source_abbrevation = re.compile(r"^[^-]*")

with open('../abdulbaha-tablets.csv', mode='w') as csv_file:
    field_names = ['Author', 'Source', 'File Name', 'Name', 'Incipit']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)

    writer.writeheader()
    count = 1
    for file in stripped_files:
        source = re.search(source_abbrevation, file).group(0)

        with open('{}/abdulbaha-{}'.format(file_path, file), 'rb') as f:
            count += 1
            contents = to_str(f.read())
            contents = normalize_carachters(contents).split()

            incipit_list = contents[0:19]
            incipit_string = ' '.join(incipit_list)
        writer.writerow({"Author": "Abdu'l-Bahá", "Source": published_volumes.get(source),
                       "File Name": 'abdulbaha-{}'.format(file), "Name": "", "Incipit": incipit_string})
csv_file.close()
