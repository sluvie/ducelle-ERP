from app.models.base import BaseTable

class User_m(BaseTable):
    
    def __init__(self):
        self.__database__ = "ducellesystem_db"
        self.__tablename__ = "t_user"
        self.__primarykey__ = "userid"
        super().__init__()
        
        
    def validate_register_account(self, key):
        try:
            data, message = self.execute("SELECT 1 FROM t_user WHERE email=%s or username=%s", (key, key, ))
            if data == None or data == []:
                return False
            
            return True
        except Exception as e:
            print(str(e))
            return False
        
        
    def validate_login(self, account):
        try:
            data, message = self.execute("SELECT password FROM t_user WHERE email=%s or username = %s", (account['email'], account['email'], ))
            if data == None or data == []:
                return False
            else:
                password = data[0][0]
                if password == account['password']:
                    return True
        except Exception as e:
            print(str(e))
            
        return False
    
    
    def get(self, account):
        try:
            data, message = self.execute("SELECT userid, name, email FROM t_user WHERE email=%s or username=%s", (account['email'], account['email'] ))
            if data == None or data == []:
                return [], "Failed to get account."
            else:
                row = {
                    "userid": data[0][0],
                    "name": data[0][1],
                    "email": data[0][2],
                }
                return row, ""
        except Exception as e:
            print(str(e))
            return [], str(e)