import os
import csv


arr = os.listdir(r"D:\Work\Provectus\Tasks\Level_1\02-src-data")



all_data = []


def store_data(file, usr_id, image_file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            all_data.append([usr_id, row['first_name'], row[' last_name'], row[' birthts'], image_file])


for item in arr:
    if item.endswith('csv'):
        usr_id = item[:4]
        if usr_id+".png" in arr:
            image_file = "02-src-data\\"+usr_id+".png"
            to_read = "02-src-data\\"+item
            store_data(to_read, int(usr_id), image_file)


header = ['user_id', 'first_name', 'last_name', 'birthts', 'img_path']

with open('processed_data/output.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(all_data)

print("DONE!")



    
