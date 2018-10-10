import pymysql

"""
关系型数据库支持事务
事务：把多个操作当成一个原子性操作，要么全部成功，要么全部失败
A —— 原子性：不能拆分
C—— 一致性：事务前后数据状态要一致
I—— 隔离线：事务不能看到彼此的中间状态
D—— 持久性：事务完成后数据要持久化
"""
# host:主机IP
# port：端口
# db：数据库名称
# user：登录用户名
# passwd：密码
# charset：字符集
# autocommit:设置False，表示不要自动提交，不会反应到数据库上面；设置True自动提交生效
# 设置手动提交


def main():
    con = pymysql.connect(host='localhost', port=3306,
                          db='datasets', user='root',
                          passwd='123456', charset='utf8')
    try:
        with con.cursor() as cursor:
            # execute执行，后面括号里面是sql语句
            result = cursor.execute("delete from tbdept where deptno=40")
            # if result == 1:
            #     print('删除成功')
            # 三元运算符
            print('删除成功' if result else '删除失败')
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

# 事务环境
# 开启事务环境
# begin;

# 删除(执行要做的多个操作)
# delete from tbemp;

# 提交让事务生效
# commit;

# 查询全部
# select * from tbemp;

# 回滚(撤销事务)
# rollback;
