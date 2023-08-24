import random
from test_SQL_DB import db, Student

first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Daniel', 'Olivia', 'Matthew', 'Sophia']
last_names = ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Wilson']
domains = ['example.com', 'testmail.com', 'school.edu', 'mail.net', 'domain.org']
bios = ['Computer Science major', 'Engineering enthusiast', 'Art history lover', 'Future astronaut', 'Aspiring writer', 'Nature lover', 'Musician in the making', 'Sports fanatic', 'Film critic', 'Mathematics geek']

for _ in range(10):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f'{first_name.lower()}_{last_name.lower()}@{random.choice(domains)}'
    age = random.randint(18, 25)
    bio = random.choice(bios)

    student = Student(firstname=first_name, lastname=last_name, email=email, age=age, bio=bio)
    db.add(student)

db.commit()
