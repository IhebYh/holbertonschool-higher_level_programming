#!/usr/bin/python3
"""
filtering states safe from sql injection
"""
import sys
import MySQLdb


def main():
    cn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cursor = cn.cursor()
    safeSearch = sys.agrv[4]
    cursor.execute("""SELECT * FROM states
                    WHERE name = %(safeSearch)s
                    ORDER BY id ASC""", {'safeSearch':safeSearch})
    res = cursor.fetchall()
    for r in res:
        print(r)
    cursor.close()
    cn.close()


if __name__ == "__main__":
    main()
