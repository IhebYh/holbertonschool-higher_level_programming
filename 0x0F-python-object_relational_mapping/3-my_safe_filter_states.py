#!/usr/bin/python3
"""
filtering states safe from sql injection
"""
from sys import argv
import MySQLdb


def main():
    cn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=argv[1],
                        passwd=argv[2],
                        db=argv[3],
                        charset="utf8"
                            )
    cursor = cn.cursor()
    cursor.execute("""SELECT * FROM states
                    WHERE name Like %s
                    ORDER BY id ASC""", (argv[4],))
    res = cursor.fetchall()
    for r in res:
        print(r)
    cursor.close()
    cn.close()


if __name__ == "__main__":
    main()
