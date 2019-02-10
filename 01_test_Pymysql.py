from pymysql import *


def main():
    conn = connect(host="localhost", port=3306, user="root", password="123456", database="jing_dong", charset="utf8")
    cs1 = conn.cursor()
    print("*" * 50)

    while True:
        input_nu = input("请输入要查询的数据：\n 1.全部\n 2.分类\n 3.品牌\n")
        if input_nu == "1":
            count = cs1.execute("select * from goods")
            print(count)
            for i in range(count):
                result = cs1.fetchone()
                print(result)
        elif input_nu == "2":
                count = cs1.execute(
                    "select g.id,c.cate_name from jing_dong.goods as g inner join jing_dong.goods_cates as c on "
                    "g.cate_id = c.id group by c.cate_name")
                print(count)
                for i in range(count):
                    result = cs1.fetchone()
                    print(result)
        elif input_nu == "3":
            count = cs1.execute(
                "select g.id,b.brand_name from jing_dong.goods as g inner join jing_dong.goods_brands as b on "
                "g.brand_id= b.id")
            print(count)
            for i in range(count):
                result = cs1.fetchone()
                print(result)
        elif input_nu == exit:
            break
        else:
            print("输入有误，请重新输入\n")
    cs1.close()
    conn.close()


if __name__ == "__main__":
    main()
