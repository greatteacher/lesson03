import csv

user_list = [
        {'name': 'Мария', 'age': 28, 'job': 'Scientist'}, 
        {'name': 'Артур', 'age': 32, 'job': 'Programmer'}, 
        {'name': 'Ольга', 'age': 31, 'job': 'Teacher'},         
        {'name': 'Лера', 'age': 39, 'job': 'Big boss'},
    ]
with open('exporthm.csv', 'w', encoding='ANSI', newline='') as f:
    fields = ['name', 'job', 'age']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)