# import django
# print(django.get_version())

# django-admin startproject mysite -> in CMD to create django project
# py manage.py runserver -> in CMD to run server path is outer layer of "mysite"

import sqlite3
from employee import Employee

#conn = sqlite3.connect('pythonDB.db') # Creating connection to DB
conn = sqlite3.connect(':memory:') # Creating database to RAM, Great for testing purposes
curr = conn.cursor()     # Creating cursor to point to DB


# Creating table in the DB

curr.execute("""CREATE TABLE employees (      
            first  text,
            last text,
            pay integer
            )""")




def insert_emp(emp): # Function for inserting employyes to database
    with conn:
        curr.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
        { 'first': emp.first,'last': emp.last, 'pay': emp.pay })

def get_emps_by_name(lastname): # Function for getting employees by last name
    curr.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return curr.fetchall()

def update_pay(emp,pay): # Function for updating employees pay
    with conn:
        curr.execute("""UPDATE employees SET pay = :pay
                        WHERE first = :first AND last = :last""",
                        {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp): # Function to remove employee
    with conn:
        curr.execute("DELETE from employees WHERE first = :first AND last= :last",
                    {'first': emp.first, 'last':emp.last})  




# curr.execute("INSERT INTO employees VALUES ('Oskari', 'Manninen', '10000')")

emp_1 = Employee('John','Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)
emps = get_emps_by_name('Doe')
print(emps)
conn.close()


# curr.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))  # -> string formatting is bad practise while dealing with SQL databases since it creates vulnerability to SQL injections 
# curr.execute("INSERT INTO employees VALUES (?, ?, ?)",(emp_1.first, emp_1.last, emp_1.pay))  # -> this is better way to do the later, needs to pass tuple on emp_1.first...
# curr.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
# {'first': emp_2.first,'last': emp_2.last, 'pay': emp_2.pay })  # -> this is more informative way to do but requires to pass a dictionary


# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)

# curr.execute("SELECT * FROM employees")
# print(curr.fetchone()) # -> fetches one
# print(curr.fetchmany(5)) # -> return values as a list





# curr.execute("SELECT * FROM employees WHERE last=?", ('Schafer',)) # needs to be tuple with question mark so needs an extra comma at the end with one value
# print(curr.fetchall())


# curr.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'}) #a bit more readable with one value
# print(curr.fetchall())

#print(curr.fetchall()) # -> get all as a list
# conn.commit() # Commiting the changes
# conn.close() # closing the connection