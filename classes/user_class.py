

class User():
    def __init__(self, id, user_name, password) -> None:
        self.__id = id
        self.__user_name = user_name
        self.__password = password

    @property
    def Get_id(self):
        return self.__id

    @property
    def Get_user_name(self):
        return self.__user_name

    @property
    def Get_password(self):
        return self.__password

    @Get_user_name.setter
    def Set_user_name(self, valor):
        if valor.isalnum():
            self.__user_name = valor
        else:
            print("Caracteres no validos")

    @Get_password.setter
    def Set_password(self, valor):
        if valor.isalnum():
            self.__password = valor
        else:
            print("Caracteres no validos")


usuario = User(0, "julioasmb", "123")
