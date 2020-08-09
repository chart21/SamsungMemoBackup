import os
import re
import glob
import zipfile
import xmltodict
from datetime import datetime

#set path where you saved your .memo files
MEMO_PATH = r'C:\Users\User\Documents\ShareMemo\'
RESULTS_PATH = r'C:\Users\User\Documents\ShareMemo\'

memos = glob.glob(MEMO_PATH + '\*.memo')

for i, memo in enumerate(memos):
    print('{}/{} - {}'.format(i+1, len(memos), memo))

    try:
        # Extract *.memo file and read the content
        archive = zipfile.ZipFile(memo, 'r')
        memo_content = archive.read('memo_content.xml').decode('utf-8')
        cleanr = re.compile('&.*?;')
        memo_content = re.sub(cleanr, '', memo_content)
        memo_content = xmltodict.parse(memo_content)
        text = memo_content['memo']['contents']['content']

        timestamp = int(memo_content['memo']['header']['meta'][3]['@createdTime'][:10])
        title = str(memo_content['memo']['header']['meta'][0]['@title'])
        date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H-%M-%S')
        
        file_name = '{} '.format(date) +title+ '.txt'

        # Save file as a *.txt
        with open(os.path.join(RESULTS_PATH, file_name), 'w', encoding='utf-8') as file:
            file.write(text)

    except zipfile.BadZipFile:
        continue


dir_path = os.path.dirname(os.path.realpath(__file__))
for fn in os.listdir(dir_path):    
    if os.path.isfile(fn) and fn.endswith('.txt'):        
        
        
        #read input file
        fin = open(fn, "rt", encoding="utf-8")
        #read file contents to string
        data = fin.read()
        #replace all occurrences of the required string
        data = data.replace('/pp', '\n')
        data = data.replace("p value=\"memo2\" ", "")
        data = data.replace('/p', '')
        #close the input file
        fin.close()
        #open the input file in write mode
        fin = open(fn, "wt", encoding="utf-8")
        #overrite the input file with the resulting data
        #target.write(unicode(source.read(), sourceEncoding).encode(targetEncoding))
        fin.write(data)
        
        fin.close()

        

 