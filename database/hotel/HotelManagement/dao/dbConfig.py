import psycopg2

"""数据源配置信息"""
# localSourceConfig = {
#     'host': 'localhost',
#     'port': 3306,
#     'user': 'hotel',
#     'passwd': '123456',
#     'db': 'hotel',
#     'charset': 'utf8',
#     'cursorclass' : pymysql.cursors.DictCursor
# }

localSourceConfig = {
    'host': '120.46.130.234',
    'port': 26000,
    'user': 'lian',
    'passwd': 'Bigdata@123',
    'db': 'postgres',
}
# import psycopg2.extras
# conn = psycopg2.connect(dbname="postgres",
#                             user="lian",
#                             password="Bigdata@123",
#                             host="120.46.130.234",
#                             port="26000")
# cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)




