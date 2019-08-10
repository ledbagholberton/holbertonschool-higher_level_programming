#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    name2 = argv[4].split("';")
    cur = conn.cursor()
    cur.execute(("SELECT cities.name\
    FROM cities LEFT OUTER JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name = '{}'\
    ORDER BY cities.id ASC").format(name2[0]))
    query_rows = cur.fetchall()
    num = list(sum(query_rows, ()))
    num = ', '.join(map(str, num))
    print(num)
    cur.close()
    conn.close()
