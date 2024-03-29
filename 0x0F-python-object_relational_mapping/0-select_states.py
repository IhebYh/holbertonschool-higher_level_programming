#!/usr/bin/python3
"""
List all states
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
    query = "SELECT id,name FROM states ORDER BY id ASC"
    cursor.execute(query)
    res = cursor.fetchall()
    for r in res:
        print(r)
    cursor.close()
    cn.close()


if __name__ == "__main__":
    main()
