import pymysql


def main():
    no = int(input('部门编号:'))
    name = input('部门名称:')
    con = input('部门所在地:')

    con = pymysql.connect(host='localhost', port=3306,
                          db='datasets', user='root',
                          passwd='123456', charset='utf8')
    try:
        with con.cursor() as cursor:
            # execute执行，后面括号是sql语句,%s表示占位符，此处必须使用%s，否则会报错
            result = cursor.execute("insert into dat_ages values(%s,%s,%s)",
                                    (no, name, location))
            if result == 1:
                print('添加成功')
            # 手动提交
            con.commit()
    # 捕获异常
    except pymysql.MySQLError as e:
        print(e)
        # 撤销
        con.rollback()
    finally:
        con.close()


if __name__ == '__main__':
    main()





