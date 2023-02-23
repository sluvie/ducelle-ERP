import psycopg2
import psycopg2.extras
import app.config as config

class BaseModel():
    __database__ = ""
    __primarykey__ = ""
    __connection__ = None

    def __init__(self) -> None:
        conf = config.DATABASE_ACCOUNT[self.__database__]
        self.__connection__ = psycopg2.connect(
            host = conf["server"],
            port = conf["port"],
            database = conf["database"],
            user = conf["user"],
            password = conf["password"]
        )
        psycopg2.extras.register_uuid()


    # ... call procedure
    def callproc(self, query, parameters):
        try:
            cursor = self.__connection__.cursor()
            cursor.execute(query, parameters)
            rows = cursor.fetchall()
            return (rows, "")
        except psycopg2.Error as e:
            print(str(e))
            return (None, str(e))

    
    # ... execute query
    def execute(self, query, parameters) -> None:
        try:
            cursor = self.__connection__.cursor()
            cursor.execute(query, parameters)
            rows = cursor.fetchall()
            return (rows, "")
        except psycopg2.Error as e:
            print(str(e))
            return (None, str(e))


class BaseTable(BaseModel):
    __tablename__ = ""
    __fields__ = []

    def __init__(self) -> None:
        super().__init__()


    # ... select all (list)
    def list(self) -> None:
        try:
            cursor = self.__connection__.cursor()
            query = "select * from %s" % (self.__tablename__)
            cursor.execute(query, ())
            rows = cursor.fetchall()
            return (rows, "")
        except psycopg2.Error as e:
            print(str(e))
            return (None, str(e))


    # ... select first row
    def readone(self, key) -> None:
        try:
            cursor = self.__connection__.cursor()
            query = "select * from %s where %s = %s" % (self.__tablename__, self.__primarykey__, "%s")
            cursor.execute(query, (key, ))
            row = cursor.fetchone()
            return (row, "")
        except psycopg2.Error as e:
            print(str(e))
            return (None, str(e))


    # ... insert multi rows
    def insert(self, data) -> None:
        try:
            cursor = self.__connection__.cursor()
            params = list()
            for row in data:
                fieldnames = ""
                fieldvalues = ""
                params.clear()
                index = 0
                for attribute, value in row.items():
                    fieldnames = fieldnames + attribute + ","
                    fieldvalues = fieldvalues + "%s,"
                    params.insert(index, value)
                    index = index + 1
                fieldnames = fieldnames[:-1]
                fieldvalues = fieldvalues[:-1]

                query = "insert into %s(%s) values(%s)" % (self.__tablename__, fieldnames, fieldvalues)
                cursor.execute(query, tuple(params))
            
            self.__connection__.commit()
            return (True, "")
        except psycopg2.Error as e:
            print(str(e))
            self.__connection__.rollback()
            return (False, str(e))


    # ... update multi rows
    def update(self, key, data) -> None:
        try:
            cursor = self.__connection__.cursor()
            params = list()
            for row in data:
                fieldset = ""
                params.clear()
                index = 0
                for attribute, value in row.items():
                    fieldset = fieldset + attribute + "=%s,"
                    params.insert(index, value)
                    index = index + 1
                fieldset = fieldset[:-1]

                query = "update %s set %s where %s=%s" % (self.__tablename__, fieldset, self.__primarykey__, "%s")
                params.insert(index, key)
                cursor.execute(query, tuple(params))
            
            self.__connection__.commit()
            return (True, "")
        except psycopg2.Error as e:
            print(str(e))
            self.__connection__.rollback()
            return (False, str(e))


    # ... delete single data
    def delete(self, key) -> None:
        try:
            cursor = self.__connection__.cursor()
            query = "delete from %s where %s = %s" % (self.__tablename__, self.__primarykey__, "%s")
            cursor.execute(query, (key, ))
            self.__connection__.commit()
            return (True, "")
        except psycopg2.Error as e:
            print(str(e))
            self.__connection__.rollback()
            return (False, str(e))


    # ... delete single data (only flag)
    def delete_flag(self, key) -> None:
        try:
            cursor = self.__connection__.cursor()
            query = "update %s set deleteflag = 1 where %s = %s" % (self.__tablename__, self.__primarykey__, "%s")
            cursor.execute(query, (key, ))
            self.__connection__.commit()
            return (True, "")
        except psycopg2.Error as e:
            print(str(e))
            self.__connection__.rollback()
            return (False, str(e))


class BaseQuery(BaseModel):

    def __init__(self) -> None:
        super().__init__()