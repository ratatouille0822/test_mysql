import pymysql


class HandleDatabase(object):
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="jing_dong",
                                    charset="utf8")
        self.cursor1 = self.conn.cursor()

    def start_page(self):
        user_name = input("请输入用户名：")
        user_password = input("请输入密码：")
        count = self.cursor1.execute("""select * from jing_dong.customers where name = "%s" """ % user_name)
        if count > 0:
            print(self.cursor1.fetchall())
            count_pass = self.cursor1.execute(
                """select * from jing_dong.customers where name = "%s" and password = "%s" """ % (
                user_name, user_password))
            if count_pass > 0:
                print(self.cursor1.fetchall())
                print("登录成功！\r\n")

        else:
            print("用户不存在，请注册：")
            self.user_regist()

    def user_regist(self):
        pass

    @staticmethod
    def show_operations():
        print("请输入：\n\r")
        print("1. 查询所有：\n\r")
        print("2. 查询所有类别：\n\r")
        print("3. 查询所有品牌：\n\r")
        print("4. 添加一个商品分类 \n\r")

    def make_sql(self):
        option = input("请输入操作：\n\r")
        if option == '1':
            sql = "select * from goods;"
            self.execute_sql(sql)
        elif option == '2':
            sql = "select * from goods_cates;"
            self.execute_sql(sql)
        elif option == '3':
            sql = "select * from goods_brands;"
            self.execute_sql(sql)
        elif option == '4':
            name_cate = input("请输入名字")
            sql = """insert into goods_cates values (0, "%s");""" % name_cate
            self.execute_write(sql)
        else:
            pass

    def execute_sql(self, sql):
        count = self.cursor1.execute(sql)
        print(count)
        for i in range(count):
            result = self.cursor1.fetchone()
            print(result)

    def execute_write(self, sql):
        self.cursor1.execute(sql)
        self.conn.commit()

    def close_connections(self):
        self.cursor1.close()
        self.conn.close()

    def run(self):
        while True:
            self.show_operations()
            self.make_sql()

            # self.execute_sql()
            # 1self.close_connections()


def main():
    op = HandleDatabase()
    op.run()


if __name__ == "__main__":
    main()
