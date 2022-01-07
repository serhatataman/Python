#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sqlite3


def main():
    print('connecting to db...')
    db = sqlite3.connect('db-api.db')  # creates db if it doesn't exist
    cur = db.cursor()
    print('creating table...')
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('inserting row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('inserting row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('inserting row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)
    print('committing changes...')
    db.commit()
    print('counting rows...')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]  # fetchone() returns a tuple
    print(f'there are {count} rows in the table.')
    print('reading data...')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('dropping table...')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()


if __name__ == '__main__':
    main()
