import csv
with open('data/IDS2018/Data.csv', 'r') as infile_1, open('data/IDS2018/Label.csv', 'r') as infile_2:
    lines_1=csv.reader(infile_1)
    lines_1=list(lines_1)
    lines_2=csv.reader(infile_2)
    lines_2=list(lines_2)
for i in range(len(lines_1)):
    lines_1[i]+=lines_2[i]
output=[[line[2],line[0],line[1],line[3]] for line in lines_1]
formatted=[' '.join(row)+'\n' for row in output]
with   open('data/IDS2018/no_header.txt', 'w') as fw:
    fw.writelines(formatted)

# with open('data/IDS2018/format.csv', 'w') as fw:
#     # fieldnames =['node1', 'node2', 'ts','label']
#     fieldnames =['ts','node1', 'node2', 'label']
#     writer = csv.DictWriter(fw, fieldnames=fieldnames)
#     writer.writeheader()
#     for line in lines_1:
#         writer.writerow({'ts':line[2],'node1':line[0],'node2':line[1],'label':line[3]})

# with open('data/IDS2018/Data.csv', 'r') as fr,open('data/IDS2018/format.csv', 'w') as fw:
#     # fieldnames =['node1', 'node2', 'ts','label']
#     fieldnames =['ts','node1', 'node2', 'label']
#     writer = csv.DictWriter(fw, fieldnames=fieldnames)    
#     # reorder the header first
#     writer.writeheader()
#     for row in csv.DictReader(fr):
#         # writes the reordered rows to the new file
#         writer.writerow(row)

# with open('data/IDS2018/format.csv', 'r') as fr,open('data/IDS2018/no_header.txt', 'w') as fw:
#     reader = csv.reader(fr)
#     next(reader, None)  # skip the headers
#     rows=list(reader)
#     output=[' '.join(row)+'\n' for row in rows]
#     fw.writelines(output)

    # writer = csv.writer(fw)
    # for row in reader:
    #     # process each row
    #     writer.writerow(row)