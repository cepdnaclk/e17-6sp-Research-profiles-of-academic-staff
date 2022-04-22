import json
import csv
from json.decoder import JSONDecodeError

fileList = ['1.json','2.json']
List=[]
result={}
data_list = []

for i in range(len(fileList)):
    
    with open(fileList[i], "r") as infile:
        result= json.load(infile)
        result_copy=result.copy()
        List.append(result_copy)
   
out_file = open("dataSet.json", "a")
json.dump(List, out_file, indent=2)
out_file.close()

# Read the JSON file as python dictionary
filename="dataSet.json"
with open(filename, "r") as f:
        data = json.loads(f.read())

print (data)
publications_info = ['type', 'title', 'book title', 'abstract', 'year',
                     'Authors', 'DOI', 'pdf', 'publication url', 'presentation', 'code', 'tags']

with open('dataSet.csv', 'a',newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=publications_info)
    writer.writeheader()
    writer.writerows(data)
