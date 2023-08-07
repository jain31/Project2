import csv
with open (r'C:/Desktop/reviews.csv', encoding = 'utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            print(f'\n\n')
            line_count += 1
        else:
             print(f'\t {row[0]} \t {row[1]} \t {row[2]} \t {row[3]} \t {row[4]}')
             print(f'\t {row[6]} \t {row[7]} \n\n')
             line_count += 1
                
                                
with open (r'C:/Desktop/items.csv', encoding = 'utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are   {"  , ".join(row)}')
            print(f'\n\n')
            line_count += 1
        else:
             print(f'\t {row[0]}   {row[1]}   {row[2]}    {row[3]}  {row[4]}')
             print(f'\t {row[6]} \t  {row[7]} \t {row[8]} \t {row[9]}  \n\n')
             line_count += 1






# In[ ]:




