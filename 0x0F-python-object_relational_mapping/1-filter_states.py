#!/usr/bin/python3
"""
filtering states
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
    query = "SELECT * FROM states WHERE name Like 'N%' ORDER BY id ASC"
    cursor.execute(query)
    res = cursor.fetchall()
    for r in res:
        if r[1][0] == 'N':
            print(r)
    cursor.close()
    cn.close()


if __name__ == "__main__":
    main()
