import csv

file_path = '/Users/maxeow/Documents/python_files/test/table.csv'
list_id = []
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        list_id.append(row[1])

id_counts = {}
for id in list_id:
    if id in id_counts:
        id_counts[id] += 1
    else:
        id_counts[id] = 1

id_count3 = [id for id, count in id_counts.items() if count == 3]
print('id встречаются 3 раза:', id_count3)

frequency = {}
for count in id_counts.values():
    if count in frequency:
        frequency[count] += 1
    else:
        frequency[count] = 1

print('Частота повторений:')
for count_freq, count_id in frequency.items():
    print(f'{count_id} ID встречается {count_freq} раз')
