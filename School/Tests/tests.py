import sqlite3
import os
import sys
path = os.path.join(os.path.join(os.path.dirname(__file__), os.pardir), os.pardir)
sys.path.append(path)
from settings import *
import datetime
def init_db(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = """CREATE TABLE Tests (
        testid INTEGER PRIMARY KEY AUTOINCREMENT,
        subject varchar(255),
        date DATE,
        type varchar(255));"""
    cur.execute(sql)
    return conn, cur

def create_new_test(conn, cur, subject, date, type='CR'):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    sql = f"INSERT INTO Tests VALUES (NULL, '{subject}','{date}', '{type}');"
    cur.execute(sql)
    conn.commit()
    return conn, cur

def check_input(type, subject):
    set_subjects = ['math','ai',  "biology", "chemistry", "hindi", "physics", "history", "geography", "civics", "telugu", "english"]
    if subject.lower() in set_subjects:
        final_subject = subject
    else:
        final_subject = ''
    set_types = ['lr', 'cr', 'pt-1', 'pt-1', 'half-yearly', 'final']
    if type.lower() in set_types:
        final_type = type
    else:
        final_type=''
    return final_subject.upper(), final_type.upper()
today  = datetime.date.today()
year = today.year
subject, day, month, type, year = get_shell_input(3, sys.argv, ['', year])

date  = f"{day} {month}, {year}"
converted_date = datetime.datetime.strptime(date, '%d %B, %Y')
final_date = datetime.datetime.strftime(converted_date, '%Y-%m-%d')

path = '/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/Automation/School/Tests/tests.sqlite'
if not os.path.exists(path):
    conn, cur = init_db(path)
else:
    conn = sqlite3.connect(path)
    cur = conn.cursor()
subject, type = check_input(type, subject)
if type != '':
    conn, cur = create_new_test(conn, cur, subject, final_date, type)
else:
    conn, cur = create_new_test(conn, cur, subject, final_date)
