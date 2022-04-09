#!/usr/bin/python3
"""
Cities states safe from sql injection
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
    cursor.execute("""SELECT C.id, C.name, S.name
                    FROM cities C INNER JOIN states S ON C.state_id=S.id
                    WHERE S.name LIKE %s
                    ORDER BY C.id""",(argv[4],))
    rows = cursor.fetchall()
    res = ""
    for row in rows:
        res += row[0] + ", "
        print(res[0:-2:])
    cursor.close()
    cn.close()


if __name__ == "__main__":
    main()
