from database.Frame.mysqlDAO import mysqlDao
from database.SQL.sql import UserSql
class UserDB(mysqlDao):
    def __init__(self,dbName):
        super().__init__(dbName);

    def insert(self, user):
        try:
            conn = self.getConnection();
            cursor = conn.cursor();
            cursor.execute(UserSql.insert_user,(user.getId(), user.getPwd(), user.getName(), user.getArea()));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);