class curva():
    def __init__(self, v1, v2, v3, ra) -> None:
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3
        self.__ra = ra

    @property
    def GetV1(self):
        return self.__v1

    @property
    def GetV2(self):
        return self.__v2

    @property
    def GetV3(self):
        return self.__v3

    @property
    def GetRa(self):
        return self.__ra

    @GetV1.setter
    def SetV1(self):
