import PyMySQL

config = {
    'database': 'ecojejudb',
    'user': 'root',
    'password': '1111',
    'host':'127.0.0.1',
    'port': 3306,
    'charset':'utf8',
    'use_unicode':True
}
class mysqlDao:
    def getConnection(self):
        conn = PyMySQL.connect(**config);
        cursor = conn.cursor();
        return conn;

    def close(self, conn, cursor):
        if cursor != None:
            cursor.close();
        if conn != None:
            conn.close();