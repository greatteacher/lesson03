import csv

user_list = [
	{'balance': '18.82','last_name': 'Armstrong','first_name': 'Gloria','email': 'garmstrong0@harvard.edu','gender': 'Female'},
	{'balance': '15.82','last_name': 'Armstrong', 'first_name': 'George','email': 'grgarmstrong0@harvard.edu', 'gender': 'Male'},
	{'balance': '00.50','last_name': 'Scott', 'first_name': 'Mary','email': 'Mary_scott1@skyrock.com', 'gender': 'Female'},
	{'balance': '001.50','last_name': 'Manasova', 'first_name': 'Mary','email': 'Mary_pineapple@skyrock.com', 'gender': 'Female'},
	{'balance': '0.09','last_name': 'Manasik', 'first_name': 'Mary','email': 'Mary_pineaple@gmail.com', 'gender': 'Female'},
	{'balance': '18.82','last_name': 'Armstrong','first_name': 'John','email': 'johnarmstrong0@harvard.edu','gender': 'Male'},
	{'balance': '19.50','last_name': 'Scott','first_name': 'Mandy','email': 'mscott1@skyrock.com','gender': 'Female'},
	{'balance': '91.5','last_name': 'Scott','first_name': 'Sindy','email': 'ascott1@skyrock.com','gender': 'Female'}
]

with open('exportnew.csv', 'w', encoding='utf-8', newline='') as f:
    fields = ['first_name', 'last_name', 'email', 'gender', 'balance']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)