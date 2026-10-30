import sqlite3
import string
def config():

    time = input('Please input an interger: ')
    
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS time (
            number INTEGER
        )
    """)

    cursor.execute(
        "INSERT INTO time (number) VALUES (?)",
        (time)
    )

    print("succesful")

    conn.commit()
    conn.close()

def load():
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()

    cursor.execute("SELECT number FROM time")

    rows = cursor.fetchall()

    for row in rows:
        time = row

    if not sum(time) <= 0:

        print('You have', sum(time), "times left to load")

        timetoprint = sum(time) - 1


        cursor.execute(
                "INSERT INTO time (number) VALUES (?)",
                (timetoprint,)
            )
        conn.commit()


        conn.close()
    else:
        print('You can not save')

action = input("Type an action: ")


print(action)

if action.lower() == 'load':
    print("action is load")
    load()

if action.lower() == "config":
    print("action is write")
    config()