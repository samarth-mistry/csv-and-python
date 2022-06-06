import re
import csv
from datetime import datetime

print('READING input data')
with open('/home/samarth/Projects/py/Everlytics/input_sample.csv', 'r') as input_file:
    reader = csv.DictReader(input_file)
    listDic = list()
    for row in reader:
        listDic.append(dict(row))

print('READING input tags')
with open('/home/samarth/Projects/py/Everlytics/tags.csv', 'r') as tag_file:
    reader = csv.DictReader(tag_file)
    listTag = list()
    for row in reader:
        listTag.append(dict(row))

print('WRITING STARTS')
with open('/home/samarth/Projects/py/Everlytics/output_test.csv', 'w') as output_file:
    writer = csv.writer(output_file, delimiter = '\t')
    writer.writerow(["event_timestamp", "tag__id", "tag__name","tag__desc",'tag__value','tag__unit'])
    for tag in listTag:
        for dicData in listDic:
            unit = re.search('\(([^)]+)', tag['Comment']).group(1) if re.search('\(([^)]+)', tag['Comment']) is not None else ''
            writer.writerow([
                str(datetime.strptime(dicData['Date'], '%m-%d-%Y').strftime("%d/%m/%Y"))+" "+str(dicData['Time']), 
                tag['ItemId'],
                tag['ItemName'],
                tag['Comment'],
                dicData[tag['ItemName']],
                unit
            ])

print('WRITING ENDS')
print('CSV structure changed')
