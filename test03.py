import pymysql


def main():
    con = pymysql.connect(host='localhost', port=3306,
                          db='datasets', user='root',
                          passwd='123456', charset='utf8')
    try:
        with con.cursor() as cursor:
            # execute执行，后面括号是sql语句。查询所有
            cursor.execute("select * from dat_movies")
            # fetchall()抓取所有
            print(cursor.fetchall())
            # fetchone()只拿一条
            print(cursor.fetchone())
            # fetchmany(2)指定拿取参数
            print(cursor.fetchmany(2))
    # 捕获异常
    except pymysql.MySQLError as e:
        print(e)
        # 撤销
        con.rollback()
    finally:
        con.close()


if __name__ == '__main__':
    main()





