#!/usr/bin/python3
"""Query with argv[4] equal to Name"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    name2 = argv[4]
    cur = conn.cursor()
    cur.execute(("SELECT * FROM states WHERE name='{}'\
                 ORDER BY id ASC").format(name2))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
