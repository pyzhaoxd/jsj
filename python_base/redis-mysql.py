#python操作redis
from redis import StrictRedis
redis = StrictRedis(host='localhost',port = 6379,db = 1,password = 123456)
redis.set('name', 'Bob')
print(redis.get('name'))
print(redis.exists('name'))


#使用ConnectionPool连接
# from redis import ConnectionPool
# pool = ConnectionPool(host='localhost',port = 6379,db = 1, password = 123456)
# redis = StrictRedis(connection_pool=pool)
# redis.set('age',16)
# print(redis.get('age'))

#python操作数据库
import pymysql
import jsons
def connect_mysql():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="zhaoxd",
                         password="123456", database="test", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "SELECT * FROM dns_cpe_mapping WHERE client_ip = '10.188.2.73'"
    # 使用execute方法执行SQL语句
    cursor.execute(sql)
    data = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    a = list(data)
    return a

def main():
    print(connect_mysql())

if __name__ == '__main__':
    main()