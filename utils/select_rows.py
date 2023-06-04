import csv
import os

input_filename ='cleandata.csv'

index_excercise= 6 # Specify the corresponding excercise
indexes = [2,15]  # Specify the desired indexes here

path = 'model/data'
input_file= os.path.join(path,input_filename)
output_filename = 'exo_' + str(index_excercise) + '.csv'
output_file = os.path.join(path,output_filename)

def select_rows(input_file,output_file,indexes=[]):    
    with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:
        reader = csv.reader(csv_in)
        writer = csv.writer(csv_out)

        selected_rows = [row for row in reader if int(float(row[0])) in indexes]

        writer.writerows(selected_rows)

select_rows(input_file, output_file, indexes=indexes)