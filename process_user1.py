import csv

with open('export.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)