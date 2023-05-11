import sqlite3
import os
import sys
path = os.path.join('/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/Automation/')
sys.path.append(path)
from settings import *
from Managers.database_manager import DBManager
import datetime as dt

def create_new_test(conn, cur, subject, date, type='CR'):
    details = (subject, date, type)
    sql = f"INSERT OR IGNORE INTO Tests VALUES (NULL, '{subject}','{date}', '{type}');"
    insert_permission = check_duplicates(details, cur)
    if insert_permission:
        cur.execute(sql)
        conn.commit()
    else:
        pass
    return conn, cur

def check_duplicates(details : tuple, cur):
    sql = f'SELECT * FROM Tests WHERE subject = ? AND date = ? AND type = ?;'
    cur.execute(sql, details)
    row = cur.fetchone()
    if row == None:
        return True
    else:
        return False
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

def setup_db(cur):
    sql = """CREATE TABLE Tests (
        testid INTEGER PRIMARY KEY AUTOINCREMENT,
        subject varchar(255),
        date DATE,
        type varchar(255));"""
    cur.execute(sql)
    return cur

if __name__ == '__main__':
    today  = dt.date.today()
    year = today.year
    subject, day, month, type, year = get_shell_input(3, sys.argv, ['', year])

    date  = f"{day} {month}, {year}"
    converted_date = dt.datetime.strptime(date, '%d %B, %Y')
    final_date = dt.datetime.strftime(converted_date, '%Y-%m-%d')

    path = '/Users/abhijitrawool/Documents/Sarthak/Programming_Projects/Automation/School/Tests/tests.sqlite'
    if not os.path.exists(path):
        DBM = DBManager(path)
        conn, cur = DBM.get_connection
        cur = setup_db(cur)
    else:
        DBM = DBManager(path)
        conn, cur = DBM.get_connection
    subject, type = check_input(type, subject)
    if type != '':
        conn, cur = create_new_test(conn, cur, subject, final_date, type)
    else:
        conn, cur = create_new_test(conn, cur, subject, final_date)
