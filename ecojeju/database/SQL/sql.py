class UserSql:
    insert_user = ''' INSERT  INTO  user VALUES (?,?,?,?) ''';
    update_user = ''' UPDATE  user  SET  PWD=?,  NAME=?  WHERE  ID=? ''';
    delete_user = ''' DELETE  FROM  USERDB  WHERE  ID=? ''';
    select_user = ''' SELECT  *  FROM  USERDB  WHERE ID=? ''';
    selectall_user = ''' SELECT  * FROM USERDB ''';
