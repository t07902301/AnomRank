import csv,sys
def prerpocess_data(data_path,label_path,output_path):
    with open(data_path, 'r') as infile_1, open(label_path, 'r') as infile_2:
        print('Reading data from file {}'.format(data_path))
        lines_1=csv.reader(infile_1)
        lines_1=list(lines_1)
        print('Done.')
        print('Get labels from file {}'.format(label_path))
        lines_2=csv.reader(infile_2)
        lines_2=list(lines_2)
        print('Done.')
    for i in range(len(lines_1)):
        lines_1[i]+=lines_2[i]
    output=[[line[2],line[0],line[1],line[3]] for line in lines_1]
    formatted=[' '.join(row)+'\n' for row in output]
    with   open(output_path, 'w') as fw:
        fw.writelines(formatted)
if __name__=='__main__':
    '''
    data_path: path_of_data_file.csv 
    label_path: path_of_labels_file.csv 
    output_path: *.txt
    '''
    data_path,label_path,output_path=sys.argv[1:]
    prerpocess_data(data_path,label_path,output_path)