import sqlite3
import data_generator
 

# called only once to create test db
def create_db():
    # three lists are of the same length
    name_list = data_generator.create_namelist()
    birthdate_list = data_generator.create_birthdatelist()
    PHN_list = data_generator.create_PHNlist()

    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    #create table
    c.execute('''CREATE TABLE patients
                (PHN integer, name text, birthdate text)''')

    #insert tuples
    for index in range(len(name_list)):
        c.execute("INSERT INTO patients VALUES (?,?,?)", (PHN_list[index], name_list[index], birthdate_list[index]))
        #c.execute("INSERT INTO patients VALUES (130450751, 'test name', '03-05-1990')")
    conn.commit()   # save the changes

    # show all records in db
    c.execute('SELECT * FROM patients')
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()


# if a PHN (in list) exists in db, look up for corresponding name and birthdate in db;
# if name and birthdate exists in list, return this tuple (PHN, name, birthdate)
def query_db(PHN_list, name_list, birthdate_list):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    for PHN in PHN_list:
        c.execute("SELECT name, birthdate FROM patients WHERE PHN = ?", (PHN,))
        row = c.fetchone()
        if row is not None:
            name = row[0]
            birthdate = row[1]
            if ((name in name_list) and (birthdate in birthdate_list)):
                print("Match Found!")
                return PHN, name, birthdate
    conn.close()


PHN_list = [101976229, 167834507, 324534199]
name_list = ['Ethel Huddleston', 'Jesse Autry', 'not exist1', 'not exist2']
birthdate_list = ['12/19/1959', '4/17/1954', '1/30/1998']
PHN, name, birthdate = query_db(PHN_list, name_list, birthdate_list)
print(PHN, name, birthdate)


